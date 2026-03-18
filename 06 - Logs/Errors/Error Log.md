# 🔴 Error Log

Known errors, what caused them, and how to fix them.

## Format
```
### [Date] — [Workflow/Component] — [Error]
**What happened:**
**Root cause:**
**Fix:**
**Learning:**
```

---

## Active Errors

### 2026-03-18 — Builder - Web App — Broken HTTP config
**What happened:** Workflow is inactive and won't receive webhook calls
**Root cause:**
1. URL has " Headers:" appended to the end (copy-paste error)
2. Content-Type header has the value in the name field
3. API key header is missing the key name
4. Using `/webhook-test/` path (only works in n8n test mode)
**Fix:**
1. Set URL to: `https://ayush-mmu7mtqf-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-5.3-chat/chat/completions?api-version=2024-12-01-preview`
2. Set header name: `Content-Type`, value: `application/json`
3. Set header name: `api-key`, value: `7TMa4sqZEtBKdeQLllEdy4foXVuDmdY9urGxMQxh4pv9JQqxbU6uJQQJ99CCACHYHv6XJ3w3AAAAACOGpw7Y`
4. Change webhook path to `/webhook/builder-webapp`
5. Activate the workflow
**Learning:** Always test HTTP nodes manually before connecting downstream

### 2026-03-18 — Product Builder If Node — AND logic bug
**What happened:** If node can never be true — checks if classification equals web_app AND excel AND extension AND script simultaneously (impossible)
**Root cause:** Wrong combinator set to AND instead of OR (or should use a Switch node)
**Fix:** Replace If node with a Switch node that routes on `classification.type` value
**Learning:** Use Switch node for multi-branch routing in n8n, not If with multiple conditions

### 2026-03-18 — VM Disk — 100% Full
**What happened:** VM has 0 bytes free space
**Root cause:** 3 copies of same GitHub repo (~4GB total)
**Fix:** SSH in and run:
```bash
rm -rf /home/ayushpoojary1/founder-os-skills/everything-claude-code
rm -rf /home/ayushpoojary1/founder-os/skill-repos/everything-claude-code
```
**Learning:** Don't clone the same repo multiple times — use symlinks or a single source

---

## Resolved Errors

_None yet._
