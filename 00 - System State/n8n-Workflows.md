# n8n Workflows — Founder Systems
*Last updated: 2026-04-03 (auto-audited)*
*Instance: https://n8n.foundersystems.in*
*Total: 37 production workflows*

---

## Overview Table

| ID | Name | Active | Trigger | Nodes |
|----|------|--------|---------|-------|
| `2fRABiuMQl9u2Yl1` | Builder - Excel | ✅ | webhook | 8 |
| `2mUdmoDVzE0Ffw3u` | Builder - Chrome Extension | ✅ | webhook | 7 |
| `3HdXFHlJ6CI1iiPj` | Github Sync | ✅ | webhook | 7 |
| `3PbQ1mhLMWbNjavf` | Builder - Notion Template | ✅ | webhook | 8 |
| `3tLxlEtCglMd0ZTE` | Builder - Dashboard | ✅ | webhook | 7 |
| `7VMGjulq7WAOy4Ht` | 🔒 Daily n8n Backup → GitHub | ✅ | schedule | 5 |
| `7uM628kfwUq8nD31` | Analytics Data Collector | ✅ | schedule | 9 |
| `9LHPPJK0lPoxIls1` | System State Sync | ✅ | schedule | 6 |
| `A85rm1XmCAWhhZkl` | GitHub Publisher | ✅ | executeWorkflow | 6 |
| `AdIIHzlm87ebMfp9` | Marketing Engine | ✅ | webhook | 4 |
| `BkmdYttcq5lNsyfN` | Mem0 memories | ✅ | webhook | 6 |
| `DRG4H5PvSNqIpIZm` | Builder - Landing Page | ✅ | webhook | 7 |
| `HXEYSJjmCFskP7CD` | Setup Runner | ❌ | webhook | 3 |
| `IlEp1rBngL7o5EZi` | Post Generator - Marketing | ✅ | webhook | 8 |
| `KwSOa5llfq4LicY5` | Marketing Actions | ✅ | telegram | 11 |
| `NcdjFfhrCKhk6X5r` | Analytics Weekly Summary | ✅ | schedule | 7 |
| `QSfn0rF9OftFuWpq` | Builder - PDF | ✅ | webhook | 8 |
| `SpoWroLQSB090flz` | Builder - Script | ✅ | webhook | 7 |
| `TzpURLXbI6iOfLqU` | Founder OS Agent | ✅ | telegram | 12 |
| `UenNZUVbklbHEyio` | Build_workflow | ❌ | executeWorkflow | 7 |
| `YfcZDpMpgDwpbDUZ` | Marketing Agent (Phase 5) | ✅ | telegram | 28 |
| `Yg8BWmxKQuCHkn2k` | Obsidian Updater | ✅ | webhook | 8 |
| `Z9UMfP6oE6weUe1q` | Product Publisher | ✅ | webhook | 7 |
| `a7qvacpHEoRt5Lu9` | ⚠️ Error Handler | ✅ | error | 2 |
| `bOlABGUJiCiZ8I52` | Build Product Bridge | ✅ | executeWorkflow | 3 |
| `kBwt0eAhfLBRmaN4` | 🩺 Health Monitor (5min) | ✅ | schedule | 5 |
| `o26tVr23Ti0dwKXE` | Quality Gate | ✅ | webhook | 6 |
| `oMbMUAm87vHjo87P` | Website Publisher | ✅ | executeWorkflow | 9 |
| `pkTIpthafQ88wkAy` | Ideas Fetcher | ✅ | executeWorkflow | 32 |
| `rW7ohKD1BCAWUDtl` | Save Idea | ✅ | executeWorkflow | 4 |
| `vWv2fI34oFYY8J4c` | Quality Gate Actions | ✅ | telegram | 13 |
| `vo7WHaL6rq7yKRvm` | Product Builder | ✅ | webhook | 27 |
| `xiYFZhlToYLX9g4J` | Builder - Web App | ✅ | webhook | 6 |
| `yXPkDYoKc4H2aLiB` | Founder OS Agent | ❌ | telegram | 12 |
| `zHE9Y6RsPGcfn4dC` | Builder - PowerPoint | ✅ | webhook | 8 |
| `zVHRqYSWy9WeprNX` | My workflow | ❌ | telegram | 74 |
| `zgJBIZS3qUxEwwtd` | Get Idea Details | ✅ | executeWorkflow | 4 |

---

## Workflow Groups

### 🏗️ Product Builders (Webhook-triggered)
Called by the main Product Builder or manually. All SSH into Azure VM to write/build code.

