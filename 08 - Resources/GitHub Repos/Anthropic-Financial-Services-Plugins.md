# Anthropic Financial Services Plugins

**Repo:** https://github.com/anthropics/financial-services-plugins  
**Author:** Anthropic  
**Type:** Claude Code / Claude Cowork plugins for financial services  
**Relevance:** Reference for financial modeling patterns and Excel skill logic

## What It Is
A collection of professional-grade plugins built for enterprise financial analysts using Claude. Contains 41 skills, 38 commands, and 11 MCP integrations covering investment banking, equity research, private equity, and wealth management.

## ⚠️ Important: Compatibility Note
These plugins are in `.claude-plugin` format — designed for **Claude Code** and **Claude Cowork**, NOT for our OpenCode builder or n8n workflows. Do NOT clone to the VM skills folder.

The MCP data connectors (Morningstar, FactSet, Bloomberg, PitchBook, S&P Global) require **paid enterprise subscriptions**.

## Skills Inside — Financial Analysis Plugin
| Skill | What It Does | Relevant For Us? |
|-------|-------------|------------------|
| `dcf-model` | Discounted Cash Flow modeling | ✅ YES — reference for DCF template products |
| `3-statement-model` | Income, Balance Sheet, Cash Flow | ✅ YES — core of our financial models |
| `lbo-model` | Leveraged Buyout modeling | ✅ YES — advanced product idea |
| `comps-analysis` | Comparable company analysis | ✅ YES — useful for B2B SaaS model |
| `competitive-analysis` | Market & competitor research | ✅ YES — useful for idea evaluation |
| `audit-xls` | Audit Excel spreadsheets for errors | ✅ YES — quality check for our templates |
| `clean-data-xls` | Clean and normalize Excel data | ✅ YES — utility for templates |
| `deck-refresh` | Refresh PowerPoint decks with new data | 🟡 Maybe — if we build pitch deck tools |
| `ib-check-deck` | QC investment banking presentations | ❌ Enterprise only |
| `ppt-template-creator` | Create branded PowerPoint templates | 🟡 Maybe — future product idea |

## Other Plugins
| Plugin | Focus | Relevant? |
|--------|-------|----------|
| `investment-banking` | CIMs, teasers, merger models | ❌ Enterprise |
| `equity-research` | Earnings reports, coverage initiation | ❌ Enterprise |
| `private-equity` | Deal sourcing, IC memos, portfolio KPIs | ❌ Enterprise |
| `wealth-management` | Client reports, portfolio rebalancing | 🟡 Maybe — future wealth tool |

## How to Use This (For Founder Systems)
**DO NOT install as a skill.** Instead, use as a reference when building financial products:

1. **Building a new financial model template?** Read the `dcf-model` or `3-statement-model` skill logic for industry-standard structure and formulas
2. **Adding audit features to a template?** Reference `audit-xls` for common error checks
3. **Building a competitor analysis tool?** Reference `competitive-analysis` skill patterns
4. **Evaluating a financial product idea?** Check this repo for prior art and complexity signals

## How to Read the Skills
Each skill is a markdown file with:
- Task description
- Step-by-step instructions for Claude
- Output format expectations
- Quality checks

Direct URL pattern: `https://github.com/anthropics/financial-services-plugins/blob/main/financial-analysis/skills/<skill-name>/SKILL.md`

## Tags
#finance #excel #templates #reference #dcf #modeling #financial-analysis