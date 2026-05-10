# Decisions Log

Last refreshed: `2026-05-10`

## 2026-05-10

### AWS is the primary production host
- **Decision:** The live Founder Systems and PromptDeck backend stack now runs from AWS EC2.
- **Reason:** Full migration completed and public backend traffic was cut over.

### Azure is legacy, not primary
- **Decision:** The old Azure VM is now rollback infrastructure only.
- **Reason:** Active backend dependencies were migrated away from it.

### PromptDeck LLM path moved to Bedrock via LiteLLM
- **Decision:** Active PromptDeck model traffic should route through LiteLLM on AWS to Amazon Bedrock.
- **Reason:** Remove Azure OpenAI from the active path and centralize model control plus rate limiting.

### This vault should describe current state, not migration archaeology
- **Decision:** Remove or rewrite stale GCP/Azure-era notes instead of keeping contradictory “history” pages as if they were live docs.
- **Reason:** A memory repo that lies is worse than no memory repo.

## Still open

- Decide whether the legacy Founder OS Agent / atlas / memory sidecar stack remains strategic.
- Decide when the Azure VM can be fully shut down.
