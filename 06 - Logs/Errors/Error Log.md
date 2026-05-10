# Error Log

Last refreshed: `2026-05-10`

## Active concerns

### 2026-05-10 - PromptDeck strategist and source-grounding UX
**What happened:** PromptDeck could accept an uploaded source file but still answer through a generic strategist path or leave the attachment looking unsent.
**Current state:** Multiple fixes were deployed on 2026-05-10. End-user validation is still ongoing.
**Learning:** Build-lane attachment state and background context state must not be conflated.

### 2026-05-10 - Legacy split PromptDeck backend
**What happened:** PromptDeck public routing still depends on both the modern API service and the legacy `8090` service.
**Current state:** Stable enough for production, but still architectural debt.
**Learning:** Route-level migrations need explicit verification for legacy endpoints like `/upload` and `/chat`.

### 2026-05-10 - Temporary workflow sprawl in n8n
**What happened:** Several `_tmp_*` workflows remain active in production `n8n`.
**Current state:** Cleanup pending.
**Learning:** Temporary operational helpers should be archived quickly after migrations.
