# Secrets Reference — Founder Systems

> ⚠️ This file documents WHERE secrets are stored, NOT their values.
> Never commit actual keys to GitHub. Values live on VMs only.

---

## GCP VM (34.47.167.251 · user: ayushpoojary1)

**Primary secrets file:** `/home/ayushpoojary1/.env.production`
**Permissions:** `600` (owner read-write only)
**Loaded by:** PM2 via `ecosystem.config.js` → `require('dotenv').config(...)`

| Secret | Variable Name | Used In |
|--------|--------------|---------|
| Gemini API Key | `GEMINI_API_KEY` | n8n: Ideas Fetcher, ranking |
| Groq API Key | `GROQ_API_KEY` | n8n: fallback LLM |
| OpenAI API Key | `OPENAI_API_KEY` | n8n: Product Builder (GPT 5.3 Azure) |
| Gumroad API Key | `GUMROAD_API_KEY` | n8n: Product Publisher |
| Gumroad Access Token | `GUMROAD_ACCESS_TOKEN` | n8n: Product Publisher |
| LemonSqueezy API Key | `LEMONQUEEZY_API_KEY` | n8n: Product Publisher |
| Twitter API Key | `TWITTER_API_KEY` | n8n: social posting |
| GitHub Token | `GITHUB_TOKEN` | n8n: Obsidian Updater, deployer |
| Telegram Bot Token | `TELEGRAM_BOT_TOKEN` | n8n: all alert workflows (@Rayquabot) |
| Telegram Chat ID | `TELEGRAM_CHAT_ID` | n8n: all alert workflows |
| n8n Encryption Key | `N8N_ENCRYPTION_KEY` | n8n: credential encryption |

---

## Azure VM (20.193.252.82 · user: ayush)

### Analytics API
**Secrets file:** `/home/ayush/analytics/.env.production`  
**Permissions:** `600`

| Secret | Variable Name | Used In |
|--------|--------------|---------|
| Internal API Key | `INTERNAL_API_KEY` | analytics server auth |
| Gumroad API Key | `GUMROAD_API_KEY` | sales sync |
| LemonSqueezy API Key | `LEMONQUEEZY_API_KEY` | sales sync |
| Telegram Bot Token | `TELEGRAM_BOT_TOKEN` | alerts |

### Atlas Agent (@Blasikenbot)
**Secrets file:** `/home/ayush/atlas/.env.production`  
**Permissions:** `600`

| Secret | Variable Name | Used In |
|--------|--------------|---------|
| Grok API Key | `GROK_API_KEY` | Atlas: Grok 4.1 Fast (primary) |
| Groq API Key | `GROQ_API_KEY` | Atlas: Llama 3.3 70B fallback |
| Telegram Bot Token | `TELEGRAM_BOT_TOKEN` | Atlas: @Blasikenbot |
| Memory API Key | `MEMORY_API_KEY` | Atlas: memory-server auth |

---

## GitHub Repos

- **AyushPoo/Founder-Systems** — no secrets in repo; Vercel env vars in dashboard
- **AyushPoo/FounderOS-Memory** — no secrets; this file is safe to commit

---

*Last updated: 2026-04-03 — Phase 6B*
