# 🏠 Founder Systems — Dashboard

> **Mission:** Build an autonomous product factory that scrapes ideas, builds tools, publishes, markets, and learns — all with minimal human input.

## Quick Links
- [[Architecture Overview]] — How everything connects
- [[VM Status]] — GCP VM details
- [[Workflow Index]] — All n8n workflows
- [[Skill Registry]] — What the system can build
- [[Idea Pipeline]] — Current ideas being processed

## System Status

| Component | Status | Notes |
|-----------|--------|-------|
| n8n | ✅ Running | PM2 managed, 658MB RAM |
| Founder OS Agent | ✅ Active | Telegram bot, Gemini LLM |
| Ideas Fetcher | ✅ Active | 9 sources, auto-rank |
| Product Builder | ⚠️ Partial | Planner works, builders incomplete |
| Builder - Web App | ❌ Inactive | Broken HTTP config |
| Obsidian Memory | 🔄 Setting up | This vault |
| Antigravity | 🔌 Disconnected | Not connected to n8n yet |

## Recent Activity
```dataview
TABLE file.mtime as "Modified", file.folder as "Section"
FROM ""
WHERE file.name != "Dashboard"
SORT file.mtime DESC
LIMIT 10
```

## Open Tasks
```dataview
TASK
WHERE !completed
SORT file.mtime DESC
LIMIT 15
```
