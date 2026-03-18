# ⚡ Workflow Index

All n8n workflows in the Founder Systems infrastructure.

## Active Workflows

### Founder OS Agent
- **ID:** YSPgCuzj9JIHS7EG
- **Status:** ✅ Active
- **Trigger:** Telegram message
- **LLM:** Google Gemini
- **Purpose:** Main AI assistant — handles ideas, details, saves, workflow management
- **Details:** [[Founder OS Agent]]

### Ideas Fetcher
- **ID:** pkTIpthafQ88wkAy
- **Status:** ✅ Active
- **Trigger:** Called by Founder OS Agent
- **LLM:** Google Gemini (for ranking)
- **Purpose:** Scrapes 9 sources, ranks top 7 ideas, stores to Google Sheets
- **Details:** [[Ideas Fetcher]]

### Get Idea Details
- **ID:** zgJBIZS3qUxEwwtd
- **Status:** ✅ Active
- **Trigger:** Called by Founder OS Agent with idea_name
- **LLM:** Google Gemini
- **Purpose:** Deep breakdown of a specific idea (what, problem, feasibility, MVP, monetization)

### Save Idea  
- **ID:** rW7ohKD1BCAWUDtl
- **Status:** ✅ Active
- **Trigger:** Called by Founder OS Agent
- **Purpose:** Saves bookmarked idea to Google Sheets "Saved Ideas" tab
- **⚠️ Issue:** Only saves name, not full details/score

### Product Builder
- **ID:** vo7WHaL6rq7yKRvm
- **Status:** ⚠️ Active but incomplete
- **Trigger:** Webhook POST to `/webhook/build-product`
- **LLM:** GPT 5.3 (Azure OpenAI)
- **Purpose:** Takes idea → finds skills on VM → plans with GPT 5.3 → routes to builder
- **Details:** [[Product Builder]]

## Inactive Workflows

### Builder - Web App
- **ID:** xiYFZhlToYLX9g4J
- **Status:** ❌ Inactive (broken config)
- **LLM:** GPT 5.3 (Azure OpenAI)
- **Purpose:** Generate complete Next.js app code from a plan
- **Details:** [[Builder - Web App]]

### Build_workflow
- **ID:** UenNZUVbklbHEyio
- **Status:** ❌ Inactive
- **Purpose:** Meta-tool to generate n8n workflows from description (not part of main pipeline)

### Activate Workflow Bot
- **ID:** 2A2KKaHX45F7wiSr
- **Status:** ❌ Inactive
- **Purpose:** Telegram bot to approve/activate newly created workflows

## Workflow Map
```
Telegram → [Founder OS Agent] → [Ideas Fetcher] → Google Sheets
                               → [Get Idea Details]
                               → [Save Idea] → Google Sheets
                               → (TODO: connect) [Product Builder]
                                                      ↓
                                                  SSH → VM Skills
                                                      ↓
                                                  GPT 5.3 Planner
                                                      ↓
                                                  Route by type
                                                      ↓
                                              [Builder - Web App] → (TODO: deploy)
```
