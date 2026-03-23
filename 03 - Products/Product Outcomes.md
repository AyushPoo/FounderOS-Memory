# Product Outcomes

> Last updated: 2026-03-23 by co-founder agent

## Shipped Products

| Product | Type | Live URL | Status |
|---------|------|----------|--------|
| Pomodoro Timer | Web App (HTML) | https://foundersystems.in/tools/pomodoro-timer/ | Live |
| Startup Cost Calculator | Web App (HTML) | https://foundersystems.in/tools/startup-cost-calculator/ | Live |

## Deployment Pipeline (LIVE as of 2026-03-23)

```
OpenCode builds product
      |
      v
~/products/<name>/index.html  (Azure VM)
      |
      v
~/founder-os/builder/deploy.sh <name>
      |
      v
GitHub: AyushPoo/Founder-Systems
public/tools/<name>/index.html
      |
      v
Vercel auto-deploy (~60 seconds)
      |
      v
https://foundersystems.in/tools/<name>/
```

## How To Deploy a New Product
```bash
ssh ayush@20.193.252.82
~/founder-os/builder/deploy.sh <product-folder-name>
```
Or Atlas can run this via ssh_azure tool.

## Next Steps
- Add products to the foundersystems.in catalog page (ProductDetail.jsx)
- Set up Gumroad/payment links for new tools
- Automate deploy.sh call at end of every build
