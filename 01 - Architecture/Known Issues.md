# Known Issues
> Last updated: 2026-03-25 by co-founder agent

## Open Issues

| # | Issue | Severity | Notes |
|---|-------|----------|-------|
| 1 | memory-server (GCP) — 62 restarts | Medium | Still running but unstable. Needs log investigation. |
| 2 | Product data hardcoded in JSX on foundersystems.in | Medium | No CMS. Every new product requires a code deploy. |
| 3 | Port 3000 exposed to internet on Azure | Low | Python HTTP server scanned by bots. Not a crash risk. |
| 4 | Product Builder workflow not connected to Atlas | Medium | Triggered via webhook only, not from Telegram/Atlas yet. |
| 5 | No deployment pipeline from Azure products/ to live website | High | Products built but served on raw port — not on foundersystems.in |
| 6 | Google Sheets OAuth expired | Medium | Save Idea workflow fails with EAUTH — needs re-auth in n8n credentials. |

## Fixed Issues

| Date | Issue | Fix |
|------|-------|-----|
| 2026-03-25 | System State Sync failing — 32+ consecutive hourly errors | Fixed: hardcoded old GCP IP (34.14.219.64) updated to current IP (34.47.167.251) in all HTTP nodes |
| 2026-03-25 | Product Builder 100% failure — Acknowledge Button Press killing workflow | Fixed: set continueRegularOutput on Acknowledge node so stale Telegram callbacks don't abort the build |
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
