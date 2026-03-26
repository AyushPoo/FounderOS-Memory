# 🗺️ Founder Systems — Production Roadmap
_Last updated: 2026-03-26_

Full pipeline: **Idea → Approval → Plan → Build → Deploy → Market → Track**

---

## 🔴 PHASE 1 — Fix What's Broken (Blockers)

- [x] **Fix Google Sheets OAuth** — credential expired (EAUTH), re-auth in n8n UI
  - Affects: Ideas Fetcher "Clear sheet" node, Save Idea workflow
- [x] **Fix Atlas crash loop** — founder-agent still showing 50+ restarts, needs root cause
- [x] **Fix memory-server restarts** — 62 restarts on GCP, investigate cause
- [ ] **Fix "Suggest Changes" button** — Product Builder has the button but no branch handling it in n8n
- [x] **Fix Builder - Web App workflow** — fixed malformed URL + wrong header name, re-activated (2026-03-26)

---

## 🟡 PHASE 2 — Complete the Core Pipeline

### 2A · Ideas → Fetch → Select
- [ ] Confirm Ideas Fetcher scrapes all sources: ProductHunt, HN, IndieHackers, Reddit, GitHub Trending
- [ ] Ideas ranked and sent to Telegram with selection buttons (Yes / No / Details)
- [ ] "Get Idea Details" gives full breakdown when requested
- [ ] "Save Idea" saves to Google Sheets reliably (needs Sheets fix first)

### 2B · Plan → Skills → Approve
- [ ] Product Builder receives selected idea and auto-selects relevant skills from the skills library
- [ ] GPT-5.3 generates a detailed product plan (features, stack, file structure)
- [ ] Plan sent to Telegram with: **Approve / Suggest Changes / Reject**
- [ ] "Suggest Changes" flow: Ayush gives feedback → plan revised → re-sent for approval
- [ ] Plan stored in Obsidian under `06 - Products/[ProductName]/plan.md`

### 2C · Build — All Product Types
Currently only web apps are attempted. Need builders for ALL types:

- [ ] **Web App builder** — Next.js / static HTML (fix existing broken workflow)
- [ ] **Chrome Extension builder** — manifest.json, popup, background script, content script
- [ ] **Excel / Google Sheets template builder** — formulas, structure, sample data (via Python openpyxl)
- [ ] **PowerPoint / Google Slides builder** — python-pptx or similar
- [ ] **Notion template builder** — exported .zip or Notion API duplication link
- [ ] **Script / CLI tool builder** — Python or Node, packaged with README
- [ ] **PDF / eBook builder** — markdown → PDF (pandoc or similar)
- [ ] Each builder: receives plan → generates all files → saves to Azure `/products/[name]/`

### 2D · Quality Gate
- [ ] After build: auto-check that all files are present and non-empty
- [ ] For web apps: lint check (ESLint / basic HTML validator)
- [ ] Summary report sent to Telegram: files created, any errors
- [ ] Ayush gets **Deploy / Fix / Reject** buttons

---

## 🟠 PHASE 3 — Deployment

### 3A · GitHub
- [ ] Auto-create GitHub repo under AyushPoo account
- [ ] Push all product files to repo
- [ ] Add README auto-generated from plan
- [ ] Tag release v1.0.0

### 3B · Website (foundersystems.in)
- [ ] Audit current website structure — how existing product pages are built
- [ ] Build page generator: takes product name, description, price, screenshots → generates matching page
- [ ] Auto-deploy new page to foundersystems.in via GitHub push + CI/CD
- [ ] Page follows the same layout/style as existing products on the site

### 3C · Sales Platforms
- [ ] **Gumroad** — auto-create product listing via Gumroad API (name, description, price, files)
- [ ] **LemonSqueezy** — auto-create product via LemonSqueezy API
- [ ] **Instamojo** — auto-create product listing (check if API available, else flag for manual)
- [ ] All 3 listings: consistent title, description, pricing, product files uploaded
- [ ] Links to all 3 stores saved in Obsidian product page

