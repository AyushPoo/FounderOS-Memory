# 🌐 BrowserOS → Obsidian Capture

How to save anything from your browser (BrowserOS or regular Chrome) directly into the Obsidian vault.

---

## Method 1: Bookmarklet (Recommended — Works Everywhere)

A bookmarklet is a browser bookmark that runs JavaScript. One click saves the current page to your vault.

### Setup (one time)

1. Copy the code below
2. In Chrome/BrowserOS, create a new bookmark
3. Name it: **💾 Save to Vault**
4. Paste the code as the URL

```javascript
javascript:(function(){
  var title = document.title;
  var url = window.location.href;
  var selection = window.getSelection().toString().trim();
  var date = new Date().toISOString().split('T')[0];
  var time = new Date().toTimeString().split(' ')[0];
  var content = '| ' + date + ' ' + time + ' | [' + title + '](' + url + ') | ' + (selection || '—') + ' |';
  fetch('https://34.14.219.64.nip.io/webhook/update-obsidian', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      file: '05 - Memory/Browser Captures.md',
      action: 'append',
      content: content,
      section: '## Captures'
    })
  }).then(function(){
    alert('✅ Saved to Obsidian vault!');
  }).catch(function(){
    alert('❌ Failed — check n8n is running');
  });
})();
```

### How to Use
1. Navigate to any page in BrowserOS or Chrome
2. **Optional:** Select text you want to save as a note
3. Click the **💾 Save to Vault** bookmark
4. You'll see a ✅ confirmation popup
5. Page is logged to `05 - Memory/Browser Captures.md`

---

## Method 2: BrowserOS Prompt (If BrowserOS Has AI Commands)

If BrowserOS lets you type commands/prompts, use this:

> "Save this page to my Obsidian vault via POST https://34.14.219.64.nip.io/webhook/update-obsidian with file '05 - Memory/Browser Captures.md', action 'append', content '[page title](url) — [your note]'"

---

## Method 3: Via Telegram (Manual)

If you're on mobile or away from your laptop, send to Telegram bot:

```
/save-link [URL] [optional note]
```

(Requires adding a command handler to Founder OS Agent — see `02 - Workflows/Founder OS Agent.md`)

---

## Where Captures Go

File: `05 - Memory/Browser Captures.md`

| Date | Page | Note |
|------|------|------|
| — | — | — |

---

## Status
- [x] Bookmarklet designed
- [ ] Browser Captures.md file created in vault
- [ ] Tested end-to-end in BrowserOS
- [ ] Optional: Add /save-link command to Telegram bot
