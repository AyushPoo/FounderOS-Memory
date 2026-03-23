# Product Outcomes

> Last updated: 2026-03-23 by co-founder agent

## Shipped Products

| Product | Type | Status | Location | Notes |
|---------|------|--------|----------|-------|
| Pomodoro Timer | Web App (HTML) | Shipped | Azure: products/pomodoro-timer/index.html | Static HTML, served on port 3000 |
| Startup Cost Calculator | Web App (HTML) | Shipped | Azure: products/startup-cost-calculator/index.html | Static HTML, served on port 3000 |

## Pipeline Status

```
Idea (Google Sheets)
    |
    v
Product Builder (n8n) -- GPT-5.3 plan
    |
    v
OpenCode (Azure) -- code generation
    |
    v
products/ on Azure VM  <-- HERE currently
    |
    x  (NO DEPLOYMENT PIPELINE YET)
    |
    v
foundersystems.in  <-- TARGET
```

## Next: Deployment Pipeline
The main gap is getting products from `Azure:products/` onto `foundersystems.in` automatically.
