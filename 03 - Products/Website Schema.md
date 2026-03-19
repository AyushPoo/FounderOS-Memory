# 🌐 foundersystems.in — Website Schema

> The complete structure, product catalog, positioning, and marketplace presence of the Founder Systems website.
> Keep this updated whenever products are added, prices change, or new marketplaces are added.

---

## Tech Stack
- **Framework:** React + Vite
- **Styling:** Tailwind CSS
- **Deployment:** Vercel
- **Repo:** `AyushPoo/Founder-Systems` (GitHub)
- **Domain:** foundersystems.in

---

## Brand Positioning

**Tagline:** "Build faster with proven systems."
**Sub-headline:** "Practical tools, templates, and systems for founders and operators."

**Brand identity:**
- Bold, high-contrast design (black, cream, orange)
- Anti-corporate tone — direct, punchy copywriting
- Speaks to non-technical founders who want leverage, not complexity
- Heavy emphasis on ROI framing ("save 40 hours", "stop guessing your runway")
- Target audience: seed/Series A founders, indie hackers, startup operators

**Three product pillars (from Toolkit section):**
1. **Finance** — SaaS financial models, forecasting tools
2. **Operations** — Workflows for efficiency
3. **Strategy** — Investor CRM templates, pitch decks

---

## Site Structure

| Route | Page | Purpose |
|-------|------|---------|
| `/` | Home | Hero + Toolkit section |
| `/products` | Products Catalog | Grid of active + coming soon products |
| `/products/:id` | Product Detail | Full sales page per product |
| `/about` | About | Ayush's story + credibility |
| `/download` | Download | Post-purchase delivery page |
| `/access` | Access Purchase | Repurchase/access recovery |
| `/terms` | Terms | Legal |
| `/refund-policy` | Refund Policy | Legal |
| `/privacy-policy` | Privacy Policy | Legal |

---

## Live Products

All product data is hardcoded in `src/pages/ProductDetail.jsx`.

### FS001 — SaaS Financial Model Template
- **ID:** `saas-financial-model`
- **Full title:** "The 10-Minute SaaS Financial Model"
- **Subtitle:** "Stop Guessing Your Runway. Start Winning Your Pitch."
- **Category:** Finance
- **Price:** ₹1,499 / $20 (original: ₹1,999 / $25)
- **What it is:** Investor-ready SaaS model with MRR/ARR dashboards, LTV/CAC, valuation engine (ARR multiples + DCF), sensitivity analysis
- **For:** SaaS founders raising seed, indie hackers, analysts
- **Gumroad:** https://ayushpoojary.gumroad.com/l/saas-investor-model
- **Instamojo:** https://ayushpoojary.myinstamojo.com/product/the-10-minute-saas-financial-model/
- **LemonSqueezy:** https://ayushpoojary.lemonsqueezy.com/checkout/buy/9509df15-9420-4761-a668-bdb525b4b838

### FS002 — Advanced B2B SaaS Model
- **ID:** `advanced-saas-model`
- **Full title:** "The Pro-Grade B2B SaaS Financial Model (Advanced Edition)"
- **Subtitle:** "Stop Guessing Your Unit Economics. Start Raising Like a Pro."
- **Category:** Finance
- **Price:** ₹2,499 / $30 (original: ₹2,999 / $35)
- **What it is:** Heavy-duty model with automated cohort analysis, NRR, Burn Multiple, Magic Number, top-quartile SaaS benchmarks, dual valuation (ARR + DCF), sensitivity engine
- **For:** Seed/Series A founders, VC due diligence prep
- **Gumroad:** https://ayushpoojary.gumroad.com/l/advanced-saas-financial-model
- **Instamojo:** https://ayushpoojary.myinstamojo.com/product/the-founder-grade-saas-financial-model/
- **LemonSqueezy:** https://ayushpoojary.lemonsqueezy.com/checkout/buy/aac3b6c7-fbbc-435d-a02c-c5297adf37d1

