# VM Status

> Last updated: 2026-03-23 by co-founder agent

## GCP VM — 34.14.219.64

| Field | Value |
|-------|-------|
| Status | Online |
| OS | Debian Linux |
| Disk | 30GB / 22GB used / 6.3GB free (78%) |
| Node.js | v22.22.1 |
| n8n | Running — https://34.14.219.64.nip.io |
| n8n uptime | 21h+ (2 total restarts — stable) |
| memory-server | Running (port 8000) — 62 restarts (investigate) |
| custom-memory | Running — stable (0 restarts) |

### Disk Breakdown
```
founder-os/skills/      484MB   (108 skill folders)
founder-os/skill-repos/  42MB   (cloned repos)
founder-os/builder/      8.6MB
founder-os/knowledge/    20KB
founder-os/context/      8KB
.n8n/                   (SQLite DB + executions)
```

## Azure VM — 20.193.252.82

| Field | Value |
|-------|-------|
| Status | Online |
| OS | Ubuntu Linux |
| Disk | 29GB / 4GB used / 25GB free (15%) |
| RAM | 1.9GB (be careful with concurrent processes) |
| Atlas v3 | Running — 51 restarts (bugs fixed 2026-03-23) |
| HTTP server | python3 -m http.server 3000 (serves products/) |

### Products Shipped
| Product | Path | Status |
|---------|------|--------|
| Pomodoro Timer | products/pomodoro-timer/index.html | Shipped |
| Startup Cost Calculator | products/startup-cost-calculator/index.html | Shipped |

## History
- 2026-03-19: GCP disk was 100% full — cleaned up
- 2026-03-21: Mem0 v4 deployed with API key auth
- 2026-03-22: Atlas v3 built on Azure — multi-model, SSH tools, 20 capabilities
- 2026-03-23: Fixed Atlas crash bugs (bad tool schema + max_tokens param)
