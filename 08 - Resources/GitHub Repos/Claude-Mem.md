# Claude-Mem

**Repo:** https://github.com/thedotmack/claude-mem  
**Author:** Alex Newman (@thedotmack)  
**Type:** Persistent Memory Plugin for Claude Code  
**Relevance:** Memory architecture, session continuity, context management

## What It Does
Automatically captures everything Claude does during coding sessions, compresses it with AI, and injects relevant context back into future sessions. Essentially gives Claude Code a persistent memory layer using SQLite + Chroma vector search.

## Key Features
- 5 lifecycle hooks (SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd)
- SQLite database stores sessions, observations, summaries
- Chroma vector DB for semantic search across past sessions
- Web viewer UI at localhost:37777
- 3-layer search workflow: search → timeline → get_observations (10x token savings)
- Privacy control via tags to exclude sensitive content
- OpenClaw integration available: `curl -fsSL https://install.cmem.ai/openclaw.sh | bash`

## Architecture Insight (Useful for our memory system)
The 3-layer memory retrieval pattern is worth copying:
1. **search** → compact index (~50-100 tokens/result)
2. **timeline** → chronological context around interesting results  
3. **get_observations** → full details only for filtered IDs

This is basically what our Obsidian vault does — search tags/headers first, then drill into specific notes.

## When to Use (For Founder Systems)
- Reference the 3-layer search pattern when designing how I query the vault
- The lifecycle hook architecture is worth studying for n8n trigger design
- If we ever add a coding agent to the stack, install claude-mem on it

## Tags
#memory #context #persistence #claude-code #architecture
