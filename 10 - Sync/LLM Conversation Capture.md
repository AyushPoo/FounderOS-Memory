# 🤖 LLM Conversations → Obsidian

How to capture key decisions, builds, and context from AI tool sessions into the vault.

---

## The Problem
You work across ChatGPT, Claude, BrowserOS, Arena AI, and OpenClaw. Each has its own memory. Without capture, important decisions get lost between sessions.

## The Solution
Two layers:
1. **Quick capture** — log the key points while still in the session (30 seconds)
2. **Auto-capture** — OpenClaw logs its own sessions automatically

---

## Method 1: OpenClaw Auto-Capture (Already Working)

OpenClaw (this tool) logs to the vault automatically. After significant sessions, it updates:
- `05 - Memory/Conversations/Conversation Log.md` — session summaries
- `05 - Memory/Decisions/Decisions Log.md` — key decisions made
- Relevant files if something was built

**You don't need to do anything for OpenClaw sessions.**

---

## Method 2: Quick Capture via Telegram

At the end of any ChatGPT / Arena / BrowserOS session, send to your Telegram bot:

```
/log-session
Tool: ChatGPT
Topic: Product Builder fix
What was built: Updated the If node to Switch logic
Decisions: Use Switch node, not If+AND
Open items: Still need to connect to Telegram agent
```

The Founder OS Agent will forward this to the n8n `update-obsidian` webhook and log it to `05 - Memory/Conversations/Conversation Log.md`.

> **Note:** Requires adding a `/log-session` command handler to Founder OS Agent (see setup below).

---

## Method 3: Quick Capture via OpenClaw

Just tell me what happened in another tool session. Say something like:

> "Log this session: I was in ChatGPT, we fixed the Product Builder's If node, decided to use Switch instead of AND logic. Still need to connect it to Telegram."

I'll format it and push it to the vault immediately.

**This works right now — no setup needed.**

---

## Method 4: Paste the Context Block

At the start of any new AI session, paste the master context block from `05 - Memory/Context for AI Tools.md`.
At the end of the session, tell me a quick summary and I'll log it.

---

## Adding /log-session to Telegram Bot (Optional Enhancement)

To enable Telegram capture without going through OpenClaw:

In the **Founder OS Agent** n8n workflow, add a branch:

```
Trigger: message starts with "/log-session"
Action: Parse message body → POST to update-obsidian webhook
  file: "05 - Memory/Conversations/Conversation Log.md"
  action: "append"
  section: "## Sessions"
  content: [formatted log entry]
```

---

## Where Captures Go

| What | File |
|------|------|
| Session summaries | `05 - Memory/Conversations/Conversation Log.md` |
| Key decisions | `05 - Memory/Decisions/Decisions Log.md` |
| Things built | Relevant file in `02 - Workflows/` or `03 - Products/` |
| Open issues | `01 - Architecture/Known Issues.md` |

---

## Status
- [x] Method 3 (OpenClaw capture) — works now
- [x] Method 1 (OpenClaw auto-log) — works now
- [ ] Method 2 (/log-session Telegram command) — needs n8n workflow edit
- [x] Context block for pasting into new sessions — in `05 - Memory/Context for AI Tools.md`
