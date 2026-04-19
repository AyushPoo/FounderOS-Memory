#!/usr/bin/env python3
"""
Conversation State Manager — Pitch Deck Builder
Manages per-user interview state stored as JSON files in /tmp/

Usage (called by n8n via SSH):
  python3 state_manager.py --chat_id 12345 --action read
  python3 state_manager.py --chat_id 12345 --action write --data '{"step":1,...}'
  python3 state_manager.py --chat_id 12345 --action clear
  python3 state_manager.py --chat_id 12345 --action status
"""

import json
import sys
import os
import argparse
from datetime import datetime
from pathlib import Path

STATE_DIR = "/tmp/pitchdeck_states"
Path(STATE_DIR).mkdir(parents=True, exist_ok=True)


def state_path(chat_id: str) -> str:
    return f"{STATE_DIR}/state_{chat_id}.json"


def read_state(chat_id: str) -> dict:
    p = state_path(chat_id)
    if os.path.exists(p):
        try:
            with open(p, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def write_state(chat_id: str, data: dict) -> bool:
    try:
        with open(state_path(chat_id), "w") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"ERROR writing state: {e}", file=sys.stderr)
        return False


def clear_state(chat_id: str) -> bool:
    p = state_path(chat_id)
    if os.path.exists(p):
        os.remove(p)
    return True


def init_state(chat_id: str, company_name: str = "") -> dict:
    """Initialize a fresh interview session."""
    state = {
        "step": 1,
        "chat_id": chat_id,
        "company_name": company_name,
        "answers": {},
        "style": None,
        "ref_file": None,
        "started_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat(),
    }
    write_state(chat_id, state)
    return state


def advance_state(chat_id: str, answer: str, field: str) -> dict:
    """Record an answer and advance to the next step."""
    state = read_state(chat_id)
    if not state:
        return {}
    state["answers"][field] = answer
    state["step"] = state.get("step", 1) + 1
    state["updated_at"] = datetime.utcnow().isoformat()
    write_state(chat_id, state)
    return state


# ── Interview Questions ───────────────────────────────────────────────────────

QUESTIONS = [
    {
        "step": 1,
        "field": "company_description",
        "question": "🚀 *Question 1/8 — The Pitch*\n\nWhat does your startup do? Give me a 1-2 sentence description of the problem you solve and for whom.",
        "hint": "e.g. \"We help solo founders automate their product pipeline using AI agents, so they can ship 10x faster without a big team.\""
    },
    {
        "step": 2,
        "field": "target_customer",
        "question": "👤 *Question 2/8 — Your Customer*\n\nWho is your target customer? Be specific — who feels the pain most acutely?",
        "hint": "e.g. \"Early-stage solo founders and micro-teams (1-3 people) building SaaS products.\""
    },
    {
        "step": 3,
        "field": "market_size",
        "question": "📊 *Question 3/8 — Market Size*\n\nHow big is the market? Share your TAM/SAM estimate, or describe the market opportunity.",
        "hint": "e.g. \"The global no-code/low-code market is $45B by 2027. Our TAM is the $5B indie dev tools segment.\""
    },
    {
        "step": 4,
        "field": "differentiation",
        "question": "⚡ *Question 4/8 — Your Edge*\n\nWhat makes you different from existing solutions? Why can't customers just use [competitor]?",
        "hint": "e.g. \"Unlike Zapier, we handle full product builds autonomously. Unlike hiring devs, it costs <$50/month.\""
    },
    {
        "step": 5,
        "field": "business_model",
        "question": "💰 *Question 5/8 — Business Model*\n\nHow do you make money? Describe your pricing/revenue model.",
        "hint": "e.g. \"$49/month SaaS subscription. Enterprise plan at $299/month. 30-day free trial.\""
    },
    {
        "step": 6,
        "field": "traction",
        "question": "📈 *Question 6/8 — Traction*\n\nWhat proof do you have? Share any metrics — users, revenue, waitlist, pilot customers, or notable milestones.",
        "hint": "e.g. \"150 waitlist signups in 2 weeks. 3 paying pilot customers at $500 MRR. Featured on Product Hunt.\""
    },
    {
        "step": 7,
        "field": "team",
        "question": "👥 *Question 7/8 — The Team*\n\nWho's building this? Share founder names and key backgrounds (1-2 lines each).",
        "hint": "e.g. \"Ayush Poojary — CA background, 5 years in SaaS. Previously built 3 products with $200K+ ARR.\""
    },
    {
        "step": 8,
        "field": "ask",
        "question": "🎯 *Question 8/8 — The Ask*\n\nHow much are you raising, at what valuation (if applicable), and what will you use it for?",
        "hint": "e.g. \"Raising $500K pre-seed. Use: 40% product, 30% marketing, 20% ops, 10% reserve. Target: 18-month runway.\""
    },
]

STYLE_MENU = """✨ *Almost there! Choose your deck style:*

1️⃣ *YC Clean* — White, minimal, bold typography (YC-style)
2️⃣ *Premium Dark* — Dark background, purple accents (a16z-style)
3️⃣ *Founder Modern* — Dark navy, cyan gradient accents

Or send me a reference deck (PDF or PPTX) to clone its style.

Reply with *1*, *2*, *3*, or upload a file."""

