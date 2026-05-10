# Website Schema

Last refreshed: `2026-05-10`

## Primary public surfaces

| Domain | Hosting | Purpose |
|--------|---------|---------|
| `foundersystems.in` | Vercel | Founder Systems marketing, product, account surface |
| `promptdeck.foundersystems.in` | Vercel | PromptDeck frontend |
| `api.foundersystems.in` | AWS + nginx | Shared Founder Systems API |
| `promptdeck-api.foundersystems.in` | AWS + nginx | PromptDeck backend |
| `n8n.foundersystems.in` | AWS + nginx | `n8n` UI |
| `openclaw.foundersystems.in` | AWS + nginx | Openclaw gateway |
| `paperclip.foundersystems.in` | AWS + nginx | Paperclip app |

## Backend routing notes

- `api.foundersystems.in/health` returns the Founder Systems API health payload.
- `promptdeck-api.foundersystems.in/health` returns the PromptDeck API health payload.
- `promptdeck-api.foundersystems.in` still uses split routing: modern PromptDeck backend on `8011`, legacy routes on `8090`.

## Repo ownership

| Repo | Role |
|------|------|
| `AyushPoo/Founder-Systems` | Main website and Founder Systems product/account surface |
| `promptdeck` | PromptDeck frontend/backend |

## Editing rule

Do not maintain exact product catalog copy, prices, or checkout links manually in this vault unless they were freshly verified from the live codebase. This page should describe structure and responsibilities, not become another stale hardcoded catalog.