| Workflow | Purpose |
|----------|---------|
| Builder - Excel | GPT → generates Excel macro code → SSH write → build |
| Builder - Chrome Extension | GPT → extension scaffold → SSH write |
| Builder - Landing Page | GPT → HTML landing page → SSH write |
| Builder - Dashboard | GPT → React dashboard → SSH write |
| Builder - Notion Template | GPT → Notion template → SSH write |
| Builder - PDF | GPT → PDF generator → SSH write |
| Builder - Script | GPT → Python/JS script → SSH write |
| Builder - Web App | GPT → web app → SSH write |
| Builder - PowerPoint | GPT → PPTX → SSH write |

### 🧠 Core Pipeline
| Workflow | Trigger | Purpose |
|----------|---------|---------|
| Ideas Fetcher | executeWorkflow | 9 sources scraped → Gemini ranking → Google Sheets |
| Get Idea Details | executeWorkflow | Enriches idea with market data |
| Save Idea | executeWorkflow | Stores approved idea to Sheets/memory |
| Product Builder | Webhook | Routes idea → correct builder by type (27 nodes) |
| Build Product Bridge | executeWorkflow | Bridge between builder output and publishing |
| Quality Gate | Webhook | Validates built product quality |
| Quality Gate Actions | Telegram | Human approval flow for product QA |
| GitHub Publisher | executeWorkflow | Pushes built product to Founder-Systems repo |
| Website Publisher | executeWorkflow | Triggers Vercel redeploy + updates products.json |
| Product Publisher | Webhook | Syncs product to Gumroad + LemonSqueezy |

### 📣 Marketing
| Workflow | Trigger | Purpose |
|----------|---------|---------|
| Marketing Engine | Webhook | Orchestrates post creation → scheduling |
| Post Generator - Marketing | Webhook | GPT generates platform-specific posts |
| Marketing Actions | Telegram | Human approval/edit of marketing posts |
| Marketing Agent (Phase 5) | Telegram | Conversational marketing brainstorm (28 nodes) |

### 📊 Analytics & Reporting
| Workflow | Trigger | Purpose |
|----------|---------|---------|
| Analytics Data Collector | Schedule | Polls Gumroad/LS sales → stores in SQLite |
| Analytics Weekly Summary | Schedule | Weekly Telegram report of sales + metrics |
| Mem0 memories | Webhook | Stores/queries agent memories in Mem0 |
| Github Sync | Webhook | Syncs vault changes to Mem0 memory |

### 🤖 Agents
| Workflow | Trigger | Purpose |
|----------|---------|---------|
| Founder OS Agent | Telegram | Main @Rayquabot agent (12 nodes) |
| Marketing Agent (Phase 5) | Telegram | Marketing-specific agent |

### 🔧 System & Infrastructure
| Workflow | Trigger | Purpose |
|----------|---------|---------|
| ⚠️ Error Handler | errorTrigger | Catches all workflow errors → Telegram alert |
| 🔒 Daily n8n Backup → GitHub | Schedule (2AM IST) | Exports all workflows → FounderOS-Memory/backups/n8n/ |
| 🩺 Health Monitor (5min) | Schedule (5min) | Checks n8n + website + analytics API liveness |
| System State Sync | Schedule | Hourly vault refresh |
| Obsidian Updater | Webhook | Webhook → commits to FounderOS-Memory GitHub repo |

---

## Error Handling

Every production workflow has `settings.errorWorkflow = "a7qvacpHEoRt5Lu9"` (⚠️ Error Handler).
On failure → Telegram message to @Rayquabot with: workflow name, error message, last node, IST time, link.

---

## Key Credentials Used

| Credential | Used In |
|------------|---------|
| Azure SSH (sshPassword) | All Builder workflows — SSH into Azure VM |
| Telegram account 3 | All Telegram-triggered workflows + alerts |
| Google Gemini PaLM API | Ideas Fetcher ranking |
| Azure OpenAI (GPT-5.3) | All code generation in builders |
| GitHub PAT - FounderOS Memory | Obsidian Updater, Daily Backup |
| GitHub account | GitHub Publisher |
| Google Sheets OAuth2 | Ideas Fetcher storage |
| n8n API | Internal workflow calls |

---

## Inactive Workflows (❌)

| ID | Name | Reason |
|----|------|--------|
| HXEYSJjmCFskP7CD | Setup Runner | One-time setup, deactivated |
| UenNZUVbklbHEyio | Build_workflow | Replaced by Build Product Bridge |
| VXxA6yRzIipSvjhN | _tmp_read_atlas | Temp/debug |
| yXPkDYoKc4H2aLiB | Founder OS Agent (old) | Superseded by active version |
| zVHRqYSWy9WeprNX | My workflow | Draft/unused |
