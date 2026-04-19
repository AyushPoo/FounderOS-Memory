#!/usr/bin/env python3
"""
Atlas Pitch Deck Tool — Founder Systems
Called by Atlas via ssh_azure when the user wants to generate a pitch deck.

Atlas conducts the interview conversationally, then calls this script once
with all collected answers. This script:
  1. Builds the pitch data JSON
  2. Calls generate_deck.py to create the PDF
  3. Sends the PDF back to the user via Telegram Bot API
  4. Cleans up temp files

Usage:
  python3 atlas_pitchdeck.py \
    --chat_id 7866603961 \
    --company "Founder Systems" \
    --tagline "Autonomous AI product factory for solo founders" \
    --description "We help founders automate their product pipeline using AI agents" \
    --customer "Solo founders and micro-teams (1-3 people)" \
    --market "Global SaaS tools market is $200B+. Our TAM is $5B" \
    --differentiation "Unlike Zapier we handle full product builds autonomously" \
    --biz_model "49/month SaaS subscription, 299/month enterprise" \
    --traction "150 waitlist, 3 paying pilots at 500 MRR" \
    --team "Ayush Poojary, CA background, 5 years in SaaS" \
    --ask "Raising 500K pre-seed, 40% product 30% marketing" \
    --style yc \
    --presenter "Ayush Poojary"
"""

import argparse
import json
import os
import sys
import subprocess
import requests
import tempfile
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
GENERATOR = SCRIPT_DIR / "generate_deck.py"

# Load Telegram bot token from .env
def get_telegram_token() -> str:
    env_path = Path("/home/ayush/.env")
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("TELEGRAM_BOT_TOKEN=") or line.startswith("ATLAS_TELEGRAM_BOT_TOKEN="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    # Fallback: check environment
    return os.environ.get("TELEGRAM_BOT_TOKEN", os.environ.get("ATLAS_TELEGRAM_BOT_TOKEN", ""))


def send_telegram_message(token: str, chat_id: str, text: str, parse_mode: str = "Markdown"):
    """Send a text message via Telegram Bot API."""
    try:
        resp = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": text, "parse_mode": parse_mode},
            timeout=15
        )
        return resp.ok
    except Exception as e:
        print(f"Telegram message error: {e}", file=sys.stderr)
        return False


def send_telegram_document(token: str, chat_id: str, file_path: str, caption: str = ""):
    """Send a PDF document via Telegram Bot API."""
    try:
        with open(file_path, "rb") as f:
            resp = requests.post(
                f"https://api.telegram.org/bot{token}/sendDocument",
                data={"chat_id": chat_id, "caption": caption, "parse_mode": "Markdown"},
                files={"document": (Path(file_path).name, f, "application/pdf")},
                timeout=60
            )
        if resp.ok:
            return True
        else:
            print(f"Telegram document error: {resp.status_code} {resp.text}", file=sys.stderr)
            return False
    except Exception as e:
        print(f"Telegram document error: {e}", file=sys.stderr)
        return False


def build_pitch_data(args) -> dict:
    """Build the structured pitch data dict from CLI args."""
    return {
        "company_name": args.company,
        "tagline": args.tagline,
        "presenter": args.presenter or args.company,
        "style": args.style,
        "answers": {
            "company_description": args.description,
            "problem": args.description,
            "solution": args.description,
            "target_customer": args.customer,
            "market_size": args.market,
            "differentiation": args.differentiation,
            "business_model": args.biz_model,
            "traction": args.traction,
            "team": args.team,
            "ask": args.ask,
        },
        "generated_at": datetime.utcnow().isoformat(),
    }


