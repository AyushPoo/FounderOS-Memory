# ð Auto Update System

How Obsidian gets automatically updated from n8n, the VM, and AI tools.

## Architecture

```
n8n workflows          â webhook â [Obsidian Updater Workflow] â GitHub API â vault  â LIVE
Website GitHub pushes  â GitHub Action â GitHub API â vault                          â LIVE
BrowserOS/Chrome       â JS bookmarklet â webhook â GitHub API â vault               â READY
LLM sessions           â tell OpenClaw â webhook â GitHub API â vault                â LIVE
OpenClaw sessions      â auto-logged by OpenClaw â webhook â GitHub API â vault      â LIVE
Telegram conversations â Founder OS Agent â (optional /log-session command)          ð² Optional
```

## The Obsidian Updater Workflow â LIVE

**Workflow ID:** Yg8BWmxKQuCHkn2k
**Webhook:** `POST https://n8n.foundersystems.in/webhook/update-obsidian`
**Status:** Active â (running on Azure VM â GCP VM decommissioned 2026-04-04)

### Request Format
```json
{
  "file": "06 - Logs/n8n/n8n Execution Log.md",
  "action": "append",
  "content": "| 2026-03-19 13:30 | Ideas Fetcher | â Success | Fetched 7 ideas |",
  "section": "## Recent Executions"
}
```

### Supported Actions
- `append` â add to end of file or below a section header
- `update_table` â add a row to a markdown table (alias for append)
- `overwrite` â replace entire file content
- `create` â create a new file

## Connection Status

| Connection | Status | Notes |
|------------|--------|-------|
| n8n â Obsidian | â Live | Obsidian Updater workflow active |
| Ideas Fetcher â Obsidian | â Wired | Logs to n8n Execution Log |
| Save Idea â Obsidian | â Wired | Logs to Saved Ideas.md |
| Product Builder â Obsidian | â Wired | Logs build events |
| Antigravity/Website â Obsidian | ð² Not built | GitHub Action needed |
| BrowserOS â Obsidian | ð² Not built | Bookmarklet/paste flow |
| LLM Conversations â Obsidian | ð² Not built | Manual paste via OpenClaw |

## GitHub API Approach

Uses GitHub Contents API â no git CLI needed:

```
GET /repos/AyushPoo/FounderOS-Memory/contents/{path}
  â returns file content (base64) + sha

PUT /repos/AyushPoo/FounderOS-Memory/contents/{path}
  body: {
    "message": "auto update from n8n",
    "content": "<base64 encoded new content>",
    "sha": "<current sha>"
  }
```

**Credential:** GitHub PAT stored in n8n as `GitHub PAT - FounderOS Memory` (id: XsVpsC29vOaYW9oc)

## Laptop â GitHub Sync (Already Working)
The `autosync.bat` file in your vault root:
```bat
cd /d F:\Work\FounderOS
git add .
git commit -m "vault auto update %date% %time%"
git push origin main
```
n8n pushes go the other direction: n8n â GitHub API â pulled by Obsidian Git plugin.
