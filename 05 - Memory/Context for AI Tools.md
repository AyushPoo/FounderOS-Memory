# 🧠 Context for AI Tools

> Copy-paste this into any new AI tool (ChatGPT, Claude, BrowserOS, Arena AI etc.) to give it instant context about Founder Systems.

---

## Master Context Block

```
You are helping Ayush Poojary build "Founder Systems" — an autonomous AI product factory based in Bengaluru, India.

## What Founder Systems Is
An automated pipeline that:
1. Scrapes startup ideas from the internet (Product Hunt, HN, Indie Hackers, Reddit, GitHub Trending)
2. Ranks ideas using AI (Gemini)
3. Plans products using GPT 5.3 (Azure OpenAI)
4. Builds products (Next.js web apps, Excel templates, extensions, scripts)
5. Publishes to website via GitHub + Antigravity IDE
6. (Future) Markets and analyzes performance

## Infrastructure
- GCP VM at 34.14.219.64, running n8n via PM2
- n8n URL: https://34.14.219.64.nip.io
- LLMs: Google Gemini (ideas), GPT 5.3 Azure (planning + code gen)
- Telegram bot as main control interface
- Google Sheets as ideas storage
- PostgreSQL for chat memory
- GitHub (AyushPoo account) for code
- Antigravity IDE for website deployment (local, not connected to n8n yet)
- Obsidian vault (this) as central memory layer

## Key n8n Workflows
- Founder OS Agent (YSPgCuzj9JIHS7EG) — Telegram AI assistant
- Ideas Fetcher (pkTIpthafQ88wkAy) — scrapes + ranks ideas
- Get Idea Details (zgJBIZS3qUxEwwtd) — deep dive on one idea
- Save Idea (rW7ohKD1BCAWUDtl) — bookmark to Google Sheets
- Product Builder (vo7WHaL6rq7yKRvm) — skills + GPT 5.3 planner
- Builder - Web App (xiYFZhlToYLX9g4J) — generates Next.js code (INACTIVE/BROKEN)

## VM Structure
/home/ayushpoojary1/
├── .n8n/                     # n8n SQLite DB
├── founder-os/
│   ├── skill-repos/          # Cloned GitHub repos
│   ├── skills/               # 108 skill folders from everything-claude-code
│   └── context/
│       └── skill-registry.json  # Maps product types to skills

## Active Issues
1. VM disk 100% full — needs cleanup
2. Product Builder not connected to Telegram agent
3. Builder - Web App has broken config + is inactive
4. If node in Product Builder uses wrong AND logic (should be Switch)
5. No deployment pipeline from code generation to live website
6. Antigravity not connected to n8n

## Ayush's Style
- Non-technical founder — explain things simply
- Prefers automation over manual work
- Uses Telegram as his main interface
- Wants the system to learn and improve over time
- Building Founder Systems as the product (tools/templates for founders)
```

---

## Tool-Specific Contexts

### For Antigravity (Google IDE)
```
Project: Founder Systems website
GitHub: AyushPoo/Founder-Systems
Stack: (check current repo for tech stack)
Goal: A marketplace for founder tools and templates, each product built by the AI pipeline
Pipeline: n8n Product Builder → GPT 5.3 → code → GitHub push → auto-deploy
```

### For n8n AI Agent System Prompt Addition
```
Additional context: You have access to an Obsidian memory vault at GitHub repo AyushPoo/FounderOS-Memory. 
This vault tracks all ideas, builds, learnings, and system state. 
When something significant happens (idea saved, product built, error encountered), 
you should update the vault via the update-obsidian webhook.
```

### For ChatGPT / Claude Sessions
```
Working on: Founder Systems autonomous product factory
Current focus: [fill in current task]
Last session: [fill in what was last worked on]
Relevant files: See Obsidian vault AyushPoo/FounderOS-Memory on GitHub
Don't repeat suggestions from previous sessions — check the vault for what's been decided.
```
