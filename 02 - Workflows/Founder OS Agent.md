# 🤖 Founder OS Agent

## Overview
The main orchestrator — an AI agent triggered by Telegram messages that can fetch ideas, get details, save ideas, and manage workflows.

## Configuration
- **Workflow ID:** YSPgCuzj9JIHS7EG
- **Trigger:** Telegram messages from Ayush (chat ID: 7866603961)
- **LLM:** Google Gemini (via PaLM API)
- **Memory:** PostgreSQL Chat Memory (keyed by Telegram chat ID)
- **Telegram Bot:** Account 2 (credential: hZoZ9ZWSH2zDFlSZ)

## System Prompt (Key Rules)
1. **Fetch ideas** → always call `get_startup_ideas` tool
2. **Show ideas** → clean numbered list, name + score, under 800 chars
3. **Get details** → MUST call `get_idea_details` tool (never generate from memory)
4. **Save idea** → call Save Idea tool
5. **Response limit** → never exceed 3000 characters (Telegram limit)
6. **No empty replies** → if tool fails, say "Sorry, something went wrong"
7. **Build workflow** → conversational → summarize → confirm → build

## Connected Tools
| Tool | Workflow | Purpose |
|------|----------|---------|
| Call 'Ideas Fetcher' | pkTIpthafQ88wkAy | Scrape & rank ideas |
| Call 'Get Idea Details' | zgJBIZS3qUxEwwtd | Deep-dive on one idea |
| Call 'Save Idea' | rW7ohKD1BCAWUDtl | Bookmark to Google Sheets |
| list_workflows | HTTP GET /api/v1/workflows | Show all n8n workflows |
| delete_workflow | HTTP DELETE | Remove a workflow |
| Call n8n Workflow Tool | ⚠️ UNCONFIGURED | Dead — no workflow ID |

## Personality
- Direct and smart, not a yes-man
- Pushes back when something doesn't make sense
- Remembers context via PostgreSQL chat memory
- Takes action when asked, not just talk

## TODO
- [ ] Connect Product Builder as a tool
- [ ] Add Obsidian memory read/write tools
- [ ] Remove dead "Call n8n Workflow Tool" node
