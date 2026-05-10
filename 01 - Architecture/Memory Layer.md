# Memory Layer

Last refreshed: `2026-05-10`

## Canonical memory

The canonical human-readable memory for Founder Systems is this repo:

- Obsidian vault
- stored in GitHub
- curated manually or by trusted automation only

## Current reality

There are still legacy “memory” services running on AWS:

- `memory-api` via PM2
- `atlas-api` via PM2
- `qdrant` in Docker

But those are not currently the same thing as “the source of truth.”

## Source of truth order

1. This vault for current operating state
2. App repos for exact implementation details
3. Live infra verification for anything operationally unstable

## Important cleanup note

Old notes in this vault referenced:

- GCP `nip.io` webhooks
- Azure OpenAI
- Atlas-on-Azure assumptions
- skill mirrors on older VMs

Those should be treated as historical unless a page has been refreshed after the AWS migration.
