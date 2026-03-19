# 🛒 Marketplace Presence

Where Founder Systems products are listed, how each platform fits the strategy, and what to track for marketing + analytics.

---

## Platform Overview

| Platform | Role | Audience | Currency | Status |
|----------|------|----------|----------|--------|
| **foundersystems.in** | Primary storefront | Direct traffic, SEO | INR + USD | ✅ Live |
| **Gumroad** | Discovery + checkout | International indie founders | USD | ✅ Live (all 4) |
| **Instamojo** | India-focused checkout | Indian founders | INR | ✅ Live (all 4) |
| **LemonSqueezy** | Discovery + checkout | International | USD | ⚠️ Live (3 of 4 — FS003 URL missing) |
| **Razorpay** | Payment processor | India + International | INR + USD | ✅ Live (embedded in site) |

---

## Platform Details

### Gumroad
- **Profile:** https://ayushpoojary.gumroad.com
- **Audience:** International indie hackers, makers, small founders
- **Strength:** Built-in discovery, newsletter, followers, product ratings
- **Revenue share:** ~10% fee
- **Analytics available:** Sales, views, conversion rate per product
- **Products:**
  - FS001: https://ayushpoojary.gumroad.com/l/saas-investor-model
  - FS002: https://ayushpoojary.gumroad.com/l/advanced-saas-financial-model
  - FS003: https://ayushpoojary.gumroad.com/l/marketplace-financial-model
  - FS004: https://ayushpoojary.gumroad.com/l/sbdyuh

### Instamojo
- **Profile:** https://ayushpoojary.myinstamojo.com
- **Audience:** Indian founders and operators (INR payments, UPI, cards)
- **Strength:** India-native, UPI support, familiar to Indian buyers
- **Revenue share:** ~2-3% + gateway fees
- **Analytics available:** Sales, payment methods
- **Products:**
  - FS001: https://ayushpoojary.myinstamojo.com/product/the-10-minute-saas-financial-model/
  - FS002: https://ayushpoojary.myinstamojo.com/product/the-founder-grade-saas-financial-model/
  - FS003: https://ayushpoojary.myinstamojo.com/product/the-investor-ready-marketplace-financial-mod/
  - FS004: https://ayushpoojary.myinstamojo.com/product/the-investor-ready-d2c-ecommerce-financial-m/

### LemonSqueezy
- **Profile:** https://ayushpoojary.lemonsqueezy.com
- **Audience:** International, SaaS/indie community
- **Strength:** Clean UX, good for digital products, Merchant of Record (handles VAT/tax)
- **Revenue share:** ~5% + gateway fees
- **Analytics available:** Sales dashboard, revenue, refunds
- **Products:**
  - FS001: https://ayushpoojary.lemonsqueezy.com/checkout/buy/9509df15-9420-4761-a668-bdb525b4b838
  - FS002: https://ayushpoojary.lemonsqueezy.com/checkout/buy/aac3b6c7-fbbc-435d-a02c-c5297adf37d1
  - FS003: ❌ URL not set up yet
  - FS004: https://ayushpoojary.lemonsqueezy.com/checkout/buy/673d59d1-6f5a-48fc-adde-d939a8ee1d6a

### Razorpay (embedded in site)
- **Key:** `rzp_live_SNdUB2ZDVSnOgi`
- **Role:** Primary checkout on foundersystems.in — not a marketplace, just payment processing
- **Geo-detection:** India (Asia/Kolkata timezone) → INR; everyone else → USD
- **Post-purchase:** Redirects to `/download` page with payment ID

---

## Positioning Per Platform

The same product, but framed slightly differently by platform context:

| Platform | Buyer mindset | How to position |
|----------|--------------|-----------------|
| Gumroad | "I'm a builder looking for tools" | Community, maker credibility, "built by a founder for founders" |
| Instamojo | "I need a trusted Indian seller" | Local trust, INR pricing front-and-centre, CA background |
| LemonSqueezy | "I want a clean, professional product" | Clean UX, international framing, professional copy |
| Direct site | "I found this via SEO or word of mouth" | Full brand experience, all product details, social proof |

---

## Analytics Gap (Current State)

Right now there is **no unified view** of sales across platforms. Each platform has its own dashboard.

### What we're missing:
- Which platform drives the most sales?
- Which product converts best on which platform?
- What's the geographic split (India vs international)?
- Which marketing channel → which platform → which sale?

### Future: Unified Analytics
When the marketing system is built, connect:
1. **UTM tracking** on all external links → Google Analytics / Plausible on foundersystems.in
2. **Webhook/API pulls** from Gumroad, LemonSqueezy, Instamojo → n8n → Google Sheets or Obsidian log
3. **Sales log** in vault: `06 - Logs/sales/Sales Log.md` (to be created)
4. **Dashboard** in Obsidian or a simple n8n report to Telegram

### Platforms with webhook/API support:
- **Gumroad:** ✅ Has webhooks (sale, refund, subscription events)
- **LemonSqueezy:** ✅ Has webhooks (order.created, order.refunded)
- **Instamojo:** ✅ Has webhooks/API
- **Razorpay:** ✅ Has webhooks (payment.captured, payment.failed)

---

## Open Tasks

- [ ] Fix LemonSqueezy URL for FS003 (Marketplace Model)
- [ ] Set up UTM tracking on all marketplace product links
- [ ] Connect Gumroad + LemonSqueezy + Instamojo webhooks → n8n → sales log
- [ ] Create `06 - Logs/sales/Sales Log.md` for unified sales tracking
- [ ] Build Telegram sales alert: "New sale: FS002, $30, Gumroad, Germany"
