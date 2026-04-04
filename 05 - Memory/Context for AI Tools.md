# ð§  Context for AI Tools

> Copy-paste this into any new AI tool (ChatGPT, Claude, BrowserOS, Arena AI etc.) to give it instant context about Founder Systems.

---

## Master Context Block

```
You are helping Ayush Poojary build "Founder Systems" â an autonomous AI product factory based in Bengaluru, India.

## What Founder Systems Is
An automated pipeline that:
1. Scrapes startup ideas from the internet (Product Hunt, HN, Indie Hackers, Reddit, GitHub Trending)
2. Ranks ideas using AI (Gemini Flash)
3. Plans products using GPT-5.3 (Azure OpenAI)
4. Builds products (static web apps, Excel templates, Chrome extensions, scripts)
5. Publishes to foundersystems.in via GitHub + Vercel CI/CD
6. Markets via auto-generated posts (Twitter, Reddit, LinkedIn)
7. Tracks performance via analytics dashboard + weekly Telegram summary

## Infrastructure (as of 2026-04-04)
- **Azure VM only** (20.193.252.82, user: ayush) â GCP VM decommissioned
- n8n URL: https://n8n.foundersystems.in (37 workflows, 32 active)
- Atlas v3 (@Blasikenbot): primary Telegram interface, 20+ tools, GPT-5.3/Grok/Llama via LiteLLM
- @Rayquabot: n8n workflow bot (Ideas â Plan â Build â Deploy pipeline)
- LLMs: Gemini Flash (ideas ranking), GPT-5.3 Azure (planning + code gen), Grok 4.1 (Atlas chat)
- Storage: Google Sheets (ideas), PostgreSQL (n8n), SQLite (analytics), Qdrant (vector memory)
- GitHub (AyushPoo) for code + Obsidian vault sync
- Vercel for website hosting (foundersystems.in)
- Gumroad + LemonSqueezy for product sales

## Key n8n Workflows
- Founder OS Agent (ID: TzpURLXbI6iOfLqU): â Active (legacy, superseded by Atlas v3)
- Ideas Fetcher (ID: pkTIpthafQ88wkAy): â Active â 9 sources, Gemini ranking
- Get Idea Details (ID: zgJBIZS3qUxEwwtd): â Active
- Save Idea (ID: rW7ohKD1BCAWUDtl): â Active
- Product Builder (ID: vo7WHaL6rq7yKRvm): â Active â GPT-5.3 planner
- Builder - Web App (ID: xiYFZhlToYLX9g4J): â Active
- Obsidian Updater (ID: Yg8BWmxKQuCHkn2k): â Active â POST /webhook/update-obsidian
- Error Handler (ID: a7qvacpHEoRt5Lu9): â Active â all 29 workflows wired to it
- Health Monitor (ID: kBwt0eAhfLBRmaN4): â Active â 5-min uptime checks

## Azure VM Structure
/home/ayush/
âââ .env                      # All secrets/API keys
âââ litellm-config.yaml       # LLM routing (Azure OpenAI, Groq, Grok)
âââ analytics/                # analytics-api (port 3001, SQLite)
âââ atlas-api/                # Atlas v3 Telegram bot (main.py, tools.py)
âââ openclaw-gateway/         # OpenClaw API gateway
âââ products/                 # Built products (index.html per product)

## PM2 Processes (Azure VM)
analytics-api (3001), atlas-api, auto-healer, founder-agent, litellm-proxy (4000), n8n (5678), openclaw-gateway

## Active Issues (as of 2026-04-04)
1. Product Builder not yet directly triggerable from Atlas/Telegram (webhook only).
2. Save Idea Google Sheets auth â verify still stable after re-auth in March 2026.
3. Port 3000 exposed on Azure â Python HTTP server, low severity, can be disabled.

## Ayush's Style
- Non-technical founder â explain things simply
- Prefers automation over manual work
- Uses Telegram (@Blasikenbot) as his primary interface
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
Pipeline: n8n Product Builder â GPT 5.3 â code â GitHub push â auto-deploy
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
Don't repeat suggestions from previous sessions â check the vault for what's been decided.
```
