# 🏗️ Architecture Overview

## Infrastructure

### GCP VM (34.14.219.64)
- **OS:** Debian Linux
- **Disk:** 10GB (⚠️ 100% full — needs cleanup)
- **User:** ayushpoojary1
- **Process Manager:** PM2
- **n8n:** Running at https://34.14.219.64.nip.io
- **Database:** SQLite (n8n internal) + PostgreSQL (chat memory)
- **SSH:** Password auth (credential ID: pr7nIWz5tdv5ctrk)

### Key Paths on VM
```
/home/ayushpoojary1/
├── .n8n/                         # n8n data (68MB SQLite)
├── founder-os/
│   ├── skill-repos/              # Cloned GitHub repos with skills
│   │   └── everything-claude-code/
│   ├── skills/                   # Working skills directory  
│   │   ├── everything-claude-code/
│   │   │   └── skills/           # 108 skill folders
│   │   └── cline/                # Cline AI rules
│   └── context/
│       └── skill-registry.json   # Maps product types → skills
└── founder-os-skills/            # ⚠️ Duplicate (wastes disk)
    └── everything-claude-code/   # Same repo, third copy
```

### External Services
| Service | Purpose | Credential |
|---------|---------|-----------|
| Google Gemini | LLM for ideas/chat | PaLM API (ZjzL0eOMlw6PIBMl) |
| Azure OpenAI GPT 5.3 | Product planning & code gen | API key in workflow |
| Telegram Bot 2 | Main Founder OS interface | hZoZ9ZWSH2zDFlSZ |
| Telegram Bot 3 | Workflow activation bot | pRnfD9U062jKCLks |
| Google Sheets | Ideas storage | OAuth2 (6HZp5UHiQlcI4HW0) |
| PostgreSQL | Chat memory | SL4hyuxdPXs7IrMt |
| GitHub | Code + Obsidian sync | AyushPoo account |
| Antigravity | IDE on laptop, pushes to website | Local, not connected to n8n |

### Data Flow
```
                    ┌─────────────┐
                    │  Telegram   │
                    │  (Ayush)    │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ Founder OS  │
                    │   Agent     │◄──── Postgres Chat Memory
                    │  (Gemini)   │
                    └──────┬──────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
     ┌──────▼──────┐┌─────▼─────┐┌──────▼──────┐
     │   Ideas     ││  Get Idea ││  Save Idea  │
     │  Fetcher    ││  Details  ││ (to Sheets) │
     │ (9 sources) ││ (Gemini)  ││             │
     └──────┬──────┘└───────────┘└─────────────┘
            │
     ┌──────▼──────┐
     │Google Sheets │
     │"Founder      │
     │ Systems      │
     │ Ideas"       │
     └──────────────┘

     ┌──────────────┐   (NOT YET CONNECTED to Agent)
     │   Product    │
     │   Builder    │
     │  (Webhook)   │
     └──────┬──────┘
            │
     ┌──────▼──────┐
     │  SSH → VM   │
     │ Find Skills │
     └──────┬──────┘
            │
     ┌──────▼──────┐
     │  Planner    │
     │ (GPT 5.3)  │
     └──────┬──────┘
            │
     ┌──────▼──────┐
     │  If: type?  │
     ├─ web_app ──→ Builder - Web App (❌ broken)
     ├─ excel ────→ ❌ not built
     ├─ extension → ❌ not built
     └─ script ──→ ❌ not built
```

## Known Issues
> See [[Known Issues]] for full list with status tracking.

## Related
- [[Workflow Index]]
- [[VM Status]]
- [[Skill Registry]]