GENERATING_MSG = "⚙️ *Generating your pitch deck...*\n\nThis takes about 30-60 seconds. I'll send the PDF when ready."

DONE_MSG = "🎉 *Your pitch deck is ready!*\n\nHere's your VC-ready PDF. Review it and let me know if you'd like any changes.\n\n_Built with Founder Systems AI_"


def get_question(step: int) -> dict | None:
    for q in QUESTIONS:
        if q["step"] == step:
            return q
    return None


def process_message(chat_id: str, text: str, file_path: str = None) -> dict:
    """
    Main state machine. Returns:
    {
      "action": "send_message" | "send_style_menu" | "generate" | "ignore",
      "message": "...",
      "generate_data": {...}  # only when action=="generate"
    }
    """
    state = read_state(chat_id)
    text = (text or "").strip()
    text_lower = text.lower()

    # ── Not in session: check for /pitchdeck trigger ──────────────────────────
    if not state:
        if text_lower.startswith("/pitchdeck") or text_lower.startswith("pitchdeck"):
            # Start new session
            parts = text.split(maxsplit=1)
            company_name = parts[1].strip() if len(parts) > 1 else ""
            state = init_state(chat_id, company_name)

            q = QUESTIONS[0]
            welcome = (
                f"👋 *Welcome to the Pitch Deck Builder!*\n\n"
                f"I'll ask you 8 quick questions to extract the soul of your pitch, "
                f"then generate a professional VC-ready PDF deck.\n\n"
                f"Ready? Let's go! 🔥\n\n"
                f"━━━━━━━━━━━━━━━━\n\n"
                f"{q['question']}\n\n"
                f"💡 _{q['hint']}_"
            )
            return {"action": "send_message", "message": welcome, "new_state": state}
        else:
            return {"action": "ignore"}

    current_step = state.get("step", 1)

    # ── Cancel command ────────────────────────────────────────────────────────
    if text_lower in ("/cancel", "cancel", "/stop", "stop"):
        clear_state(chat_id)
        return {"action": "send_message", "message": "❌ Pitch deck session cancelled. Send /pitchdeck anytime to start again."}

    # ── Style selection (step 9) ──────────────────────────────────────────────
    if current_step == 9:
        # Handle file upload for custom style
        if file_path:
            state["ref_file"] = file_path
            state["style"] = "custom"
            state["step"] = 10
            write_state(chat_id, state)
            return {
                "action": "generate",
                "message": GENERATING_MSG,
                "generate_data": state
            }

        # Parse style choice
        style_map = {
            "1": "yc", "yc": "yc", "yc clean": "yc", "clean": "yc",
            "2": "dark", "dark": "dark", "premium dark": "dark", "a16z": "dark",
            "3": "modern", "modern": "modern", "founder modern": "modern", "cyan": "modern",
        }
        chosen = style_map.get(text_lower)
        if chosen:
            state["style"] = chosen
            state["step"] = 10
            write_state(chat_id, state)
            return {
                "action": "generate",
                "message": GENERATING_MSG,
                "generate_data": state
            }
        else:
            return {
                "action": "send_message",
                "message": "Please reply with *1*, *2*, or *3* to choose a style, or upload a PDF/PPTX reference deck."
            }

    # ── Already generating (step 10) ─────────────────────────────────────────
    if current_step >= 10:
        return {
            "action": "send_message",
            "message": "⏳ Still generating your deck... please wait a moment!"
        }

    # ── Collect answer for current question ───────────────────────────────────
    q = get_question(current_step)
    if not q:
        return {"action": "ignore"}

    # Save the answer
    state["answers"][q["field"]] = text
    next_step = current_step + 1
    state["step"] = next_step
    state["updated_at"] = datetime.utcnow().isoformat()

    # Extract company name from first answer
    if current_step == 1 and not state.get("company_name"):
        words = text.split()
        state["company_name"] = words[0] if words else "YourStartup"

    write_state(chat_id, state)

    # ── Send next question or style menu ─────────────────────────────────────
    if next_step <= 8:
        next_q = get_question(next_step)
        progress = f"*[{next_step}/8 answered]*\n\n"
        msg = f"{progress}{next_q['question']}\n\n💡 _{next_q['hint']}_"
        return {"action": "send_message", "message": msg}
    else:
        # All 8 questions answered, show style menu
        state["step"] = 9
        write_state(chat_id, state)
        return {"action": "send_message", "message": STYLE_MENU}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chat_id", required=True)
    parser.add_argument("--action", choices=["read", "write", "clear", "status", "process"], required=True)
    parser.add_argument("--data", default="{}", help="JSON data for write/process actions")
    parser.add_argument("--text", default="", help="Message text for process action")
    parser.add_argument("--file", default="", help="File path for process action")
    args = parser.parse_args()

    if args.action == "read":
        print(json.dumps(read_state(args.chat_id)))
    elif args.action == "write":
        data = json.loads(args.data)
        write_state(args.chat_id, data)
        print("OK")
    elif args.action == "clear":
        clear_state(args.chat_id)
        print("OK")
    elif args.action == "status":
        state = read_state(args.chat_id)
        if state:
            print(f"Active session: step {state.get('step', '?')}/10, started {state.get('started_at', '?')}")
        else:
            print("No active session")
    elif args.action == "process":
        result = process_message(args.chat_id, args.text, args.file or None)
        print(json.dumps(result))
