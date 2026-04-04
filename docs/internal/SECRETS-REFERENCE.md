# Secrets Reference â Founder Systems

> â ï¸ This file documents WHERE secrets are stored, NOT their values.
> Never commit actual keys to GitHub. Values live on VMs only.

---

## ~~GCP VM~~ â DECOMMISSIONED (2026-04-04)

> â ï¸ GCP VM (34.47.167.251) no longer exists. All services have been moved to the Azure VM.
> The secrets listed below were migrated to `/home/ayush/.env` on the Azure VM.

---

## Azure VM (20.193.252.82 Â· user: ayush)

### Analytics API
**Secrets file:** `/home/ayush/analytics/.env.production`
**Permissions:** `600`
**Loaded by:** PM2 analytics-api process

| Secret | Variable Name | Used In |
|--------|--------------|---------|
| Internal API Key | `INTERNAL_API_KEY` | analytics server auth |
| DB Path | `DB_PATH` | SQLite database path |
| Gumroad API Key | `GUMROAD_API_KEY` | sales sync |
| LemonSqueezy API Key | `LEMONQUEEZY_API_KEY` | sales sync |
| Telegram Bot Token | `TELEGRAM_BOT_TOKEN` | alerts |
| Telegram Chat ID | `TELEGRAM_CHAT_ID` | alerts |

### Atlas Agent (@Blasikenbot)
**Secrets file:** `/home/ayush/atlas/.env.production`
**Permissions:** `600`
**Loaded by:** Atlas v3 Python agent startup

| Secret | Variable Name | Used In |
|--------|--------------|---------|
| Groq API Key | `GROQ_API_KEY` | Atlas: Llama 3.3 70B fallback |
| Grok API Key | `GROK_API_KEY` | Atlas: Grok 4.1 Fast (primary) |
| Telegram Bot Token | `TELEGRAM_BOT_TOKEN` | Atlas: @Blasikenbot |
| Telegram Chat ID | `TELEGRAM_CHAT_ID` | Atlas: user DMs |
| Memory API Key | `MEMORY_API_KEY` | Atlas: memory-server auth |
| Memory Server URL | `MEMORY_SERVER_URL` | Atlas: GCP memory-server |

---

## GitHub Repos

### AyushPoo/Founder-Systems (website)
- No secrets stored in repo
- Vercel env vars set in Vercel dashboard (not in code)
- `.gitignore` includes: `.env`, `.env.production`, `*.env`

### AyushPoo/FounderOS-Memory (vault)
- No secrets stored
- `docs/internal/SECRETS-AUDIT.md` is gitignored
- This file (`SECRETS-REFERENCE.md`) is safe to commit (no values)

---

## Rotation Policy

| Key Type | Rotate Every | Last Rotated |
|----------|-------------|--------------|
| Telegram Bot Tokens | On compromise only | 2026-03-22 |
| LLM API Keys | 90 days | 2026-03-22 |
| GitHub PAT | 90 days | 2026-03-22 |
| Platform API Keys (Gumroad, LS) | 180 days | 2026-03-22 |

---

*Last updated: 2026-04-03*
*If you find a hardcoded key anywhere, move it to the .env.production file immediately.*
