# Known Issues

> Last updated: 2026-03-21 (auto-sync)

## Critical
- [ ] **Founder OS Agent errors** — workflow TzpURLXbI6iOfLqU throwing errors on every Telegram message (20+ errors today). Needs investigation.
- [ ] **Builder - Web App inactive** — workflow xiYFZhlToYLX9g4J is INACTIVE. Builds now triggered via OpenCode directly on Azure VM instead.
- [ ] **Product Builder not connected to Agent** — no tool call from Telegram agent to trigger builds end-to-end

## High Priority
- [ ] **If node in Product Builder uses AND logic** — impossible condition, should be Switch node
- [ ] **Post-Planner code node is placeholder** — just adds myNewField=1, does not parse GPT response
- [ ] **Only web_app builder exists** — excel, extension, script builders not built yet
- [ ] **Save Idea loses data** — only saves name, not full description/score/details

## Medium Priority
- [ ] **Ideas Fetcher wipes history** — clears entire Google Sheet before writing new ideas
- [ ] **Skill matching is basic keyword grep** — skill-registry.json exists but not used properly
- [ ] **No error handling in workflows** — most have no error catching or retry logic
- [ ] **No feedback loop** — built products not tracked, no quality review, no market analysis
- [ ] **Antigravity not connected** — website deployment is manual
- [ ] **Product data on website is hardcoded JSX** — no CMS or API

## Low Priority
- [ ] **founder-os-skills/ duplicate** — 42MB duplicate on GCP VM (safe to delete when needed)
- [ ] **No workflow versioning** — n8n workflow changes not version tracked
- [ ] **PM2 memory-server restarts** — 62 restarts, investigate root cause

## Resolved
- [x] **Disk 100% full** — was stale info. Actual: 78% used (22GB/30GB). Not critical.
- [x] **Mem0 security** — API key auth added 2026-03-21, keys moved to .env
- [x] **Stale vault** — auto-sync system built 2026-03-21
