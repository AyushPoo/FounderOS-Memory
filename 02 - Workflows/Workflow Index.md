# Workflow Index
> Last updated: 2026-03-25 by co-founder agent

## n8n Workflows (GCP — 34.47.167.251.nip.io)

| Status | Name | ID | Description |
|--------|------|----|-------------|
| Active | Founder OS Agent | TzpURLXbI6iOfLqU | Main Telegram bot (Gemini) — legacy, superseded by Atlas v3 |
| Active | Ideas Fetcher | pkTIpthafQ88wkAy | Scrapes 9 sources, ranks with Gemini, saves to Google Sheets |
| Active | Get Idea Details | zgJBIZS3qUxEwwtd | Deep dive on a single idea |
| Active | Save Idea | rW7ohKD1BCAWUDtl | Bookmarks idea to Google Sheets |
| Active | Product Builder | vo7WHaL6rq7yKRvm | Skills lookup + GPT-5.3 planner — fixed 2026-03-25 |
| Active | Build Product Bridge | bOlABGUJiCiZ8I52 | Bridge workflow for product builds |
| Active | Obsidian Updater | Yg8BWmxKQuCHkn2k | Webhook → GitHub commits to vault |
| Active | System State Sync | 9LHPPJK0lPoxIls1 | Hourly — updates Workflow Index + Error Log — fixed 2026-03-25 |
| Active | Github Sync | 3HdXFHlJ6CI1iiPj | GitHub sync workflow |
| Active | Mem0 memories | BkmdYttcq5lNsyfN | Qdrant/Mem0 memory operations |
| Inactive | Builder - Web App | xiYFZhlToYLX9g4J | Next.js code gen — replaced by OpenCode on Azure |
| Inactive | Build_workflow | UenNZUVbklbHEyio | Legacy build workflow |
| Inactive | My workflow | zVHRqYSWy9WeprNX | Unnamed/unused |

## Atlas v3 Capabilities (Azure — 20.193.252.82)
Atlas is the **primary interface** as of 2026-03-22. Replaces the n8n Founder OS Agent for most tasks.

| Tool | What It Does |
|------|--------------|
| ssh_gcp | Run shell commands on GCP VM |
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
| analyze_image | Gemini vision — analyze screenshots |
| github_browse | Browse any GitHub repo |
| store_learning | Store learning to Qdrant + vault |
| read_own_code | Atlas reads its own source |

## Known Broken / Inactive
- **Builder - Web App** — inactive, replaced by OpenCode CLI on Azure
- **Founder OS Agent (n8n)** — still active but Atlas v3 is now the primary agent
