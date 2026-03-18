# 🐛 Known Issues

## Critical
- [ ] **Disk 100% full** — VM has 0 bytes free. Delete duplicate skill repos. See [[VM Status]]
- [ ] **Builder - Web App broken** — URL has "Headers:" appended, header name/value swapped, uses `/webhook-test/` (test mode), workflow is INACTIVE
- [ ] **Product Builder not connected to Founder OS Agent** — no tool call from the Telegram agent to trigger builds

## High Priority  
- [ ] **If node in Product Builder uses AND logic** — checks if type equals web_app AND excel AND extension AND script (impossible). Should be a Switch node or use OR logic
- [ ] **Post-Planner code node is placeholder** — just adds `myNewField = 1`, doesn't parse GPT response properly
- [ ] **Only web_app builder exists** — excel, extension, script builders not built yet
- [ ] **Save Idea loses data** — only saves `$json.query` (the name), not the full description, score, or details

## Medium Priority
- [ ] **Ideas Fetcher wipes history** — clears entire Google Sheet before writing new ideas (loses all previous batches)
- [ ] **Skill matching is basic keyword grep** — Product Builder doesn't use the `skill-registry.json` that already exists on the VM
- [ ] **No error handling** — most workflows have no error catching or retry logic
- [ ] **No feedback loop** — built products aren't tracked, no quality review, no market analysis
- [ ] **Antigravity not connected** — website deployment is manual through Antigravity IDE

## Low Priority
- [ ] **3 copies of everything-claude-code repo** — wasting ~4GB of disk space
- [ ] **Double .md.md extensions** — some files were created with duplicate extensions (fixed in vault restructure)
- [ ] **No workflow versioning** — changes to n8n workflows aren't tracked

## Resolved
_None yet — let's start fixing things!_
