# Known Issues
> Last updated: 2026-03-29 by co-founder agent

## Current Status (as of 2026-03-29)

### Azure VM (20.193.252.82)
- `founder-agent`: **errored** with 104 restarts. This is a critical issue impacting the Atlas v3 Telegram bot.
- `atlas-api` and `litellm-proxy`: online.

### GCP VM (34.47.167.251)
- `custom-memory`: online, but with 312 restarts (high frequency). This suggests instability.
- `memory-server`: online, but with 1900 restarts (extremely high frequency). This is a critical issue for our Qdrant/Mem0 server.
- `analytics-api`, `azure-proxy`, and `n8n`: online.

### n8n Workflows
- `Save Idea` (rW7ohKD1BCAWUDtl): ⚠️ Google Sheets auth broken. (Confirmed)
- `Builder - Web App` (xiYFZhlToYLX9g4J): ❌ Broken/Inactive. (Confirmed)

## Open Issues

| # | Issue | Severity | Notes |
|---|-------|----------|-------|
| 1 | `founder-agent` (Azure) errored, 104 restarts | High | Critical issue. Atlas v3 Telegram bot is unstable. Needs urgent investigation. |
| 2 | `custom-memory` (GCP) frequent restarts | High | Significant instability. Needs log investigation. |
| 3 | `memory-server` (GCP) extremely frequent restarts | Critical | Qdrant/Mem0 server is highly unstable with 1900 restarts. Needs urgent log investigation. |
| 4 | Product data hardcoded in JSX on foundersystems.in | Medium | No CMS. Every new product requires a code deploy. |
| 5 | Port 3000 exposed to internet on Azure | Low | Python HTTP server scanned by bots. Not a crash risk. |
| 6 | Product Builder workflow not connected to Atlas | Medium | Triggered via webhook only, not from Telegram/Atlas yet. |
| 7 | No deployment pipeline from Azure products/ to live website | High | Products built but served on raw port — not on foundersystems.in |
| 8 | Google Sheets OAuth expired (`Save Idea` workflow) | Medium | Workflow fails with EAUTH — needs re-auth in n8n credentials. |
| 9 | `Builder - Web App` n8n workflow broken/inactive | High | Core product building workflow is not functional. |

## Fixed Issues

| Date | Issue | Fix |
|------|-------|-----|\
| 2026-03-25 | System State Sync failing — 32+ consecutive hourly errors | Fixed: hardcoded old GCP IP (34.14.219.64) updated to current IP (34.47.167.251) in all HTTP nodes |
| 2026-03-25 | Product Builder 100% failure — Acknowledge Button Press killing workflow | Fixed: set continueRegularOutput on Acknowledge node so stale Telegram callbacks don\'t abort the build |
| 2026-03-25 | Product Builder Log nodes hitting dead GCP IP | Fixed: replaced 34.14.219.64 → 34.47.167.251 in all Log HTTP nodes |
| 2026-03-23 | Atlas crashes 50+ times — bad n8n_create_workflow tool schema | Fixed: added items:{type:object} to nodes array |
| 2026-03-23 | Atlas crashes on GPT-5.3 calls — max_tokens not supported | Fixed: flagged gpt53 as is_reasoning to use max_completion_tokens |
| 2026-03-23 | Obsidian vault stale — not updating | Fixed: was caused by Atlas crashes above. Webhook confirmed working. |
| 2026-03-21 | GCP disk 100% full | Fixed: cleaned up duplicate skill repos |
| 2026-03-20 | n8n API edits corrupted workflow state | Fixed: avoid editing 200+ node workflows via API |
| 2026-03-21 | Gemini API key blocked by IP restriction | Fixed: whitelisted VM IPs |

## Tech Gotchas (permanent notes)
- Gemini API key has IP restriction — must allowlist both IPv4 and IPv6 of VMs
- n8n `specifyBody: json` with expressions in `jsonBody` fails validation — use Code node to pre-serialize
- n8n `webhook-test/` URLs only work in test mode — use `webhook/` for production
- Azure VM only has 1.9GB RAM — avoid restarting multiple PM2 services simultaneously
- GPT-5.3 uses `max_completion_tokens` not `max_tokens`
- Product data on foundersystems.in is hardcoded in JSX — no CMS or API yet
- GCP VM IP changes on restart — update System State Sync + all n8n HTTP nodes when IP changes
- n8n PUT /api/v1/workflows/{id} rejects `availableInMCP` and `binaryMode` in settings — strip before PUT
