# 🌐 Builder - Web App

## Overview
Receives a build plan from [[Product Builder]] and generates complete working code for a Next.js web application using GPT 5.3.

## Configuration
- **Workflow ID:** xiYFZhlToYLX9g4J
- **Trigger:** Webhook POST to `/webhook-test/builder-webapp`
- **LLM:** GPT 5.3 (Azure OpenAI)
- **Status:** ❌ INACTIVE + BROKEN

## Pipeline
1. Receive plan via webhook (product_name, tagline, features, tech stack, file structure)
2. Send to GPT 5.3 with code generation prompt
3. GPT returns JSON with complete file contents
4. Respond to webhook with generated files

## Code Generation Prompt
Instructs GPT 5.3 to:
- Use Next.js 14 with App Router
- TypeScript
- Tailwind CSS
- Mobile responsive
- Error handling + loading states
- Complete README with setup instructions

### Output Format
```json
{
  "files": [
    {"path": "README.md", "content": "..."},
    {"path": "package.json", "content": "..."},
    {"path": "app/page.tsx", "content": "..."},
    {"path": "app/layout.tsx", "content": "..."},
    {"path": "app/globals.css", "content": "..."},
    {"path": "next.config.js", "content": "..."}
  ],
  "buildNotes": "Implementation notes"
}
```

## Bugs (Must Fix)
- [ ] **URL malformed** — has "Headers:" appended to the end
- [ ] **HTTP headers wrong** — Content-Type is in name field, API key label is wrong
- [ ] **Uses `/webhook-test/`** — only works in test mode, not production
- [ ] **Workflow is INACTIVE** — won't receive webhook calls
- [ ] **No deployment step** — generates code but doesn't write to disk, push to GitHub, or deploy
- [ ] **No connection to Antigravity** — can't deploy to website

## Missing Steps (TODO)
- [ ] Write generated files to VM disk
- [ ] Push to GitHub repo
- [ ] Trigger Antigravity/Vercel deployment
- [ ] Notify Ayush via Telegram on completion
- [ ] Log the build to Obsidian