---

## 🟢 PHASE 4 — Marketing

### 4A · Content Generation
- [ ] Auto-generate platform-specific posts from product plan:
  - **Twitter/X** — short punchy thread (3-5 tweets), hook + features + CTA + link
  - **Reddit** — long-form post for relevant subreddits (r/SideProject, r/entrepreneur, r/indiehackers, r/tools, niche subreddits based on product)
  - **Product Hunt** — tagline, description, first comment, maker comment
  - **Hacker News** — "Show HN" post text
  - **LinkedIn** — professional angle post
  - **IndieHackers** — milestone post format

### 4B · Auto-Posting (or Approval Queue)
- [ ] Posts sent to Telegram for review with **Post Now / Edit / Skip** per platform
- [ ] Auto-post to Twitter via API after approval
- [ ] Auto-post to Reddit via API after approval
- [ ] Product Hunt and HN: manual post (platform rules), but content ready to copy-paste
- [ ] All posts + links logged in Obsidian

---

## 🔵 PHASE 5 — Analytics Dashboard

### 5A · Data Collection (per product)
- [ ] Gumroad: sales count, revenue, conversion rate (via API)
- [ ] LemonSqueezy: same (via API)
- [ ] Instamojo: same (via API or manual)
- [ ] GitHub: stars, forks, clones (via GitHub API)
- [ ] Website: page views, time on page (Google Analytics or Plausible)
- [ ] Twitter: impressions, likes, retweets, link clicks (via API)
- [ ] Reddit: upvotes, comments, link clicks

### 5B · Dashboard
- [ ] Build web dashboard (analytics.foundersystems.in or page on site)
- [ ] Shows: all products, revenue per product, total revenue, traffic, best performers
- [ ] Auto-refreshes via cron (daily pull from all APIs)
- [ ] Weekly summary sent to Telegram every Monday morning

### 5C · Learning Loop
- [ ] Track which idea categories perform best
- [ ] Feed top performers back into Ideas Fetcher ranking weights
- [ ] Atlas stores learnings in Mem0/Qdrant for future planning decisions

---

## ⚙️ PHASE 6 — Infrastructure & Reliability

- [ ] Set up proper CI/CD (GitHub Actions) for all deployments
- [ ] Atlas crash loop permanently fixed + auto-restart with alerting
- [ ] memory-server stability fix
- [ ] All n8n workflows have error handlers — failures send alert to Telegram
- [ ] Daily backup of n8n workflows to GitHub
- [ ] Monitoring: uptime checks on all PM2 processes, alert if any go down
- [ ] Secrets management — move all API keys to proper env files, not hardcoded
- [ ] Document all API keys and where they're stored (internal doc, not public)

---

## 📊 Progress Tracker

| Phase | Status | Blockers |
|-------|--------|----------|
| Phase 1 — Fix broken | 🟡 In progress (4/5 done) | — |
| Phase 2 — Core pipeline | 🟡 Partial | Sheets auth, broken builder |
| Phase 3 — Deployment | 🔴 Not started | Need pipeline working first |
| Phase 4 — Marketing | 🔴 Not started | Need deployment working |
| Phase 5 — Analytics | 🔴 Not started | Need products live first |
| Phase 6 — Infrastructure | 🟡 Partial | Atlas crashes, memory-server |

---

## 🔑 Architecture Notes
- **@Rayquabot** (n8n) = main FounderOS flow (ideas → plan → build)
- **@Blasikenbot** (Atlas v3, Azure) = direct builds, brainstorming, autonomous tasks
- **@AzureOCbackupbot** (OpenClaw Azure) = backup when Emergent credits low
- Gemini Flash = cheap bulk work (ideas ranking, summarization)
- GPT-5.3 Azure = quality work (planning, code gen, decisions)
- All products saved to Azure `/products/[name]/` before deploy
- All product data logged in Obsidian under `06 - Products/`
- Do NOT deploy to foundersystems.in without Ayush's explicit approval