### FS003 — Marketplace Financial Model
- **ID:** `marketplace-financial-model`
- **Full title:** "The Investor-Ready Marketplace Financial Model"
- **Subtitle:** "Stop Mixing Up GMV and Net Revenue. Start Raising Like a Pro."
- **Category:** Finance
- **Price:** ₹1,999 / $25 (original: ₹2,499 / $30)
- **What it is:** Dual-sided supply/demand growth model, GMV waterfall, marketplace benchmarks (Take Rate, Buyer-to-Seller Ratio), Base/Bull/Bear scenarios, triple valuation (GMV multiples + Net Rev multiples + DCF)
- **For:** Two-sided marketplace founders (B2B or B2C) raising seed/Series A
- **Gumroad:** https://ayushpoojary.gumroad.com/l/marketplace-financial-model
- **Instamojo:** https://ayushpoojary.myinstamojo.com/product/the-investor-ready-marketplace-financial-mod/
- **LemonSqueezy:** https://ayushpoojary.lemonsqueezy.com/checkout (not set up yet)

### FS004 — D2C & Ecommerce Financial Model
- **ID:** `d2c-ecommerce-model`
- **Full title:** "The Investor-Ready D2C & Ecommerce Financial Model"
- **Subtitle:** "Stop Guessing Your ROAS. Start Scaling Profitably."
- **Category:** Finance
- **Price:** ₹1,999 / $25 (original: ₹2,499 / $30)
- **What it is:** Multi-channel growth engine (D2C + subscriptions + bundles + wholesale), 36-month cohort retention, inventory cash flow planner with reorder forecasting, D2C benchmarks, dual valuation
- **For:** D2C/ecommerce founders raising or debt financing
- **Gumroad:** https://ayushpoojary.gumroad.com/l/sbdyuh
- **Instamojo:** https://ayushpoojary.myinstamojo.com/product/the-investor-ready-d2c-ecommerce-financial-m/
- **LemonSqueezy:** https://ayushpoojary.lemonsqueezy.com/checkout/buy/673d59d1-6f5a-48fc-adde-d939a8ee1d6a

---

## Coming Soon Products

| ID | Name | Category | Description |
|----|------|----------|-------------|
| cs-1 | Investor CRM | Strategy | Manage fundraising pipelines and investor updates |
| cs-2 | Founder Dashboard | Operations | Centralized operating system for daily startup metrics |
| cs-3 | Startup Budget Planner | Finance | Allocate resources and track operational spend |
| cs-4 | LinkedIn Summarizer | Operations | Automated extraction of insights from profiles |

---

## Payment & Checkout Architecture

### Primary: Razorpay
- **Key:** `rzp_live_SNdUB2ZDVSnOgi`
- **Geo-detection:** Auto-detects India via `Asia/Kolkata` timezone → shows ₹ price and INR checkout
- **International:** USD checkout for everyone else
- **Flow:** Buy button → email capture modal → Razorpay popup → payment → redirect to `/download`
- **Fallback URL:** https://rzp.io/rzp/aig9tmBT

### Alternate Marketplaces
All products are also listed on:

| Platform | Ayush's Profile | Notes |
|----------|----------------|-------|
| **Gumroad** | ayushpoojary.gumroad.com | All 4 products listed |
| **Instamojo** | ayushpoojary.myinstamojo.com | All 4 products listed (India-focused) |
| **LemonSqueezy** | ayushpoojary.lemonsqueezy.com | 3 of 4 listed (FS003 URL missing) |

### Key Insight for Marketing/Analytics
- **India traffic** → Razorpay INR or Instamojo (familiar, local)
- **International traffic** → Razorpay USD, Gumroad, or LemonSqueezy
- Each marketplace is an independent traffic/discovery source AND a checkout option
- Need to track which marketplace drives the most conversions (currently no unified analytics)

---

## Hardcoded Data — Known Limitation

All product data (titles, descriptions, prices, checkout URLs) is **hardcoded** in `src/pages/ProductDetail.jsx`.

**What this means for the AI pipeline:**
- Adding a new product = manually editing `ProductDetail.jsx` and `Products.jsx`
- No CMS, no database, no API
- Future goal: move product data to a JSON/CMS so the pipeline can auto-add products

---

## Important Files in Repo

| File | Purpose |
|------|---------|
| `src/pages/ProductDetail.jsx` | ALL product data lives here (hardcoded PRODUCTS_DATA object) |
| `src/pages/Products.jsx` | Product catalog + coming soon list (also hardcoded) |
| `src/utils/checkout.js` | Razorpay logic + geo-detection |
| `src/components/Hero.jsx` | Homepage hero section |
| `src/components/Toolkit.jsx` | Homepage toolkit section (Finance/Ops/Strategy) |
| `src/components/Navbar.jsx` | Nav: Toolkit, Products, Access Purchase, About |
| `vercel.json` | Vercel deployment config |
| `.github/workflows/log-to-obsidian.yml` | Auto-logs deploys to vault |
