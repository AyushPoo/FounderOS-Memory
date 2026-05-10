# Founder Systems Dashboard

> Mission: run Founder Systems from one current operating memory instead of scattered migration notes.

Last refreshed: `2026-05-10`

## Quick links

- [[Architecture Overview]]
- [[VM Status]]
- [[Known Issues]]
- [[Workflow Index]]
- [[Website Schema]]
- [[Context for AI Tools]]

## Live system status

| Component | Status | Notes |
|-----------|--------|-------|
| `foundersystems.in` | Live | Vercel marketing/storefront surface |
| `promptdeck.foundersystems.in` | Live | Vercel PromptDeck frontend |
| Founder Systems shared API | Live | AWS, health check OK |
| PromptDeck API | Live | AWS, health check OK |
| PromptDeck legacy API | Live | AWS `127.0.0.1:8090`, still needed for `/upload` and `/chat` |
| Open Design daemon | Live | Docker on AWS |
| Postgres | Live | AWS local Postgres `18-main` |
| `n8n` | Live | AWS PM2 process, public subdomain active |
| `openclaw` | Live | AWS gateway on `openclaw.foundersystems.in` |
| `paperclip` | Live | AWS Node app on `paperclip.foundersystems.in` |
| LiteLLM + Bedrock | Live | Active PromptDeck LLM routing |
| Azure VM | Legacy | No longer in active production path |

## Current priorities

1. Stabilize PromptDeck chat, attachment handling, and source-grounding UX after the AWS migration.
2. Clean old Azure/GCP secrets and env residue from PM2 and related services.
3. Archive or disable active `_tmp_*` `n8n` workflows.
4. Decide when to fully shut down the old Azure VM after final rollback confidence.

## Current repos

| Repo | Purpose |
|------|---------|
| `AyushPoo/Founder-Systems` | Main website, shared auth/payment surface |
| `promptdeck` | PromptDeck frontend + backend codebase |
| `FounderOS-Memory` | This operating memory vault |
