# Context for AI Tools

Use this when bootstrapping a new AI session on Founder Systems.

Last refreshed: `2026-05-10`

## Master context block

```text
You are helping Ayush Poojary operate Founder Systems.

Founder Systems current live stack:
- foundersystems.in on Vercel
- promptdeck.foundersystems.in on Vercel
- api.foundersystems.in on AWS
- promptdeck-api.foundersystems.in on AWS
- n8n.foundersystems.in on AWS
- openclaw.foundersystems.in on AWS
- paperclip.foundersystems.in on AWS

Primary backend host:
- AWS EC2 public IP: 52.87.13.200
- The old Azure VM 20.193.252.82 is legacy/rollback only unless explicitly stated otherwise.

Current important runtime facts:
- Founder Systems shared API is on AWS.
- PromptDeck backend is on AWS.
- PromptDeck still has a legacy backend service on port 8090 for some routes.
- PromptDeck uses Open Design on AWS.
- Active PromptDeck LLM traffic is off Azure OpenAI and goes through LiteLLM to Amazon Bedrock.
- n8n is running on AWS and the live workflow inventory should be read from the vault's Workflow Index.

Key repos:
- AyushPoo/Founder-Systems
- promptdeck
- FounderOS-Memory

Current operating priority:
- stabilize PromptDeck UX and source-grounding after the AWS migration
- clean old Azure/GCP secrets, envs, and temporary workflows
- keep this memory repo aligned with the real production state
```

## Rule

If a new session finds older GCP/Azure notes, trust the refreshed May 10, 2026 vault pages first.
