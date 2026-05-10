# Production Roadmap

Last refreshed: `2026-05-10`

This roadmap is now anchored to the current live stack, not the old GCP + Azure design.

## Phase 1: stabilize what is already live

- [ ] Finish PromptDeck UX fixes around attachment handling, strategist grounding, and build reliability.
- [ ] Remove or archive active `_tmp_*` workflows from `n8n`.
- [ ] Rotate old Azure and other leaked credentials after the migration work.
- [ ] Clean PM2 envs that still contain Azure/GCP-era variables and webhooks.
- [ ] Decide whether `promptdeck-legacy.service` can be retired or needs to remain a supported split backend.

## Phase 2: finish the Azure exit

- [ ] Do one final rollback-confidence pass on the AWS stack.
- [ ] Shut down the Azure VM once rollback is no longer needed.
- [ ] Remove old Azure OpenAI resources after secret rotation and workflow validation.
- [ ] Audit any remaining docs, scripts, or env files that still assume Azure/GCP.

## Phase 3: make the automation layer trustworthy

- [ ] Audit every active `n8n` workflow by intent, owner, and current usefulness.
- [ ] Separate production workflows from experiments and `_tmp_*` helpers.
- [ ] Define the canonical path for product publishing: builder workflow -> quality gate -> GitHub publisher -> website publisher.
- [ ] Re-verify the Obsidian/memory update workflow post-migration instead of trusting the old GCP webhook notes.

## Phase 4: simplify the operating model

- [ ] Decide whether the legacy Founder OS Agent / atlas / memory stack is still strategic or just leftover infrastructure.
- [ ] Decide whether Founder Systems should keep multiple parallel product pipelines or consolidate around the current website + PromptDeck stack.
- [ ] Keep this vault current enough that a new session can recover state without re-investigating the infrastructure.
