# Architecture Overview

> Last updated: 2026-04-04 by co-founder agent

## Infrastructure

> â ï¸ **GCP VM NO LONGER EXISTS.** All services run on the Azure VM.

### Azure VM (20.193.252.82) â ONLY SERVER

- **OS:** Ubuntu Linux
- **Disk:** 29GB total, ~4GB used, ~25GB free
- **User:** ayush
- **RAM:** 1.9GB â avoid running heavy processes simultaneously
- **Process Manager:** PM2
- **n8n:** https://n8n.foundersystems.in (nginx reverse proxy)

### Key Paths â Azure

```
/home/ayush/
âââ .env                          # All secrets/API keys
âââ litellm-config.yaml           # LiteLLM model routing config
âââ analytics/                    # analytics-api (port 3001, SQLite)
âââ atlas-api/                    # Atlas v3 Telegram bot
â   âââ main.py
â   âââ models.py                 # Multi-model router
â   âââ tools.py                  # 20 tools (SSH, n8n, GitHub, web, etc.)
âââ openclaw-gateway/             # OpenClaw API gateway
âââ products/
    âââ pomodoro-timer/           # index.html â SHIPPED
    âââ startup-cost-calculator/  # index.html â SHIPPED
```

### External Services

| Service | Purpose | Status |
|---------|---------|--------|
| Azure OpenAI GPT-5.3 | Planning + code gen (via LiteLLM port 4000) | â Active |
| Azure OpenAI Grok 4.1 Fast | Default Atlas chat model | â Active |
| Google Gemini 2.5 Flash | Ideas ranking, summarization | â Active |
| Groq Llama 3.3 70B | Fallback model | â Active |
| Qdrant (port 6333) | Vector DB for Atlas memory | â Active |
| PostgreSQL | n8n database backend | â Active |
| Telegram (@Blasikenbot) | Atlas v3 â primary interface | â Active |
| Telegram (@Rayquabot) | n8n workflow bot | â Active |
| Google Sheets | Ideas storage | â Active |
| Gumroad + LemonSqueezy | Product sales platforms | â Active |
| Vercel | Website hosting (foundersystems.in) | â Active |
| GitHub (AyushPoo) | Code + Obsidian vault sync | â Active |

### PM2 Processes

| Name | Port | Purpose |
|------|------|---------|
| analytics-api | 3001 | Sales/analytics REST API |
| atlas-api | â | Atlas v3 (@Blasikenbot) |
| auto-healer | â | PM2 watchdog (restarts crashed processes) |
| founder-agent | â | Core pipeline orchestrator |
| litellm-proxy | 4000 | LLM router â Azure OpenAI |
| n8n | 5678 | Workflow automation |
| openclaw-gateway | â | OpenClaw API gateway |

## Data Flow

```
Telegram (Ayush)
      â
      â¼
  @Blasikenbot â Atlas v3 (Azure VM)
  - GPT-5.3 / Grok / Llama via LiteLLM
  - 20+ tools
      â
      ââââº ssh_azure        â VM commands
      ââââº n8n_*            â Workflow control
      ââââº mem0_search/store â Qdrant memory (port 6333)
      ââââº obsidian_write   â GitHub vault (via n8n webhook)
      ââââº web_search/fetch â Internet

  @Rayquabot â n8n (37 workflows, Azure VM)
      â
      ââââº Ideas Fetcher    â Google Sheets
      ââââº Product Builder  â GPT-5.3 plans â GitHub â Vercel
      ââââº Obsidian Updater â GitHub vault
      ââââº Health Monitor   â 5-min uptime checks
      ââââº Daily Backup     â n8n workflows â GitHub
      ââââº Error Handler    â Telegram alerts on failures

  Products Pipeline:
  Build â Azure /products/ â GitHub (AyushPoo/Founder-Systems) â Vercel â foundersystems.in
```

## Deployment Pipeline

```
Product files (Azure VM /products/<name>/)
  â
  âââº deploy.sh â git push â AyushPoo/Founder-Systems
                                    â
                                    âââº GitHub Actions (deploy.yml)
                                    â       âââº Vercel deploy â foundersystems.in
                                    â
                                    âââº GitHub Actions (product-sync.yml)
                                            âââº n8n webhook â Gumroad + LemonSqueezy sync
```

## Related

- [[VM Status]]
- [[n8n-Workflows]]
- [[Infrastructure]]
- [[Workflow Index]]
