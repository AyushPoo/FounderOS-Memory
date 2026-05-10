# Known Issues

Last refreshed: `2026-05-10`

## Open issues

| # | Issue | Severity | Notes |
|---|-------|----------|-------|
| 1 | PromptDeck first-turn chat, attachment, and source-grounding UX is still under active QA | High | Multiple fixes were deployed on `2026-05-10`, but end-user validation is still in progress |
| 2 | PromptDeck still depends on the legacy `8090` service for `/upload` and `/chat` | High | Backend is split between `8011` and `8090` |
| 3 | Several active `_tmp_*` workflows are still enabled in `n8n` | Medium | These should be archived or disabled before they create confusion |
| 4 | PM2 processes still carry old Azure/GCP-era env variables and webhook references | High | Secrets rotation and env cleanup are still pending |
| 5 | `founder-agent` is online but has a very large historical restart count | Medium | Treat it as not fully trusted until audited |
| 6 | Azure VM still exists as a rollback box | Low | Remove only after rollback confidence and key rotation |

## Recently fixed

| Date | Fix |
|------|-----|
| `2026-05-10` | Full public backend cutover from Azure VM to AWS EC2 |
| `2026-05-10` | Active PromptDeck and related workflow traffic moved off Azure OpenAI to Bedrock via LiteLLM |
| `2026-05-10` | Active `n8n` Azure SSH usage was migrated to AWS |
| `2026-05-10` | PromptDeck attachment routing no longer silently falls back to prompt-only generation in the known fixed branches |

## Permanent operational notes

- The root path of `api.foundersystems.in` and `promptdeck-api.foundersystems.in` returning `404` is not, by itself, an outage. Use `/health` to verify those services.
- Do not trust old `nip.io`, GCP, or Azure notes unless they are explicitly marked historical.
- This vault should be updated after infra migrations, workflow changes, routing changes, and pricing/auth changes.
