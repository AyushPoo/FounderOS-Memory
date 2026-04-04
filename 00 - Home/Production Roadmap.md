# ðºï¸ Founder Systems â Production Roadmap
_Last updated: 2026-04-04_

Full pipeline: **Idea â Approval â Plan â Build â Deploy â Market â Track**

---

## â PHASE 1 â Fix What's Broken (Blockers) â COMPLETE

- [x] **Fix Google Sheets OAuth** â re-authed in n8n UI
- [x] **Fix Atlas crash loop** â fixed bad tool schema + max_tokens param (2026-03-23)
- [x] **Fix memory-server restarts** â GCP VM decommissioned (services moved to Azure)
- [x] **Fix "Suggest Changes" button** â added Is Suggest Changes? node + Request Feedback Telegram node (2026-03-26)
- [x] **Fix Builder - Web App workflow** â fixed malformed URL + wrong header name, re-activated (2026-03-26)

---

## ð¡ PHASE 2 â Complete the Core Pipeline (Partial)

### 2A Â· Ideas â Fetch â Select
- [x] Ideas Fetcher scrapes 9 sources, ranks with Gemini, saves to Google Sheets
- [x] Ideas ranked and sent to Telegram with selection buttons
- [x] "Get Idea Details" gives full breakdown when requested
- [ ] "Save Idea" â verify Google Sheets auth still reliable

### 2B Â· Plan â Skills â Approve
- [x] Product Builder receives selected idea and auto-selects relevant skills
- [x] GPT-5.3 generates detailed product plan via LiteLLM proxy
- [x] Plan sent to Telegram with: **Approve / Suggest Changes / Reject**
- [x] "Suggest Changes" flow working
- [ ] Plan stored in Obsidian under `06 - Products/[ProductName]/plan.md` â not yet wired

### 2C Â· Build â All Product Types
- [x] **Web App builder** â static HTML via OpenCode
- [ ] **Chrome Extension builder**
- [ ] **Excel / Google Sheets template builder**
- [ ] **PowerPoint / Google Slides builder**
- [ ] **Notion template builder**
- [ ] **Script / CLI tool builder**
- [ ] **PDF / eBook builder**

### 2D Â· Quality Gate
- [x] Quality Gate Actions workflow â post-build checks
- [ ] Full lint + validation checks
- [ ] Deploy / Fix / Reject Telegram buttons

---

## â PHASE 3 â Deployment â COMPLETE

### 3A Â· GitHub
- [x] Auto-push product files to AyushPoo/Founder-Systems repo
- [x] GitHub Actions CI/CD (deploy.yml) triggers Vercel on push to main

### 3B Â· Website (foundersystems.in)
- [x] Dynamic product pages via JSON files in public/products/
- [x] New products auto-appear on site without code deploys
- [x] Vercel auto-deploys on GitHub push

### 3C Â· Sales Platforms
- [x] Product Publisher n8n workflow syncs to Gumroad + LemonSqueezy on product JSON push
- [x] GitHub Actions product-sync.yml triggers n8n webhook on products/** changes
- [ ] Instamojo â API not available, manual for now

---

## â PHASE 4 â Marketing â COMPLETE

### 4A Â· Content Generation
- [x] Auto-generate platform-specific posts (Twitter/X, Reddit, LinkedIn)
- [x] Marketing Agent Phase 5 â conversational post brainstorming via Telegram

### 4B Â· Auto-Posting
- [x] 3 marketing workflows live
- [x] Posts sent to Telegram for review with Post Now / Edit / Skip
- [ ] Deep links for mobile approval (plan at docs/superpowers/plans/2026-03-28-mobile-posting-deep-links.md)

---

## â PHASE 5 â Analytics Dashboard â COMPLETE

### 5A Â· Data Collection
- [x] Gumroad + LemonSqueezy sales data (via API)
- [x] Analytics API (port 3001, SQLite) serving data

### 5B Â· Dashboard
- [x] analytics.foundersystems.in (or equivalent) built
- [x] Weekly summary sent to Telegram every Monday morning

### 5C Â· Learning Loop
- [x] Quality Gate Actions + learning loop built
- [x] Atlas stores learnings in Qdrant for future planning

---

## â PHASE 6 â Infrastructure & Reliability â COMPLETE

- [x] GitHub Actions CI/CD for all deployments (deploy.yml + product-sync.yml)
- [x] auto-healer PM2 process â permanently fixes crash loops
- [x] GCP VM decommissioned â all services consolidated on Azure
- [x] All 29 n8n workflows wired to Error Handler â Telegram alerts
- [x] Daily n8n Backup (2AM IST â GitHub)
- [x] Health Monitor (5-min checks on n8n, website, analytics-api)
- [x] Secrets documented in docs/internal/SECRETS-REFERENCE.md

---

## ð Progress Tracker

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 1 â Fix broken | â Complete | All blockers resolved |
| Phase 2 â Core pipeline | ð¡ Partial | Builder types + Obsidian logging still TODO |
| Phase 3 â Deployment | â Complete | GitHub â Vercel + Gumroad/LS sync live |
| Phase 4 â Marketing | â Complete | 3 workflows live + Marketing Agent |
| Phase 5 â Analytics | â Complete | Dashboard + weekly summary live |
| Phase 6 â Infrastructure | â Complete | Error handling, backup, monitoring, CI/CD |

---

## ð Architecture Notes
- **@Rayquabot** (n8n) = main FounderOS pipeline (ideas â plan â build â deploy)
- **@Blasikenbot** (Atlas v3, Azure) = direct builds, brainstorming, autonomous tasks
- Gemini Flash = cheap bulk work (ideas ranking, summarization)
- GPT-5.3 Azure = quality work (planning, code gen, decisions) via LiteLLM port 4000
- All products saved to Azure `/products/[name]/` before deploy
- All product data logged in Obsidian under `03 - Products/`
- Do NOT deploy to foundersystems.in without Ayush's explicit approval
- **No GCP VM** â everything runs on Azure VM (20.193.252.82)