def main():
    parser = argparse.ArgumentParser(description="Atlas Pitch Deck Generator")
    parser.add_argument("--chat_id", required=True, help="Telegram chat ID to send the result to")
    parser.add_argument("--company", required=True, help="Company/startup name")
    parser.add_argument("--tagline", required=True, help="One-line company tagline")
    parser.add_argument("--description", required=True, help="What the startup does + problem it solves")
    parser.add_argument("--customer", required=True, help="Target customer description")
    parser.add_argument("--market", required=True, help="Market size and opportunity")
    parser.add_argument("--differentiation", required=True, help="Competitive differentiation")
    parser.add_argument("--biz_model", required=True, help="Business/revenue model")
    parser.add_argument("--traction", required=True, help="Traction metrics and proof points")
    parser.add_argument("--team", required=True, help="Team members and backgrounds")
    parser.add_argument("--ask", required=True, help="Fundraising ask and use of funds")
    parser.add_argument("--style", choices=["yc", "dark", "modern"], default="yc", help="Deck visual style")
    parser.add_argument("--presenter", default="", help="Presenter name for cover slide")
    parser.add_argument("--ref_file", default="", help="Path to reference PDF/PPTX for style extraction")
    args = parser.parse_args()

    token = get_telegram_token()
    if not token:
        print("ERROR: Telegram bot token not found in /home/ayush/.env", file=sys.stderr)
        sys.exit(1)

    # ── Handle custom style from reference deck ────────────────────────────────
    custom_style_path = None
    if args.ref_file and Path(args.ref_file).exists():
        print(f"Extracting style from reference: {args.ref_file}")
        custom_style_path = f"/tmp/pitchdeck_custom_style_{args.chat_id}.json"
        result = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "extract_style.py"),
             "--input", args.ref_file,
             "--output", custom_style_path],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"Style extraction failed: {result.stderr}", file=sys.stderr)
            custom_style_path = None

    # ── Build pitch data ──────────────────────────────────────────────────────
    pitch_data = build_pitch_data(args)

    # If custom style was extracted, load it and inject
    if custom_style_path and Path(custom_style_path).exists():
        with open(custom_style_path) as f:
            pitch_data["custom_style"] = json.load(f)
        pitch_data["style"] = "custom"

    # Save pitch data to temp file
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    company_slug = args.company.lower().replace(" ", "_")[:20]
    input_path = f"/tmp/pitchdeck_input_{args.chat_id}_{ts}.json"
    output_path = f"/tmp/pitchdeck_{company_slug}_{ts}.pdf"

    with open(input_path, "w") as f:
        json.dump(pitch_data, f, indent=2)

    print(f"Pitch data saved: {input_path}")

    # ── Send "generating" message ─────────────────────────────────────────────
    send_telegram_message(
        token, args.chat_id,
        "⚙️ *Generating your pitch deck...*\n\nBuilding 10 slides with your pitch data. This takes ~30-60 seconds.\n\n_Stand by..._"
    )

    # ── Run PDF generator ─────────────────────────────────────────────────────
    print(f"Generating PDF: {output_path}")
    result = subprocess.run(
        [sys.executable, str(GENERATOR), "--input", input_path, "--output", output_path],
        capture_output=True, text=True, timeout=120
    )

    print("Generator stdout:", result.stdout)
    if result.stderr:
        print("Generator stderr:", result.stderr, file=sys.stderr)

    # ── Check for PDF output ──────────────────────────────────────────────────
    pdf_exists = Path(output_path).exists() and Path(output_path).stat().st_size > 1000
    html_path = output_path.replace(".pdf", ".html")
    html_exists = Path(html_path).exists()

    if pdf_exists:
        print(f"PDF generated: {output_path} ({Path(output_path).stat().st_size // 1024}KB)")
        # Send the PDF
        style_names = {"yc": "YC Clean ⚪", "dark": "Premium Dark 🟣", "modern": "Founder Modern 🔵", "custom": "Custom 🎨"}
        caption = (
            f"🎉 *{args.company} — Pitch Deck*\n\n"
            f"Style: {style_names.get(args.style, args.style)}\n"
            f"Slides: 10 (Cover → Problem → Solution → Market → Business Model → Traction → Team → Competition → Ask → Closing)\n\n"
            f"_Built with Founder Systems AI_"
        )
        success = send_telegram_document(token, args.chat_id, output_path, caption)
        if success:
            print("PDF sent to Telegram successfully")
        else:
            print("ERROR: Failed to send PDF to Telegram", file=sys.stderr)
            send_telegram_message(token, args.chat_id, "❌ PDF generation succeeded but Telegram delivery failed. Check Azure VM at: " + output_path)

    elif html_exists:
        # Playwright failed but HTML is available — notify user
        print(f"HTML fallback: {html_path}")
        send_telegram_message(
            token, args.chat_id,
            f"⚠️ *PDF generation encountered an issue.*\n\n"
            f"Your pitch deck HTML is ready at:\n`{html_path}`\n\n"
            f"You can open this in a browser and print to PDF.\n"
            f"_To fix: run `playwright install chromium` on the Azure VM._"
        )
    else:
        print(f"ERROR: Generator failed. Return code: {result.returncode}", file=sys.stderr)
        send_telegram_message(
            token, args.chat_id,
            "❌ *Generation failed.* Please try again or contact support.\n\n"
            f"Error: `{result.stderr[:200] if result.stderr else 'Unknown error'}`"
        )

    # ── Cleanup ───────────────────────────────────────────────────────────────
    for f in [input_path]:
        try:
            os.remove(f)
        except Exception:
            pass

    print("Done.")


if __name__ == "__main__":
    main()
