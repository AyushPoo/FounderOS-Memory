# Workflow Index

> Last updated: 2026-04-04 by co-founder agent

## n8n Workflows (Azure â n8n.foundersystems.in)

Total: 37 production workflows | 32 active, 5 inactive

### ðï¸ Builders

| Status | Name | ID | Trigger | Description |
|--------|------|----|---------|-------------|
| â Active | Product Builder | vo7WHaL6rq7yKRvm | Webhook | Skills lookup + GPT-5.3 planner â main build orchestrator |
| â Active | Build Product Bridge | bOlABGUJiCiZ8I52 | executeWorkflow | Bridge for product build sub-flows |
| â Active | Builder - Web App | xiYFZhlToYLX9g4J | Webhook | Web app builder (static HTML via OpenCode) |
| â Active | Quality Gate Actions | (see n8n-Workflows.md) | executeWorkflow | Post-build quality checks |

### ð¥ Core Pipeline

| Status | Name | ID | Trigger | Description |
|--------|------|----|---------|-------------|
| â Active | Ideas Fetcher | pkTIpthafQ88wkAy | Schedule | Scrapes 9 sources, ranks with Gemini, saves to Google Sheets |
| â Active | Get Idea Details | zgJBIZS3qUxEwwtd | Webhook | Deep dive on a single idea |
| â Active | Save Idea | rW7ohKD1BCAWUDtl | Webhook | Bookmarks idea to Google Sheets |
| â Active | Founder OS Agent | TzpURLXbI6iOfLqU | Telegram | Legacy n8n Telegram bot (superseded by Atlas v3) |

### ð Deployment & Publishing

| Status | Name | ID | Trigger | Description |
|--------|------|----|---------|-------------|
| â Active | Github Sync | 3HdXFHlJ6CI1iiPj | Webhook | GitHub sync for product files |
| â Active | Obsidian Updater | Yg8BWmxKQuCHkn2k | Webhook | Pushes file content to FounderOS-Memory GitHub vault |
| â Active | System State Sync | 9LHPPJK0lPoxIls1 | Schedule | Hourly â updates vault docs from live system state |
| â Active | Product Publisher | (see n8n-Workflows.md) | Webhook | Syncs products.json â Gumroad + LemonSqueezy |

### ð£ Marketing

| Status | Name | ID | Trigger | Description |
|--------|------|----|---------|-------------|
| â Active | Marketing Agent Phase 5 | (see n8n-Workflows.md) | Telegram | Conversational marketing post brainstorming |
| â Active | (3 other marketing workflows) | â | â | Content gen + posting for Twitter, Reddit, LinkedIn |

### ð Analytics

| Status | Name | ID | Trigger | Description |
|--------|------|----|---------|-------------|
| â Active | (Analytics workflows) | â | Schedule | Gumroad + LemonSqueezy + GitHub data pull |
| â Active | (Weekly summary) | â | Schedule | Weekly revenue summary â Telegram Monday morning |

### ð¤ Agents

| Status | Name | ID | Trigger | Description |
|--------|------|----|---------|-------------|
| â Active | Mem0 memories | BkmdYttcq5lNsyfN | Webhook | Qdrant/Mem0 vector memory operations |

### âï¸ System & Infrastructure

| Status | Name | ID | Trigger | Description |
|--------|------|----|---------|-------------|
| â Active | â ï¸ Error Handler | a7qvacpHEoRt5Lu9 | Error Trigger | Catches failures from all 29 workflows â Telegram alert |
| â Active | ð Daily n8n Backup | 7VMGjulq7WAOy4Ht | Schedule (2AM IST) | Exports all workflows â GitHub backup |
| â Active | ð©º Health Monitor | kBwt0eAhfLBRmaN4 | Schedule (5min) | Checks n8n, foundersystems.in, analytics-api uptime |

### â Inactive

| Status | Name | ID | Notes |
|--------|------|----|-------|
| â Inactive | Build_workflow | UenNZUVbklbHEyio | Legacy |
| â Inactive | My workflow | zVHRqYSWy9WeprNX | Unused |
| â Inactive | (3 others) | â | Legacy/unused |

> ð Full workflow list with all IDs and node counts: see [[Infrastructure]] â `00 - System State/n8n-Workflows.md`

## Obsidian Updater Webhook

**URL:** `POST https://n8n.foundersystems.in/webhook/update-obsidian`
**Workflow ID:** Yg8BWmxKQuCHkn2k

```json
{
  "file": "path/to/file.md",
  "action": "overwrite",
  "content": "...full file content..."
}
```
Actions: `append`, `overwrite`, `create`, `update_table`

## Atlas v3 Capabilities (Azure â 20.193.252.82)

Atlas (@Blasikenbot) is the **primary interface** as of 2026-03-22.

| Tool | What It Does |
|------|--------------|
| ssh_azure | Run shell commands on Azure VM |
| mem0_search | Search Qdrant vector memory |
| mem0_store | Store memory to Qdrant |
| obsidian_read | Read any file from this vault |
| obsidian_write | Write/append to any vault file |
| n8n_list_workflows | List all n8n workflows |
| n8n_get_workflow | Get full workflow JSON |
| n8n_update_workflow | Update a workflow |
| n8n_create_workflow | Create a new workflow |
| n8n_toggle_workflow | Activate/deactivate workflow |
| n8n_trigger_webhook | Fire any n8n webhook |
| web_fetch | Fetch URL content |
| web_search | DuckDuckGo search |
| file_write | Write file to Azure VM |
| file_read | Read file from Azure VM |
| analyze_image | Gemini vision â analyze screenshots |
| github_browse | Browse any GitHub repo |
| store_learning | Store learning to Qdrant + vault |
| read_own_code | Atlas reads its own source |

> Note: `ssh_gcp` tool removed â GCP VM no longer exists.
