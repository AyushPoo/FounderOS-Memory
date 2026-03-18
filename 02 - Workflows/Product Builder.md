# 🏭 Product Builder

## Overview
Takes an idea, finds relevant skills from the VM, creates a detailed build plan using GPT 5.3, classifies the product type, and routes to the appropriate builder workflow.

## Configuration
- **Workflow ID:** vo7WHaL6rq7yKRvm
- **Trigger:** Webhook POST to `/webhook/build-product`
- **Body:** `{"idea": "description of the idea"}`
- **LLM:** GPT 5.3 (Azure OpenAI)
- **Status:** ⚠️ Active but incomplete

## Pipeline

### Step 1: Extract Idea
Simple code node that pulls `$json.idea` from the webhook body.

### Step 2: SSH → VM → Find Skills
Connects to VM via SSH and runs a bash script that:
1. Goes to `/home/ayushpoojary1/founder-os/skill-repos/`
2. Finds all SKILL.md files across repos
3. Keyword-matches skills to the idea:
   - web/frontend/ui/react → frontend skills
   - api/backend/server → backend skills
   - python → python skills
   - test → testing skills
   - deploy → deployment skills
4. Falls back to "frontend-patterns api-design" if no matches
5. Returns content of up to 3 matched SKILL.md files (first 100 lines each)

**⚠️ Issue:** Doesn't use the `skill-registry.json` that already maps types → skills.

### Step 3: Build Prompt
Code node combines idea + cleaned skills context (escaped, limited to 3000 chars).

### Step 4: Planner (GPT 5.3)
Sends to Azure OpenAI GPT 5.3 with a detailed system prompt:

**Classification:** Assigns one of: `web_app`, `excel`, `extension`, `script`
**Plan includes:**
- product_name, tagline, target_user
- problem_solved, success_criteria
- mvp_features (3-5 items)
- out_of_scope
- tech_stack (framework, language, styling, hosting, database)
- file_structure
- build_steps (with time estimates)
- quality_gates
- pricing_recommendation
- estimated_build_hours
- complexity_score

### Step 5: Route by Classification
If node checks `classification.type`:
- `web_app` → sends to [[Builder - Web App]]
- `excel` → ❌ Telegram "not ready"
- `extension` → ❌ Telegram "not ready"
- `script` → ❌ Telegram "not ready"

**⚠️ Bug:** If node uses AND combinator — should be Switch/OR.

## Azure OpenAI Endpoint
```
POST https://ayush-mmu7mtqf-eastus2.cognitiveservices.azure.com/
     openai/deployments/gpt-5.3-chat/chat/completions
     ?api-version=2024-12-01-preview
```

## Not Yet Connected
- [ ] Founder OS Agent cannot trigger this — needs tool connection
- [ ] No notification back to Telegram on completion
- [ ] No logging of plans to Obsidian
- [ ] Doesn't use skill-registry.json for smarter matching
