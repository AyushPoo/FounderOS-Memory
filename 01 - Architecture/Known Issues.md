# Known Issues

> Last updated: 2026-04-04 by co-founder agent

## Open Issues

| # | Issue | Severity | Notes |
|---|-------|----------|-------|
| 1 | Port 3000 exposed to internet on Azure | Low | Python HTTP server scanned by bots. Not a crash risk. Products now served via Vercel â can disable port 3000. |
| 2 | Product Builder workflow not connected to Atlas | Medium | Triggered via webhook only, not from Telegram/Atlas yet. |
| 3 | Save Idea Google Sheets auth â verify still working | Low | Was broken in March 2026, re-auth done. Confirm still stable. |

## Fixed Issues

| Date | Issue | Fix |
|------|-------|-----|
| 2026-04-04 | GCP VM references throughout vault | Fixed: all docs updated, GCP VM confirmed decommissioned |
| 2026-04-03 | No error handling on n8n workflows | Fixed: Error Handler workflow wired to all 29 production workflows |
| 2026-04-03 | No n8n backup | Fixed: Daily n8n Backup workflow created (2AM IST â GitHub) |
| 2026-04-03 | No uptime monitoring | Fixed: Health Monitor workflow (5-min checks on n8n, website, analytics API) |
| 2026-04-03 | No CI/CD pipeline | Fixed: GitHub Actions deploy.yml (Vercel) + product-sync.yml (n8n webhook) |
| 2026-03-29 | founder-agent crash loop â 104 restarts | Fixed: auto-healer PM2 process added as watchdog |
| 2026-03-26 | No deployment pipeline from Azure products/ to website | Fixed: Phase 3 complete â GitHub push + Vercel CI/CD |
| 2026-03-26 | Product data hardcoded in JSX on foundersystems.in | Fixed: Phase 3B â dynamic JSON files in public/products/ |
| 2026-03-26 | No sales platform auto-listing | Fixed: Phase 3C â n8n Product Publisher syncs to Gumroad + LemonSqueezy |
| 2026-03-25 | System State Sync failing â 32+ consecutive hourly errors | Fixed: hardcoded old GCP IP updated |
| 2026-03-25 | Product Builder 100% failure rate | Fixed: continueRegularOutput on Acknowledge node |
| 2026-03-25 | Builder - Web App workflow broken | Fixed: malformed URL + wrong header name |
| 2026-03-23 | Atlas crashes on GPT-5.3 calls | Fixed: bad schema + max_tokens â max_completion_tokens |
| 2026-03-21 | GCP disk 100% full | Fixed: cleaned up duplicate skill repos (GCP decommissioned anyway) |
| 2026-03-21 | Gemini API key blocked by IP restriction | Fixed: whitelisted Azure VM IPs |

## Tech Gotchas (permanent notes)

- Gemini API key has IP restriction â must allowlist both IPv4 and IPv6 of VMs
- n8n `specifyBody: json` with expressions in `jsonBody` fails validation â use Code node to pre-serialize
- n8n `webhook-test/` URLs only work in test mode â use `webhook/` for production
- Azure VM only has 1.9GB RAM â avoid restarting multiple PM2 services simultaneously
- GPT-5.3 uses `max_completion_tokens` not `max_tokens`
- n8n POST to create workflow: do not include `active: true` â activate separately via `/activate` endpoint
- n8n PUT workflow: only send `name, nodes, connections, settings, staticData` â extra fields cause validation errors
- n8n settings: only allowed fields are `executionOrder, callerPolicy, availableInMCP, errorWorkflow, timezone, saveData*, saveManualExecutions, saveExecutionProgress, maxExecutionTime, timeout`
- GitHub API PUT: always re-fetch SHA immediately before PUT to avoid race condition errors
