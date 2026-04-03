# Infrastructure — Founder Systems
*Last updated: 2026-04-03 (auto-audited via n8n SSH)*

---

## Azure VM (Primary & Only Server)

| Field | Value |
|-------|-------|
| **IP** | 20.193.252.82 |
| **User** | ayush |
| **OS** | Ubuntu (Azure) |
| **Uptime** | ~1 hour at last check |
| **Load** | 2.45 / 3.58 / 3.36 |
| **Disk (/)** | ~15% used |

---

## PM2 Processes

| ID | Name | Status | Memory | Restarts | Purpose |
|----|------|--------|--------|----------|---------|
| 4 | founder-agent | ✅ online | 84 MB | 1 | Python agent, port 8085 |
| 6 | analytics-api | ✅ online | 71 MB | 1 | Node/Express REST API, port 3001 |
| 1 | atlas-api | ✅ online | 68 MB | 1 | Atlas Telegram bot backend |
| 8 | auto-healer | ✅ online | 4 MB | 0 | Watchdog/self-healing daemon |
| — | litellm-proxy | ✅ running | — | 0 | LiteLLM proxy → Azure OpenAI, port 4000 |
| — | n8n | ✅ running | — | — | Workflow engine, port 5679 (internal) |
| — | openclaw-gateway | ✅ running | — | — | Openclaw MCP gateway, ports 7890/7892 |

---

## Open Ports

| Port | Service | Notes |
|------|---------|-------|
| 22 | SSH | Azure VM access |
| 80/443 | nginx | Reverse proxy → n8n |
| 3001 | analytics-api | Node.js Express + SQLite |
| 3101 | unknown | Node process |
| 4000 | litellm-proxy | Azure OpenAI gateway (sk-openclaw-azure) |
| 5432 | postgres | Internal only (127.0.0.1) |
| 5679 | n8n | Internal only (127.0.0.1) |
| 6333 | qdrant | Vector database |
| 7890/7892 | openclaw-gateway | MCP gateway |
| 8000 | memory-api | Python memory server |
| 8085 | founder-agent | Python agent API |
| 13100 | paperclip | Internal node service |

---

## Directory Map (/home/ayush/)

```
/home/ayush/
├── analytics/          # Analytics API — Express + better-sqlite3, port 3001
├── founder-os/         # Founder OS agent + watchdog.sh
├── paperclip/          # CLI tool (TypeScript/TSX), dev-watch running
├── memory-api/         # Python memory server, port 8000
├── EverMemOS/          # Memory system (EverMem)
├── openclaw-workspace/ # Openclaw IDE workspace
├── qdrant-data/        # Qdrant vector DB data
├── products/           # Built product files (html, etc.)
├── Founder-Systems/    # Website repo clone
├── gcp-final-backup/   # Backup from old GCP VM
├── builder_agent.py    # Product builder Python agent
├── ai_fixer.py         # AI code fixer utility
├── litellm-config.yaml # LiteLLM proxy config
├── health_monitor.sh   # Health check script
├── health.log          # Health log output
└── .n8n/               # n8n config + database
```

---

## LiteLLM Proxy Config

Routes all LLM calls through a unified OpenAI-compatible endpoint:
- **Endpoint:** http://localhost:4000
- **Master key:** sk-openclaw-azure
- **Models available:**
  - `gpt-5.3` → Azure OpenAI (ayush-mmu7mtqf-eastus2.cognitiveservices.azure.com)
  - `gpt-4.1` → Azure OpenAI

---

## Cron Jobs

```cron
*/5 * * * *  /home/ayush/founder-os/agent/watchdog.sh
*/5 * * * *  /home/ayush/health_monitor.sh
```

---

## External Services

| Service | URL | Purpose |
|---------|-----|---------|
| n8n | https://n8n.foundersystems.in | Workflow automation engine |
| Website | https://foundersystems.in | Product landing page (Vercel) |
| Analytics | http://20.193.252.82:3001 | Internal sales/events tracking |
| Memory API | http://20.193.252.82:8000 | Agent memory server |
| Founder Agent | http://20.193.252.82:8085 | Core automation agent |
| Qdrant | http://20.193.252.82:6333 | Vector search DB |

---

## Telegram Bots

| Bot | Handle | Backend |
|-----|--------|---------|
| Rayquabot | @Rayquabot | n8n (Founder OS Agent workflow) |
| Blasikenbot | @Blasikenbot | Atlas API (PM2 atlas-api process) |

---

## CI/CD Pipeline

```
Code change → push to GitHub (AyushPoo/Founder-Systems)
  → GitHub Actions: deploy.yml → Vercel auto-deploy → foundersystems.in
  → GitHub Actions: product-sync.yml (if public/products/** changed) → n8n Product Publisher webhook
```

---

## Backups

- **n8n workflows:** Daily at 2 AM IST via n8n "🔒 Daily n8n Backup → GitHub" workflow
  → commits to `AyushPoo/FounderOS-Memory/backups/n8n/`
- **VM data:** gcp-final-backup/ has old GCP export
- **No GCP VM** — everything runs on Azure VM only

---

## ⚠️ Note on GCP VM

Previous docs mentioned a GCP VM (34.47.167.251). **This no longer exists.**
All services — n8n, Atlas, Analytics, Memory API, LiteLLM — run on the single Azure VM.
