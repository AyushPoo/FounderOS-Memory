# VM Status

> Last updated: 2026-04-04 by co-founder agent

> â ï¸ **GCP VM (34.14.219.64 / 34.47.167.251) NO LONGER EXISTS.** Azure VM is the only server.

## Azure VM â 20.193.252.82 (ONLY SERVER)

| Field | Value |
|-------|-------|
| Status | â Online |
| OS | Ubuntu Linux |
| User | ayush |
| IP | 20.193.252.82 |
| Disk | 29GB total / ~4GB used / ~25GB free |
| RAM | 1.9GB (avoid heavy concurrent processes) |
| n8n | â https://n8n.foundersystems.in |

## PM2 Processes

| Name | Status | Port | Purpose |
|------|--------|------|---------|
| analytics-api | â Online | 3001 | Sales/analytics REST API (SQLite) |
| atlas-api | â Online | â | Atlas v3 Telegram bot (@Blasikenbot) |
| auto-healer | â Online | â | Watchdog: auto-restarts crashed PM2 processes |
| founder-agent | â Online | â | Core pipeline orchestrator |
| litellm-proxy | â Online | 4000 | LLM router â Azure OpenAI gpt-5.3 |
| n8n | â Online | 5678 | Workflow automation (proxied via nginx) |
| openclaw-gateway | â Online | â | OpenClaw API gateway |

## Port Map

| Port | Service |
|------|---------|
| 3001 | analytics-api |
| 4000 | litellm-proxy |
| 5678 | n8n (internal, proxied by nginx) |
| 6333 | Qdrant vector DB |
| 80/443 | nginx â n8n.foundersystems.in |

## Key Directories

```
/home/ayush/
âââ .env                      # All secrets/API keys
âââ litellm-config.yaml       # LiteLLM routing config
âââ analytics/                # analytics-api source
âââ atlas-api/                # Atlas v3 Python agent
âââ openclaw-gateway/         # OpenClaw gateway
âââ products/                 # Built products
    âââ pomodoro-timer/       # index.html â SHIPPED
    âââ startup-cost-calculator/ # index.html â SHIPPED
```

## Products Shipped

| Product | Path | Status |
|---------|------|--------|
| Pomodoro Timer | products/pomodoro-timer/index.html | â Live on foundersystems.in |
| Startup Cost Calculator | products/startup-cost-calculator/index.html | â Live on foundersystems.in |

## History

| Date | Event |
|------|-------|
| 2026-03-22 | Atlas v3 built on Azure â multi-model, SSH tools, 20 capabilities |
| 2026-03-23 | Fixed Atlas crash bugs (bad tool schema + wrong max_tokens param) |
| 2026-03-29 | auto-healer process added â watchdog for all PM2 services |
| 2026-04-03 | Phase 6 complete â error handler, daily backup, health monitor all live |
| 2026-04-04 | GCP VM confirmed decommissioned â Azure is only server |
