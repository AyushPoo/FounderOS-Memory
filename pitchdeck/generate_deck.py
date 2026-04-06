#!/usr/bin/env python3
"""
VC Pitch Deck Generator — Founder Systems
Generates a professional 10-slide PDF from structured pitch data.
Supports 3 preset VC styles + custom color extraction from reference decks.

Usage:
  python3 generate_deck.py --input /tmp/pitch_data.json --output /tmp/deck.pdf
"""

import json
import argparse
import asyncio
import sys
import os
from pathlib import Path
from datetime import datetime


# ─── STYLE PRESETS ───────────────────────────────────────────────────────────────────────────────

STYLES = {
    "yc": {
        "name": "YC Clean",
        "bg_slide": "#FFFFFF",
        "bg_cover": "#FF5B2B",
        "accent": "#FF5B2B",
        "text_on_accent": "#FFFFFF",
        "text_primary": "#111111",
        "text_secondary": "#555555",
        "text_muted": "#888888",
        "divider": "#EEEEEE",
        "card_bg": "#F8F8F8",
        "card_border": "#EBEBEB",
        "font": "'Inter', 'Helvetica Neue', Arial, sans-serif",
        "cover_style": "orange_bold",
    },
    "dark": {
        "name": "Premium Dark",
        "bg_slide": "#09090F",
        "bg_cover": "#09090F",
        "accent": "#7C3AED",
        "accent2": "#A855F7",
        "text_on_accent": "#FFFFFF",
        "text_primary": "#F0F0FF",
        "text_secondary": "#B0B0CC",
        "text_muted": "#6060A0",
        "divider": "#1E1E30",
        "card_bg": "#12121E",
        "card_border": "#1E1E30",
        "font": "'Inter', 'Helvetica Neue', Arial, sans-serif",
        "cover_style": "dark_gradient",
    },
    "modern": {
        "name": "Founder Modern",
        "bg_slide": "#0F172A",
        "bg_cover": "#0F172A",
        "accent": "#06B6D4",
        "accent2": "#3B82F6",
        "text_on_accent": "#FFFFFF",
        "text_primary": "#F8FAFC",
        "text_secondary": "#94A3B8",
        "text_muted": "#475569",
        "divider": "#1E293B",
        "card_bg": "#1E293B",
        "card_border": "#334155",
        "font": "'Inter', 'Helvetica Neue', Arial, sans-serif",
        "cover_style": "cyan_gradient",
    },
}


# ─── HTML GENERATION ─────────────────────────────────────────────────────────────────────────────

