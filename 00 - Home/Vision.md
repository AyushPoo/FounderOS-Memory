# Vision

Founder Systems is no longer just an “idea factory” concept. It is now a live stack with:

1. a public Founder Systems surface for auth, payments, and product access,
2. a live PromptDeck product with its own frontend and backend,
3. an AWS automation and services host running APIs, `n8n`, Open Design, Qdrant, and sidecar tools,
4. this repo as the human-readable operating memory for the whole system.

## Operating principles

- Keep one source of truth for current state.
- Prefer live, verified infra facts over old architectural intent.
- Separate “historical context” from “currently running production.”
- Remove migration clutter once it has served its purpose.
- Keep public surfaces stable while internal implementation evolves.

## Current reality

The most important current business/runtime surfaces are:

- `foundersystems.in`
- `promptdeck.foundersystems.in`
- `api.foundersystems.in`
- `promptdeck-api.foundersystems.in`
- `n8n.foundersystems.in`
- `openclaw.foundersystems.in`
- `paperclip.foundersystems.in`

The current Founder Systems operating problem is not “how do we invent the architecture?” It is:

- keep the AWS stack stable,
- finish removing old infra residue,
- improve PromptDeck quality and UX,
- keep `n8n` and app workflows aligned with the real production stack.
