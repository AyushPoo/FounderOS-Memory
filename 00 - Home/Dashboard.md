# ð  Founder Systems â Dashboard

> **Mission:** Build an autonomous product factory that scrapes ideas, builds tools, publishes, markets, and learns â all with minimal human input.

## Quick Links
- [[Architecture Overview]] â How everything connects
- [[VM Status]] â Azure VM details
- [[Workflow Index]] â All n8n workflows
- [[Production Roadmap]] â Phase status and next steps
- [[Idea Pipeline]] â Current ideas being processed

## System Status

| Component | Status | Notes |
|-----------|--------|-------|
| n8n | â Running | https://n8n.foundersystems.in â 37 workflows, 32 active |
| Atlas v3 (@Blasikenbot) | â Active | Primary interface â GPT-5.3/Grok/Llama, 20+ tools |
| Ideas Fetcher | â Active | 9 sources, Gemini ranking |
| Product Builder | â Active | GPT-5.3 planner, web app builder live |
| Website | â Live | foundersystems.in â Vercel, auto-deploys on push |
| Marketing | â Active | 3 workflows: Twitter, Reddit, LinkedIn |
| Analytics | â Live | analytics.foundersystems.in â weekly Telegram summary |
| Error Handler | â Active | All 29 workflows â Telegram alerts |
| Health Monitor | â Active | 5-min uptime checks on n8n + website + analytics |
| GCP VM | â Decommissioned | All services on Azure VM (20.193.252.82) |

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
