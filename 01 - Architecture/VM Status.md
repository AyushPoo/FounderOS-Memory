# VM Status

> Last updated: 2026-03-21 (auto-sync)

## GCP VM — n8n Brain
- **IP:** 34.14.219.64
- **OS:** Debian Linux
- **Disk:** 30GB total, 22GB used, 6.2GB free (78%)
- **User:** ayushpoojary1
- **Process Manager:** PM2

### Running Processes
| Name | Status | Uptime | Restarts | Memory |
|------|--------|--------|----------|--------|
| n8n | ✅ online | 42h+ | 1 | ~660MB |
| memory-server | ✅ online | 22h+ | 62 | 35MB |
| custom-memory | ✅ online | 4h+ | 0 | 402MB |

### n8n
- **Version:** 2.10.4
- **URL:** https://34.14.219.64.nip.io
- **DB:** SQLite (internal)

### Mem0 / Custom Memory
- **Port:** 8000
- **Auth:** X-API-Key header required
- **Health endpoint:** GET /health (requires API key)
- **Agent endpoint:** POST /agent
- **Upsert endpoint:** POST /upsert

### File Structure
```
/home/ayushpoojary1/
├── .n8n/                    # n8n SQLite DB
├── .env                     # All env vars (API keys)
├── founder-os/
│   ├── builder/             # 8.6MB — builder agent files
│   ├── context/             # 8KB — skill-registry.json
│   ├── knowledge/           # 20KB
│   ├── skill-repos/         # 42MB — cloned repos
│   └── skills/              # 484MB — 108 skill folders
└── founder-os-skills/       # 42MB — DUPLICATE (safe to delete)
```

## Azure VM — fs-builder
- **IP:** 20.193.252.82
- **OS:** Ubuntu 24.04
- **Size:** Standard B2as v2 (2 vCPUs, 8GB RAM)
- **Disk:** 29GB total, 3.6GB used, 25GB free (13%)
- **User:** ayush
- **Location:** Central India (Zone 3)
- **Created:** 2026-03-21
- **Status:** ✅ Running

### Running Processes
- PM2: installed but no processes running
- Node: v22.22.1
- npm: 10.9.4

### File Structure
```
/home/ayush/
└── founder-os/
    └── builder/
        ├── CLAUDE.md          # Builder agent instructions
        ├── HINDSIGHT.md       # Lessons learned
        ├── PRIMER.md          # Session state
        ├── .opencode.json     # OpenCode config (mimo-v2-pro-free)
        ├── FounderOS-Memory/  # Obsidian vault clone
        ├── docs -> FounderOS-Memory (symlink)
        └── memory.sh
```

### Builder Agent Stack
- **IDE:** OpenCode (free tier)
- **Default model:** opencode/mimo-v2-pro-free
- **Fallback models:** mimo-v2-omni-free → minimax-m2.5-free → nemotron-3-super → gpt-5-nano
- **Stack:** React + Vite + Tailwind (TypeScript preferred)
