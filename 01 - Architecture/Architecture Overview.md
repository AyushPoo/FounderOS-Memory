# Architecture Overview

> Last updated: 2026-03-23 by co-founder agent

## Infrastructure

### GCP VM (34.14.219.64)
- **OS:** Debian Linux
- **Disk:** 30GB total, 22GB used, 6.3GB free (78%)
- **User:** ayushpoojary1
- **Process Manager:** PM2
- **n8n:** Running at https://34.14.219.64.nip.io (uptime: stable, 2 restarts total)
- **Node.js:** v22.22.1

### Azure VM (20.193.252.82)
- **OS:** Ubuntu Linux
- **Disk:** 29GB total, 4GB used, 25GB free (15%) — plenty of headroom
- **User:** ayush
- **RAM:** 1.9GB — avoid running heavy processes simultaneously
- **Process Manager:** PM2

### Key Paths — GCP
```
/home/ayushpoojary1/
├── .n8n/                         # n8n data
└── founder-os/
    ├── builder/                  # 8.6MB — build orchestration
    ├── context/                  # 8KB — skill registry
    ├── knowledge/                # 20KB
    ├── skill-repos/              # 42MB — cloned skill repos
    └── skills/                   # 484MB — 108 skill folders
```

### Key Paths — Azure
```
/home/ayush/
├── .env                          # All secrets/API keys
├── founder-os/
│   ├── agent/                    # Atlas v3 Telegram bot
│   │   ├── main.py
│   │   ├── models.py             # Multi-model router (GPT-5.3, Grok, Llama)
│   │   ├── tools.py              # 20 tools (SSH, Mem0, n8n, GitHub, web, etc.)
│   │   ├── state/                # agent_state.json, conversations.json
│   │   └── venv/
│   └── builder/                  # Build session context
│       ├── PRIMER.md             # Current build state
│       ├── HINDSIGHT.md          # Lessons learned
│       ├── CLAUDE.md             # Claude-specific instructions
│       └── FounderOS-Memory/     # Vault mirror
└── products/
    ├── pomodoro-timer/           # index.html — SHIPPED
    ├── startup-cost-calculator/  # index.html — SHIPPED
    └── serve.py                  # Static file server (port 3000)
```

### External Services
| Service | Purpose | Status |
|---------|---------|--------|
| Google Gemini 2.5 Flash | Ideas/chat LLM | Active (IP restriction: allow VM IPs) |
| Azure OpenAI GPT-5.3 | Planning + code gen | Active (deployment: gpt-5.3-chat) |
| Azure OpenAI Grok 4.1 Fast | Default chat model | Active |
| Groq Llama 3.3 70B | Fallback model | Active |
| OpenCode (free tier) | Code generation in builder | Active |
| Telegram Bot (Atlas) | Main Founder OS interface | Active |
| Telegram Bot 2 | n8n workflow bot | Active |
| Google Sheets | Ideas storage | Active |
| PostgreSQL | Chat memory (legacy) | Active |
| Qdrant + Mem0 | Vector memory | Active (GCP port 8000) |
| GitHub (AyushPoo) | Code + Obsidian sync | Active |

### PM2 Processes
**GCP:**
| Name | Status | Restarts | Notes |
|------|--------|----------|-------|
| n8n (id:0) | online | 2 | Stable |
| memory-server (id:5) | online | 62 | Needs investigation |
| custom-memory (id:9) | online | 0 | Stable |

**Azure:**
| Name | Status | Restarts | Notes |
|------|--------|----------|-------|
| founder-agent (id:0) | online | 51 | Fixed 2026-03-23 — was crashing due to bad tool schema + wrong max_tokens param |

## Data Flow
```
Telegram (Ayush)
      |
      v
  Atlas v3 (Azure)
  - GPT-5.3 / Grok / Llama
  - 20 tools
      |
      +---> ssh_gcp / ssh_azure  -->  VM commands
      +---> n8n_*               -->  Workflow control
      +---> mem0_search/store   -->  Qdrant memory (GCP:8000)
      +---> obsidian_write      -->  GitHub vault (via n8n webhook)
      +---> web_search/fetch    -->  Internet
      |
      v
  n8n (GCP) — 13 workflows
      |
      +---> Ideas Fetcher       -->  Google Sheets
      +---> Product Builder     -->  GPT-5.3 plans
      +---> Obsidian Updater    -->  GitHub vault
      +---> System State Sync   -->  Hourly vault refresh
```

## Known Issues (as of 2026-03-23)
| # | Issue | Status |
|---|-------|--------|
| 1 | Atlas crashes on GPT-5.3 calls | FIXED — bad schema + max_tokens param |
| 2 | memory-server 62 restarts | Open — needs log investigation |
| 3 | Builder - Web App workflow | Inactive — builds done via OpenCode directly |
| 4 | Product data hardcoded in JSX on foundersystems.in | Open — no CMS yet |
| 5 | Port 3000 exposed to internet (bots scanning) | Low priority |

## Related
- [[VM Status]]
- [[Workflow Index]]
- [[Skill Registry]]
