# 🔄 Auto Update System

How Obsidian gets automatically updated from n8n, the VM, and AI tools.

## Architecture

```
n8n workflows          → webhook → [Obsidian Updater Workflow] → GitHub API → vault  ✅ LIVE
Website GitHub pushes  → GitHub Action → GitHub API → vault                          ✅ LIVE
BrowserOS/Chrome       → JS bookmarklet → webhook → GitHub API → vault               ✅ READY
LLM sessions           → tell OpenClaw → webhook → GitHub API → vault                ✅ LIVE
OpenClaw sessions      → auto-logged by OpenClaw → webhook → GitHub API → vault      ✅ LIVE
Telegram conversations → Founder OS Agent → (optional /log-session command)          🔲 Optional
```

## The Obsidian Updater Workflow ✅ LIVE

**Workflow ID:** Yg8BWmxKQuCHkn2k  
**Webhook:** `POST https://34.14.219.64.nip.io/webhook/update-obsidian`  
**Status:** Active (activated 2026-03-19)

### Request Format
```json
{
  "file": "06 - Logs/n8n/n8n Execution Log.md",
  "action": "append",
  "content": "| 2026-03-19 13:30 | Ideas Fetcher | ✅ Success | Fetched 7 ideas |",
  "section": "## Recent Executions"
}
```

### Supported Actions
- `append` — add to end of file or below a section header
- `update_table` — add a row to a markdown table (alias for append)
- `overwrite` — replace entire file content
- `create` — create a new file

## Connection Status

| Connection | Status | Notes |
|------------|--------|-------|
| n8n → Obsidian | ✅ Live | Obsidian Updater workflow active |
| Ideas Fetcher → Obsidian | ✅ Wired | Logs to n8n Execution Log |
| Save Idea → Obsidian | ✅ Wired | Logs to Saved Ideas.md |
| Product Builder → Obsidian | ✅ Wired | Logs build events |
| Antigravity/Website → Obsidian | 🔲 Not built | GitHub Action needed |
| BrowserOS → Obsidian | 🔲 Not built | Bookmarklet/paste flow |
| LLM Conversations → Obsidian | 🔲 Not built | Manual paste via OpenClaw |

## GitHub API Approach

Uses GitHub Contents API — no git CLI needed:

```
GET /repos/AyushPoo/FounderOS-Memory/contents/{path}
  → returns file content (base64) + sha

PUT /repos/AyushPoo/FounderOS-Memory/contents/{path}
  body: {
    "message": "auto update from n8n",
    "content": "<base64 encoded new content>",
    "sha": "<current sha>"
  }
```

**Credential:** GitHub PAT stored in n8n as `GitHub PAT - FounderOS Memory` (id: XsVpsC29vOaYW9oc)

## Laptop → GitHub Sync (Already Working)
The `autosync.bat` file in your vault root:
```bat
cd /d F:\Work\FounderOS
git add .
git commit -m "vault auto update %date% %time%"
git push origin main
```
n8n pushes go the other direction: n8n → GitHub API → pulled by Obsidian Git plugin.
