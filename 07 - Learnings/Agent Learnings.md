# 🎓 Agent Learnings

What works, what doesn't, and what's been figured out about building with AI agents.

## LLM Usage Patterns

### What Works
- **Gemini for fast/cheap classification** — good for ranking, scoring, simple decisions
- **GPT 5.3 for complex generation** — better for detailed plans and code generation
- **Strict JSON output prompts** — always specify exact JSON structure with examples in the prompt, or LLMs return markdown-wrapped JSON that breaks parsing
- **Character limits for Telegram** — Telegram can't handle >4096 chars; keep responses under 3000 to be safe
- **Tool rules in system prompt** — being explicit ("RULE 1: ALWAYS call X tool") prevents the agent from guessing

### What Doesn't Work
- **Asking LLMs to remember across sessions** — they don't. Use PostgreSQL chat memory or this Obsidian vault
- **Relying on LLM to parse its own output** — always add a Code node to clean/parse LLM responses
- **Generic prompts** — LLMs without specific rules will take shortcuts; be explicit about every edge case
- **AND logic in If nodes** — for multi-branch routing, use Switch node

## n8n Patterns

### What Works
- **Sub-workflow tools** — using `toolWorkflow` nodes to call other workflows as tools works well for the agent pattern
- **PostgreSQL memory** — `memoryPostgresChat` keyed by chat ID provides real conversation memory
- **Code nodes for cleanup** — always add a Code node after LLM output to clean/parse before using data

### What Doesn't Work
- **Clearing sheets before writing** — loses historical data; use appendOrUpdate instead
- **SSH keyword matching** — simple grep misses relevant skills; needs semantic matching eventually

## Architecture Learnings

### 2026-03-18
- Having multiple AI tools (ChatGPT, Claude, BrowserOS, Gemini) without shared context creates conflicting advice
- Obsidian as a central vault + GitHub sync is the right solution for cross-tool memory
- The VM is the right place for skills/context storage — it's always accessible via SSH from n8n
- The deployment gap (code generated but not deployed) is the biggest missing piece in the pipeline

## Prompt Patterns That Work

### For JSON Output (Critical)
```
## ⚠️ CRITICAL: Output Format (STRICT JSON)
You MUST return ONLY a valid JSON object. No markdown code blocks. No extra text.
The JSON MUST have this EXACT structure:
{
  "field": "value"
}
Return ONLY the JSON. No ```json wrapper.
```

### For Tool-Calling Agents
```
RULE X — [ACTION]:
If the user [trigger condition] → [exact action]. No exceptions.
```
