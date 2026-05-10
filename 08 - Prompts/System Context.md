# System Context

Last refreshed: `2026-05-10`

The canonical reusable context now lives in [[Context for AI Tools]].

## Short version

Founder Systems current stack is:

- Vercel frontends
- AWS backend host
- PromptDeck live on its own frontend/backend pair
- shared Founder Systems API for auth/payments/entitlements
- `n8n`, Open Design, Qdrant, LiteLLM, `openclaw`, and `paperclip` on AWS
- Azure is legacy, not primary

## Rule

If a prompt or tool bootstrap still mentions old GCP `nip.io`, Azure OpenAI as the main live path, or Azure as the primary app host, it is stale and should be updated.
