# 🔄 Auto Update System

How Obsidian gets automatically updated from n8n, the VM, and AI tools.

## Architecture

```
n8n workflows          → webhook → [Obsidian Updater Workflow] → GitHub API → vault
VM events              → SSH → n8n → GitHub API → vault  
Telegram conversations → Founder OS Agent → GitHub API → vault
ChatGPT/Claude/BrowserOS → manual paste OR browser extension → vault
```

## The Obsidian Updater Workflow (TO BUILD)

A new n8n workflow that:
1. Receives a POST webhook: `POST /webhook/update-obsidian`
2. Body format:
```json
{
  "file": "06 - Logs/n8n/n8n Execution Log.md",
  "action": "append",
  "content": "| 2026-03-18 10:30 | Ideas Fetcher | ✅ Success | Fetched 7 ideas |",
  "section": "## Recent Executions"
}
```
3. Fetches current file from GitHub API
4. Appends/updates content
5. Commits back to GitHub

### Webhook Actions
- `append` — add to end of file or below a section header
- `update_table` — add a row to a markdown table
- `overwrite` — replace entire file content
- `create` — create a new file

## What Should Auto-Update

### When Ideas Are Fetched
- Append to `03 - Products/Saved Ideas.md` when "save X" is triggered
- Log to `06 - Logs/n8n/n8n Execution Log.md`

### When Product Builder Runs
- Create `03 - Products/In Progress/[product-name].md` with the full build plan
- Log to `06 - Logs/n8n/n8n Execution Log.md`

### When a Product Is Built
- Move from In Progress to `03 - Products/Shipped/[product-name].md`
- Add to Dashboard status

### When Errors Occur
- Append to `06 - Logs/Errors/Error Log.md`

### When VM Health Changes
- Update `01 - Architecture/VM Status.md`

## GitHub API Approach

Use GitHub Contents API — no need for git CLI:

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

**GitHub Token needed:** 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

## Status
- [ ] Build Obsidian Updater Workflow in n8n
- [ ] Connect Ideas Fetcher → update vault on new batch
- [ ] Connect Save Idea → log to Saved Ideas
- [ ] Connect Product Builder → log build plans
- [ ] Connect Builder - Web App → log completions/errors
- [ ] Set up Windows autosync (autosync.bat already exists for laptop → GitHub)

## Laptop → GitHub Sync (Already Working)
The `autosync.bat` file in your vault root:
```bat
cd /d F:\Work\FounderOS
git add .
git commit -m "vault auto update %date% %time%"
git push origin main
```
Run this on a schedule via Windows Task Scheduler to push your local changes.
n8n pushes go the other way: n8n → GitHub API → pulled by Obsidian Git plugin.
