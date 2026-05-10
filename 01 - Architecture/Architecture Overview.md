# Architecture Overview

Last refreshed: `2026-05-10`

## Production topology

```text
Vercel
  foundersystems.in
  promptdeck.foundersystems.in
        |
        v
AWS EC2 52.87.13.200
  nginx :80/:443
    |- api.foundersystems.in              -> founder-systems-api.service   -> 127.0.0.1:8010
    |- promptdeck-api.foundersystems.in   -> promptdeck-api.service        -> 127.0.0.1:8011
    |- legacy PromptDeck routes           -> promptdeck-legacy.service     -> 127.0.0.1:8090
    |- n8n.foundersystems.in              -> n8n (PM2)                     -> :5678
    |- openclaw.foundersystems.in         -> openclaw-gateway              -> :7890
    `- paperclip.foundersystems.in        -> paperclip (PM2)               -> 127.0.0.1:3100

AWS sidecars
  Postgres 18-main                        -> 127.0.0.1:5432
  Open Design daemon (Docker)             -> 127.0.0.1:7456
  Qdrant (Docker)                         -> :6333
  LiteLLM proxy (PM2)                     -> :4000
```

## Live frontends

| Surface | Hosting | Purpose |
|---------|---------|---------|
| `foundersystems.in` | Vercel | Main Founder Systems marketing/account/product surface |
| `promptdeck.foundersystems.in` | Vercel | PromptDeck frontend |

## Live AWS services

| Service | Runtime | Status | Notes |
|---------|---------|--------|-------|
| `founder-systems-api.service` | systemd | Live | Shared auth, entitlements, payments |
| `promptdeck-api.service` | systemd | Live | PromptDeck backend / finisher |
| `promptdeck-legacy.service` | systemd | Live | Legacy PromptDeck routes still required |
| `promptdeck-design-engine.service` | systemd + Docker | Live | Open Design daemon |
| `nginx.service` | systemd | Live | Public edge / TLS |
| `postgresql@18-main.service` | systemd | Live | Local production DB on AWS |
| `n8n` | PM2 | Live | Automation control plane |
| `litellm-proxy` | PM2 | Live | LLM gateway on AWS |
| `openclaw-gateway` | direct process | Live | Public `openclaw` surface |
| `paperclip` | PM2 | Live | Public `paperclip` surface |

## Docker workloads

| Container | Purpose | Port |
|-----------|---------|------|
| `promptdeck-design-engine` | Open Design daemon | `127.0.0.1:7456` |
| `qdrant` | Vector store | `0.0.0.0:6333` |

## LLM architecture

- PromptDeck is no longer on Azure OpenAI for active traffic.
- Active PromptDeck model traffic goes through LiteLLM on AWS.
- LiteLLM is backed by Amazon Bedrock.
- Cheaper Bedrock models are used for most routine traffic to control cost.
- Claude is not the current default live model path.

## Legacy infrastructure

| Legacy surface | Current role |
|----------------|-------------|
| Azure VM `20.193.252.82` | Rollback / legacy only, not in active production path |
| Old GCP `nip.io` docs | Historical only, no longer source of truth |

## Repos that matter

| Repo | Role |
|------|------|
| `AyushPoo/Founder-Systems` | Founder Systems frontend + shared product/account surface |
| `promptdeck` | PromptDeck codebase |
| `FounderOS-Memory` | This vault |
