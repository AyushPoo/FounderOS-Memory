# 📋 Decisions Log

Key architectural and product decisions. This prevents different AI tools from giving conflicting advice about things already decided.

## Format
**Date | Decision | Reason | Decided By**

---

## 2026-03-18

### Memory Layer = Obsidian + GitHub sync
- **Decision:** Use Obsidian synced to GitHub as the central memory layer
- **Reason:** Works across all AI tools, auto-syncs, can be read/written by n8n via GitHub API
- **Decided by:** Ayush

### LLM Split: Gemini for ideas, GPT 5.3 for building
- **Decision:** Keep Gemini for idea ranking/chat (cheap, fast). Use GPT 5.3 Azure for planning and code generation (more capable)
- **Reason:** Cost vs quality tradeoff
- **Decided by:** Existing setup

### Antigravity = manual IDE, not n8n node
- **Decision:** Antigravity is Ayush's IDE on his laptop. It connects to GitHub. n8n will push code to GitHub — Antigravity or Vercel will handle deployment
- **Reason:** Antigravity doesn't have an API; GitHub is the integration point
- **Decided by:** Ayush + agent (2026-03-18)

### Product Builder triggers via webhook (not Telegram directly)
- **Decision:** Product Builder is triggered by a webhook POST, not directly from Telegram
- **Reason:** Allows decoupled triggering from multiple sources
- **Decided by:** Existing setup

### n8n runs on GCP VM, not Docker
- **Decision:** n8n runs via PM2 on bare VM, not containerised
- **Reason:** How it was initially set up
- **Decided by:** Initial setup

### Product types: web_app, excel, extension, script
- **Decision:** These 4 product types are the initial classification
- **Reason:** Covers the main use cases for Founder Systems products
- **Decided by:** Existing setup (GPT 5.3 planner)

---

_New decisions will be logged here automatically or manually as the system evolves._
