# Workflow Index

> Last updated: 2026-03-21 (auto-sync)

All n8n workflows in the Founder Systems infrastructure.

## Active Workflows

### Founder OS Agent
- **ID:** TzpURLXbI6iOfLqU
- **Status:** ACTIVE (but erroring — 20+ failures today)
- **Trigger:** Telegram message (Bot 2)
- **LLM:** Google Gemini 2.0 Flash
- **Memory:** PostgreSQL chat memory (last 10 messages)
- **Tools:** get_startup_ideas, get_idea_details, save_idea, ask_founder_memory, list_workflows, delete_workflows, build_product
- **Purpose:** Main AI assistant — handles ideas, details, saves, builds, workflow management

### Ideas Fetcher
- **ID:** pkTIpthafQ88wkAy
- **Status:** ACTIVE
- **Trigger:** Called by Founder OS Agent
- **LLM:** Google Gemini (ranking)
- **Purpose:** Scrapes 9 sources, ranks top 7 ideas, stores to Google Sheets
- **Issue:** Wipes sheet before writing (loses history)

### Get Idea Details
- **ID:** zgJBIZS3qUxEwwtd
- **Status:** ACTIVE
- **Trigger:** Called by Founder OS Agent with idea_name
- **Purpose:** Deep breakdown of a specific idea

### Save Idea
- **ID:** rW7ohKD1BCAWUDtl
- **Status:** ACTIVE
- **Trigger:** Called by Founder OS Agent
- **Purpose:** Saves idea to Google Sheets
- **Issue:** Only saves name, not full details/score

### Product Builder
- **ID:** vo7WHaL6rq7yKRvm
- **Status:** ACTIVE but incomplete
- **Trigger:** Webhook POST
- **LLM:** GPT 5.3 (Azure OpenAI)
- **Purpose:** Idea to skills match to GPT plan to builder routing
- **Issue:** If node uses AND logic (impossible), not connected to Agent

### Build Product Bridge
- **ID:** bOlABGUJiCiZ8I52
- **Status:** ACTIVE
- **Purpose:** Bridge between Agent build_product tool and Product Builder
- **Updated:** 2026-03-21

### Obsidian Updater
- **ID:** Yg8BWmxKQuCHkn2k
- **Status:** ACTIVE
- **Trigger:** POST /webhook/update-obsidian
- **Purpose:** Writes/appends content to Obsidian vault via GitHub API + syncs to Mem0
- **Actions supported:** append, overwrite, create, update_table

### Github Sync
- **ID:** 3HdXFHlJ6CI1iiPj
- **Status:** ACTIVE
- **Trigger:** GitHub webhook (push to FounderOS-Memory)
- **Purpose:** Syncs changed .md files from GitHub to Mem0 vector store

### Mem0 Memories
- **ID:** BkmdYttcq5lNsyfN
- **Status:** ACTIVE
- **Trigger:** POST /webhook/memory
- **Purpose:** Receives memory text, searches Mem0, routes to correct Obsidian folder, saves to GitHub

### System State Sync
- **ID:** (to be created)
- **Status:** PLANNED
- **Purpose:** Hourly sync of VM status, workflow list, errors to vault

## Inactive Workflows

### Builder - Web App
- **ID:** xiYFZhlToYLX9g4J
- **Status:** INACTIVE (broken config)
- **Note:** Replaced by OpenCode direct execution on Azure VM

### Build_workflow
- **ID:** UenNZUVbklbHEyio
- **Status:** INACTIVE
- **Purpose:** Meta-tool to generate n8n workflows from description

### My workflow
- **ID:** zVHRqYSWy9WeprNX
- **Status:** INACTIVE
- **Purpose:** Unknown/test

## Pipeline Map
```
Telegram -> [Founder OS Agent]
              -> get_startup_ideas -> [Ideas Fetcher] -> Google Sheets
              -> get_idea_details  -> [Get Idea Details]
              -> save_idea         -> [Save Idea] -> Google Sheets
              -> build_product     -> [Build Product Bridge] -> [Product Builder]
                                                               -> Azure VM (OpenCode)
                                                               -> GitHub -> Website
              -> ask_founder_memory -> Mem0 /agent
              -> list/delete workflows -> n8n API

GitHub push -> [Github Sync] -> Mem0
POST /memory -> [Mem0 Memories] -> Obsidian + Mem0
POST /update-obsidian -> [Obsidian Updater] -> GitHub + Mem0
```