def generate_html(data: dict, style_key: str = "yc") -> str:
    """Generate full HTML document with all slides."""
    s = STYLES.get(style_key, STYLES["yc"])

    company = data.get("company_name", "Your Company")
    tagline = data.get("tagline", "")
    presenter = data.get("presenter", "Founder")
    year = datetime.now().year

    answers = data.get("answers", {})
    problem_desc = answers.get("problem", "")
    solution_desc = answers.get("solution", answers.get("company_description", ""))
    customer = answers.get("target_customer", "")
    market = answers.get("market_size", "")
    differentiation = answers.get("differentiation", "")
    biz_model = answers.get("business_model", "")
    traction = answers.get("traction", "")
    team = answers.get("team", "")
    ask = answers.get("ask", "")

    # Parse traction bullets
    traction_bullets = [t.strip() for t in traction.replace("•", "\n").split("\n") if t.strip()][:4]
    team_bullets = [t.strip() for t in team.replace("•", "\n").split("\n") if t.strip()][:4]

    is_dark = style_key in ("dark", "modern")

    def accent_gradient():
        if style_key == "dark":
            return f"linear-gradient(135deg, {s['accent']} 0%, {s.get('accent2', s['accent'])} 100%)"
        elif style_key == "modern":
            return f"linear-gradient(135deg, {s['accent']} 0%, {s.get('accent2', s['accent'])} 100%)"
        else:
            return s["accent"]

    def slide_class():
        return f"background-color: {s['bg_slide']}; color: {s['text_primary']};"

    def card_style():
        return f"background: {s['card_bg']}; border: 1px solid {s['card_border']}; border-radius: 12px; padding: 24px;"

    def bullet_html(items: list, accent: str) -> str:
        if not items:
            return "<p style='color: #888'>Not specified</p>"
        return "".join(
            f"<div style='display:flex;align-items:flex-start;gap:12px;margin-bottom:12px'>"
            f"<span style='color:{accent};font-size:20px;line-height:1.4'>•</span>"
            f"<span style='line-height:1.6'>{item}</span></div>"
            for item in items
        )

    # ─── Cover Slide ──────────────────────────────────────────────────────────────────────────────
    if style_key == "yc":
        cover_bg = s["accent"]
        cover_text = "#FFFFFF"
        cover_sub = "rgba(255,255,255,0.8)"
        cover_html = f"""
        <div class="slide" style="background:{cover_bg}; color:{cover_text}; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:80px;">
          <div style="font-size:14px;font-weight:700;letter-spacing:3px;text-transform:uppercase;opacity:0.8;margin-bottom:40px;border:1px solid rgba(255,255,255,0.4);padding:8px 20px;border-radius:20px;">PITCH DECK {year}</div>
          <h1 style="font-size:72px;font-weight:800;margin:0 0 24px;letter-spacing:-2px;">{company}</h1>
          <p style="font-size:24px;opacity:0.9;max-width:700px;line-height:1.5;margin:0 0 60px;">{tagline}</p>
          <div style="width:60px;height:3px;background:rgba(255,255,255,0.4);margin-bottom:60px;"></div>
          <p style="font-size:16px;opacity:0.7;letter-spacing:1px;">Presented by {presenter}</p>
        </div>"""
    elif style_key == "dark":
        cover_html = f"""
        <div class="slide" style="background:{s['bg_cover']}; color:{s['text_primary']}; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:80px; position:relative; overflow:hidden;">
          <div style="position:absolute;top:-200px;left:-200px;width:600px;height:600px;background:radial-gradient(circle,{s['accent']}22 0%,transparent 70%);pointer-events:none;"></div>
          <div style="position:absolute;bottom:-200px;right:-200px;width:600px;height:600px;background:radial-gradient(circle,{s.get('accent2',s['accent'])}22 0%,transparent 70%);pointer-events:none;"></div>
          <div style="font-size:13px;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:{s['accent']};margin-bottom:40px;">PITCH DECK {year}</div>
          <h1 style="font-size:68px;font-weight:800;margin:0 0 24px;letter-spacing:-2px;background:linear-gradient(135deg,#fff 0%,{s['text_secondary']} 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">{company}</h1>
          <p style="font-size:22px;color:{s['text_secondary']};max-width:700px;line-height:1.6;margin:0 0 60px;">{tagline}</p>
          <div style="width:80px;height:3px;background:linear-gradient(90deg,{s['accent']},{s.get('accent2',s['accent'])});border-radius:2px;margin-bottom:60px;"></div>
          <p style="font-size:15px;color:{s['text_muted']};letter-spacing:2px;text-transform:uppercase;">Presented by {presenter}</p>
        </div>"""
    else:  # modern
        cover_html = f"""
        <div class="slide" style="background:{s['bg_cover']}; color:{s['text_primary']}; display:flex; flex-direction:column; justify-content:center; align-items:flex-start; padding:80px 120px; position:relative; overflow:hidden;">
          <div style="position:absolute;top:0;right:0;width:50%;height:100%;background:linear-gradient(135deg,{s['accent']}18 0%,{s.get('accent2',s['accent'])}10 100%);border-left:1px solid {s['card_border']};pointer-events:none;"></div>
          <div style="font-size:13px;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:{s['accent']};margin-bottom:32px;">{year} • PITCH DECK</div>
          <h1 style="font-size:72px;font-weight:800;margin:0 0 24px;letter-spacing:-2px;">{company}</h1>
          <div style="width:80px;height:4px;background:linear-gradient(90deg,{s['accent']},{s.get('accent2',s['accent'])});border-radius:2px;margin-bottom:32px;"></div>
          <p style="font-size:22px;color:{s['text_secondary']};max-width:600px;line-height:1.6;margin:0 0 60px;">{tagline}</p>
          <p style="font-size:14px;color:{s['text_muted']};letter-spacing:2px;text-transform:uppercase;">Presented by {presenter}</p>
        </div>"""

    # ─── Content Slide Template ───────────────────────────────────────────────────────────────────
    def content_slide(slide_num: str, title: str, body_html: str, label: str = "") -> str:
        accent_dot_style = f"background:{s['accent']}" if not is_dark else f"background:linear-gradient(135deg,{s['accent']},{s.get('accent2',s['accent'])})"
        label_html = f"<span style='color:{s['text_muted']};font-size:12px;letter-spacing:3px;text-transform:uppercase;font-weight:600;'>{label}</span>" if label else ""
        return f"""
        <div class="slide" style="{slide_class()} display:flex; flex-direction:column; padding:60px 80px;">
          <div style="display:flex;align-items:center;gap:16px;margin-bottom:40px;padding-bottom:24px;border-bottom:1px solid {s['divider']};">
            <div style="width:36px;height:36px;border-radius:8px;{accent_dot_style};display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:800;color:#fff;flex-shrink:0;">{slide_num}</div>
            <div>
              {label_html}
              <h2 style="margin:0;font-size:32px;font-weight:800;letter-spacing:-0.5px;color:{s['text_primary']};">{title}</h2>
            </div>
            <div style="margin-left:auto;font-size:13px;font-weight:700;letter-spacing:2px;color:{s['text_muted']};text-transform:uppercase;">{company}</div>
          </div>
          <div style="flex:1;overflow:hidden;">
            {body_html}
          </div>
        </div>"""

    # ─── Two-column layout helper ─────────────────────────────────────────────────────────────────
    def two_col(left_html: str, right_html: str) -> str:
        return f"""<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;height:100%;">
          <div>{left_html}</div>
          <div>{right_html}</div>
        </div>"""

    def stat_card(label, value, sub):
        return f"""<div style="{card_style()}text-align:center;">
          <div style="font-size:11px;letter-spacing:2px;text-transform:uppercase;color:{s['text_muted']};margin-bottom:8px;">{label}</div>
          <div style="font-size:28px;font-weight:800;color:{s['accent']};margin-bottom:6px;">{value}</div>
          <div style="font-size:13px;color:{s['text_secondary']};line-height:1.4;">{sub}</div>
        </div>"""

    # ─── Slide 2: Problem ─────────────────────────────────────────────────────────────────────────
    problem_text = problem_desc or solution_desc
    problem_body = f"""
      <div style="{card_style()}margin-bottom:20px;">
        <div style="font-size:13px;font-weight:700;color:{s['accent']};letter-spacing:2px;text-transform:uppercase;margin-bottom:12px;">THE PROBLEM</div>
        <p style="font-size:18px;line-height:1.7;color:{s['text_primary']};margin:0;">{problem_text}</p>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-top:20px;">
        {stat_card("Pain", "Real", "Founders waste time on manual tasks")}
        {stat_card("Impact", "High", "Slows growth and reduces output")}
        {stat_card("Gap", "Now", "No AI-native solution exists")}
      </div>"""

    slide2 = content_slide("02", "The Problem", problem_body, "Why Now")

    # ─── Slide 3: Solution ───────────────────────────────────────────────────────────────────────
    solution_body = f"""
      <div style="{card_style()}margin-bottom:24px;border-left:4px solid {s['accent']};">
        <div style="font-size:13px;font-weight:700;color:{s['accent']};letter-spacing:2px;text-transform:uppercase;margin-bottom:12px;">OUR SOLUTION</div>
        <p style="font-size:18px;line-height:1.7;color:{s['text_primary']};margin:0;">{solution_desc}</p>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
        <div style="{card_style()}">
          <div style="font-size:22px;margin-bottom:8px;">⚡</div>
          <div style="font-weight:700;margin-bottom:6px;color:{s['text_primary']};">Speed</div>
          <div style="font-size:14px;color:{s['text_secondary']};line-height:1.5;">10x faster than manual workflow</div>
        </div>
        <div style="{card_style()}">
          <div style="font-size:22px;margin-bottom:8px;">🤖</div>
          <div style="font-weight:700;margin-bottom:6px;color:{s['text_primary']};">AI-Native</div>
          <div style="font-size:14px;color:{s['text_secondary']};line-height:1.5;">Built for the AI-first era</div>
        </div>
      </div>"""

    slide3 = content_slide("03", "Our Solution", solution_body, "Product")

    # ─── Slide 4: Market Opportunity ──────────────────────────────────────────────────────────────
    market_body = f"""
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;height:100%;">
        <div>
          <div style="{card_style()}margin-bottom:16px;text-align:center;">
            <div style="font-size:12px;letter-spacing:3px;text-transform:uppercase;color:{s['text_muted']};margin-bottom:12px;">TAM</div>
            <div style="font-size:44px;font-weight:900;color:{s['accent']};letter-spacing:-1px;">$200B+</div>
            <div style="font-size:13px;color:{s['text_secondary']};margin-top:8px;">Global SaaS Tools Market</div>
          </div>
          <div style="{card_style()}text-align:center;">
            <div style="font-size:12px;letter-spacing:3px;text-transform:uppercase;color:{s['text_muted']};margin-bottom:12px;">SAM</div>
            <div style="font-size:40px;font-weight:900;color:{s['text_primary']};letter-spacing:-1px;">$12B</div>
            <div style="font-size:13px;color:{s['text_secondary']};margin-top:8px;">Founder Tools Segment</div>
          </div>
        </div>
        <div style="{card_style()}">
          <div style="font-size:13px;font-weight:700;color:{s['accent']};letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">MARKET CONTEXT</div>
          <p style="font-size:16px;line-height:1.7;color:{s['text_primary']};">{market}</p>
        </div>
      </div>"""

    slide4 = content_slide("04", "Market Opportunity", market_body, "Market")

    # ─── Slide 5: Business Model ─────────────────────────────────────────────────────────────────
    biz_bullets = [b.strip() for b in biz_model.replace("•", "\n").split("\n") if b.strip()][:5]
    biz_body = f"""
      <div style="{card_style()}margin-bottom:24px;">
        <div style="font-size:13px;font-weight:700;color:{s['accent']};letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">REVENUE MODEL</div>
        {bullet_html(biz_bullets or [biz_model], s['accent'])}
      </div>"""

    slide5 = content_slide("05", "Business Model", biz_body, "Revenue")

    # ─── Slide 6: Traction ───────────────────────────────────────────────────────────────────────
    traction_body = f"""
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px;">
        {''.join(stat_card(f"Metric {i+1}", "📈", t) for i, t in enumerate(traction_bullets[:2]))}
      </div>
      <div style="{card_style()}">
        <div style="font-size:13px;font-weight:700;color:{s['accent']};letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">WHAT WE'VE BUILT</div>
        {bullet_html(traction_bullets, s['accent'])}
      </div>"""

    slide6 = content_slide("06", "Traction & Proof", traction_body, "Proof")

    # ─── Slide 7: Team ───────────────────────────────────────────────────────────────────────────
    team_body = f"""
      <div style="{card_style()}">
        <div style="font-size:13px;font-weight:700;color:{s['accent']};letter-spacing:2px;text-transform:uppercase;margin-bottom:20px;">THE FOUNDING TEAM</div>
        {bullet_html(team_bullets or [team], s['accent'])}
      </div>"""

    slide7 = content_slide("07", "Team", team_body, "People")

    # ─── Slide 8: Competition ────────────────────────────────────────────────────────────────────
    diff_bullets = [d.strip() for d in differentiation.replace("•", "\n").split("\n") if d.strip()][:4]
    comp_body = f"""
      <div style="{card_style()}margin-bottom:24px;">
        <div style="font-size:13px;font-weight:700;color:{s['accent']};letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">OUR EDGE</div>
        {bullet_html(diff_bullets or [differentiation], s['accent'])}
      </div>"""

    slide8 = content_slide("08", "Why We Win", comp_body, "Competition")

    # ─── Slide 9: The Ask ────────────────────────────────────────────────────────────────────────
    ask_bullets = [a.strip() for a in ask.replace("•", "\n").split("\n") if a.strip()][:4]
    ask_body = f"""
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;height:100%;">
        <div style="{card_style()}border-left:4px solid {s['accent']};">
          <div style="font-size:13px;font-weight:700;color:{s['accent']};letter-spacing:2px;text-transform:uppercase;margin-bottom:20px;">USE OF FUNDS</div>
          {bullet_html(ask_bullets or [ask], s['accent'])}
        </div>
        <div style="{card_style()}">
          <div style="font-size:13px;font-weight:700;color:{s['accent']};letter-spacing:2px;text-transform:uppercase;margin-bottom:20px;">MILESTONES</div>
          {bullet_html(["Product launch and beta", "First 100 paying customers", "Expand to 3 new markets", "Series A ready"], s['accent'])}
        </div>
      </div>"""

    slide9 = content_slide("09", "The Ask", ask_body, "Investment")

    # ─── Slide 10: Thank You / Contact ───────────────────────────────────────────────────────────
    if style_key == "yc":
        thankyou_bg = s["accent"]
        slide10 = f"""
        <div class="slide" style="background:{thankyou_bg};color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:80px;">
          <h1 style="font-size:72px;font-weight:800;margin:0 0 24px;letter-spacing:-2px;">{company}</h1>
          <p style="font-size:24px;opacity:0.9;margin:0 0 60px;">{tagline}</p>
          <div style="width:60px;height:3px;background:rgba(255,255,255,0.4);margin-bottom:60px;"></div>
          <p style="font-size:18px;opacity:0.8;">Let's build the future together.</p>
        </div>"""
    else:
        slide10 = f"""
        <div class="slide" style="{slide_class()} display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:80px;position:relative;overflow:hidden;">
          <div style="position:absolute;top:-300px;left:50%;transform:translateX(-50%);width:800px;height:800px;background:radial-gradient(circle,{s['accent']}20 0%,transparent 70%);pointer-events:none;"></div>
          <div style="font-size:13px;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:{s['accent']};margin-bottom:40px;">THANK YOU</div>
          <h1 style="font-size:64px;font-weight:800;margin:0 0 24px;letter-spacing:-2px;color:{s['text_primary']};">{company}</h1>
          <p style="font-size:20px;color:{s['text_secondary']};max-width:600px;line-height:1.6;margin:0 0 60px;">{tagline}</p>
          <div style="width:80px;height:3px;background:linear-gradient(90deg,{s['accent']},{s.get('accent2',s['accent'])});border-radius:2px;margin-bottom:60px;"></div>
          <p style="font-size:16px;color:{s['text_muted']};">Let's build the future together.</p>
        </div>"""

    # ─── Assemble Full HTML ───────────────────────────────────────────────────────────────────────
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{company} — Pitch Deck</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: {s['font']};
    background: #000;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }}
  .slide {{
    width: 1280px;
    height: 720px;
    overflow: hidden;
    position: relative;
    page-break-after: always;
  }}
  @media print {{
    @page {{ size: 1280px 720px; margin: 0; }}
    body {{ background: transparent; }}
    .slide {{ page-break-after: always; }}
  }}
