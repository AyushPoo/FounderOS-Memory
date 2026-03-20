# 🧰 Skill Registry

## What Are Skills?
Skills are markdown files (SKILL.md) from cloned GitHub repos that teach AI agents how to build specific types of things. They contain patterns, best practices, and instructions.

## Installed Skill Repos on VM

| Repo | Path | Status | Skills Count |
|------|------|--------|--------------|
| everything-claude-code | `/home/ayushpoojary1/founder-os/skills/everything-claude-code/skills/` | ✅ Installed | 108 |
| superpowers | `/home/ayushpoojary1/founder-os/skills/superpowers/skills/` | ✅ Installed | 14 |
| ui-ux-pro-max-skill | `/home/ayushpoojary1/founder-os/skills/ui-ux-pro-max-skill/` | ✅ Installed | Design system generator |
| cline | `/home/ayushpoojary1/founder-os/skills/cline/` | ✅ Pre-existing | — |

## Product Type → Skill Mapping

| Product Type | Primary Skill Source | Skills to Use |
|-------------|---------------------|---------------|
| web_app | superpowers + ui-ux-pro-max | brainstorming → writing-plans → search.py (design system) → executing-plans → TDD |
| excel/template | everything-claude-code | documentation, planning |
| extension | everything-claude-code + superpowers | web-development, writing-plans, code-review |
| script | everything-claude-code + superpowers | planning, writing-plans, code-review |
| landing_page | ui-ux-pro-max | search.py --domain product → design system → build |
| dashboard | ui-ux-pro-max + superpowers | search.py --domain product → brainstorming → writing-plans → build |

## 🎨 UI-UX Pro Max — Design System Generator

**Location:** `/home/ayushpoojary1/founder-os/skills/ui-ux-pro-max-skill/`

**⚠️ MANDATORY: Run this BEFORE building any UI/frontend.**

### Search Commands
```bash
cd /home/ayushpoojary1/founder-os/skills/ui-ux-pro-max-skill

# Product type recommendations
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain product

# UI styles
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain style

# Typography
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain typography

# Color palettes
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain color

# Landing page patterns
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain landing

# Full design system
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain product --design-system
```

Domains: `product`, `style`, `typography`, `color`, `landing`, `chart`, `ux`
Stacks: `html-tailwind`, `react`, `nextjs`, `astro`, `vue`, `nuxtjs`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`

## 🦸 Superpowers — Planning & TDD Framework

**Location:** `/home/ayushpoojary1/founder-os/skills/superpowers/skills/`

### Available Skills (14)
| Skill | When to Use |
|-------|------------|
| brainstorming | First step — refine idea through questions before any code |
| writing-plans | Break work into 2-5 min tasks with file paths + verification |
| executing-plans | Follow the plan, implement step by step |
| subagent-driven-development | Dispatch fresh agent per task with 2-stage review |
| test-driven-development | RED → GREEN → REFACTOR cycle (enforced) |
| systematic-debugging | 4-phase root cause analysis |
| requesting-code-review | Review against plan, block on critical issues |
| receiving-code-review | How to handle feedback |
| finishing-a-development-branch | Merge/PR/discard decision |
| dispatching-parallel-agents | Run multiple agents simultaneously |
| verification-before-completion | Evidence over claims — verify before declaring done |
| using-git-worktrees | Parallel branches without stashing |
| using-superpowers | Meta: how the framework works |
| writing-skills | Create new skills for the framework |

### Build Workflow Order
1. **brainstorming** → Refine the idea
2. **writing-plans** → Create implementation plan
3. **UI-UX Pro Max search.py** → Generate design system (if UI involved)
4. **executing-plans** → Build it
5. **test-driven-development** → Verify it works
6. **requesting-code-review** → Quality check
7. **finishing-a-development-branch** → Ship it

## 📚 Everything Claude Code (108 Skills)

**Location:** `/home/ayushpoojary1/founder-os/skills/everything-claude-code/skills/`

Full list: see individual skill folders. Key ones for Founder Systems:
- `agentic-engineering`, `ai-first-engineering`
- `web-development`, `frontend-patterns`
- `api-design`, `backend-patterns`
- `security-review`, `coding-standards`
- `data-scraper-agent`, `deep-research`, `market-research`
- `content-engine`, `article-writing`
- `investor-materials`, `investor-outreach`

## How the Product Builder Should Use Skills

1. Receive idea + product type from plan
2. Look up Product Type → Skill Mapping (above)
3. **If UI involved:** Run UI-UX Pro Max search.py FIRST to get design system
4. **Always:** Run Superpowers brainstorming → writing-plans
5. SSH into VM, read matched SKILL.md files
6. Pass skill content + design system as context to the builder LLM
7. Build using TDD workflow
8. Run verification-before-completion

## Improvement Ideas
- Embed skills into Mem0 for semantic search
- Track which skills produce successful builds
- Add custom Founder Systems-specific skills over time
- Auto-detect product type from idea description