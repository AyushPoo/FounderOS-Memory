# FounderOS Memory

Central operating memory for Founder Systems.

Last refreshed: `2026-05-10`

This vault is meant to answer one question quickly: what is the current live state of Founder Systems right now?

## Current production snapshot

- `foundersystems.in` and `promptdeck.foundersystems.in` are live on Vercel.
- `api.foundersystems.in`, `promptdeck-api.foundersystems.in`, `n8n.foundersystems.in`, `openclaw.foundersystems.in`, and `paperclip.foundersystems.in` are live on the AWS EC2 host `52.87.13.200`.
- Founder Systems shared API, PromptDeck API, PromptDeck legacy API, nginx, Postgres, Open Design, Qdrant, `n8n`, `openclaw`, `paperclip`, and LiteLLM are running from AWS.
- Active PromptDeck LLM traffic has been migrated off Azure OpenAI to AWS Bedrock through LiteLLM.
- The old Azure VM `20.193.252.82` is no longer in the active production path, but it may still exist as a rollback box until explicitly shut down.

## Use this vault

- Start at [Dashboard](/F:/Work/FounderOS-Memory/00%20-%20Home/Dashboard.md).
- Use [Architecture Overview](/F:/Work/FounderOS-Memory/01%20-%20Architecture/Architecture%20Overview.md) for infra.
- Use [Workflow Index](/F:/Work/FounderOS-Memory/02%20-%20Workflows/Workflow%20Index.md) for live `n8n`.
- Use [Known Issues](/F:/Work/FounderOS-Memory/01%20-%20Architecture/Known%20Issues.md) for active cleanup items.

## What this repo is not

- It is not the source of truth for app code.
- It should not store secrets, SSH keys, or one-off migration scripts.
- It should not mirror stale GCP/Azure-era notes once production has moved on.