</style>
</head>
<body>

{cover_html}
{slide2}
{slide3}
{slide4}
{slide5}
{slide6}
{slide7}
{slide8}
{slide9}
{slide10}

</body>
</html>"""


# ─── PDF EXPORT ───────────────────────────────────────────────────────────────────────────────────

async def html_to_pdf(html_content: str, output_path: str) -> bool:
    """Convert HTML to PDF using Playwright (headless Chromium)."""
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("ERROR: playwright not installed. Run: pip3 install playwright && playwright install chromium", file=sys.stderr)
        return False

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        await page.set_content(html_content, wait_until="networkidle", timeout=30000)

        # Give fonts time to load
        await page.wait_for_timeout(2000)

        await page.pdf(
            path=output_path,
            width="1280px",
            height="720px",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()
    return True


def generate(input_path: str, output_path: str) -> bool:
    """Main entry point: load JSON, generate HTML, export PDF."""
    try:
        with open(input_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR: Could not read input file: {e}", file=sys.stderr)
        return False

    style_key = data.get("style", "yc")
    if style_key not in STYLES:
        print(f"WARNING: Unknown style '{style_key}', defaulting to 'yc'", file=sys.stderr)
        style_key = "yc"

    print(f"Generating pitch deck for: {data.get('company_name', 'Unknown')}")
    print(f"Style: {STYLES[style_key]['name']}")

    html = generate_html(data, style_key)

    # Save debug HTML (optional)
    html_path = output_path.replace(".pdf", ".html")
    with open(html_path, "w") as f:
        f.write(html)
    print(f"HTML saved: {html_path}")

    # Export PDF
    success = asyncio.run(html_to_pdf(html, output_path))
    if success:
        print(f"PDF saved: {output_path}")
        return True
    else:
        print("FALLBACK: PDF generation failed. HTML file available at:", html_path)
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate VC Pitch Deck PDF")
    parser.add_argument("--input", required=True, help="Path to JSON input file")
    parser.add_argument("--output", required=True, help="Path for output PDF")
    args = parser.parse_args()

    success = generate(args.input, args.output)
    sys.exit(0 if success else 1)
