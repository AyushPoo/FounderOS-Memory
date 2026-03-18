# 🧰 Skill Registry

## What Are Skills?
Skills are markdown files (SKILL.md) from cloned GitHub repos that teach AI agents how to build specific types of things. They contain patterns, best practices, and instructions.

## Source
- **Repo:** everything-claude-code (cloned from GitHub)
- **Location on VM:** `/home/ayushpoojary1/founder-os/skills/everything-claude-code/skills/`
- **Total Skills:** 108 folders

## Product Type → Skill Mapping
From `skill-registry.json` on VM:

| Product Type | Primary Skill | Supporting Skills |
|-------------|---------------|-------------------|
| web_app | web-development.md | code-review, planning |
| excel | documentation.md | — |
| extension | web-development.md | code-review |
| script | planning.md | code-review |

## All Available Skills (108)

### 🌐 Web & Frontend
- frontend-patterns
- nextjs-turbopack
- liquid-glass-design
- frontend-slides
- swiftui-patterns

### 🔧 Backend & API
- api-design
- backend-patterns
- mcp-server-patterns
- bun-runtime

### 🐍 Python
- python-patterns
- python-testing
- django-patterns
- django-security
- django-tdd
- django-verification

### ☕ Java/Kotlin/Spring
- springboot-patterns
- springboot-security
- springboot-tdd
- springboot-verification
- kotlin-patterns
- kotlin-testing
- kotlin-coroutines-flows
- kotlin-exposed-patterns
- kotlin-ktor-patterns
- java-coding-standards
- jpa-patterns
- compose-multiplatform-patterns
- android-clean-architecture

### 🦀 Rust/Go/C++
- rust-patterns
- rust-testing
- golang-patterns
- golang-testing
- cpp-coding-standards
- cpp-testing

### 🐘 PHP/Laravel
- laravel-patterns
- laravel-security
- laravel-tdd
- laravel-verification

### 🐫 Perl
- perl-patterns
- perl-security
- perl-testing

### 🗄️ Database
- postgres-patterns
- clickhouse-io
- database-migrations

### 🤖 AI & Agents
- agentic-engineering
- ai-first-engineering
- ai-regression-testing
- agent-harness-construction
- autonomous-loops
- continuous-agent-loop
- claude-api
- claude-devfleet
- cost-aware-llm-pipeline
- prompt-optimizer
- nanoclaw-repl
- eval-harness

### 🔒 Security & Quality
- security-review
- security-scan
- coding-standards
- plankton-code-quality
- tdd-workflow
- verification-loop
- e2e-testing

### 📦 DevOps & Deployment
- deployment-patterns
- docker-patterns
- dmux-workflows

### 📝 Content & Research
- article-writing
- content-engine
- crosspost
- deep-research
- market-research
- documentation-lookup

### 💼 Business Domain
- carrier-relationship-management
- customs-trade-compliance
- energy-procurement
- inventory-demand-planning
- investor-materials
- investor-outreach
- logistics-exception-management
- production-scheduling
- quality-nonconformance
- returns-reverse-logistics

### 🛠️ Utilities
- blueprint
- configure-ecc
- continuous-learning
- continuous-learning-v2
- content-hash-cache-pattern
- data-scraper-agent
- exa-search
- fal-ai-media
- foundation-models-on-device
- iterative-retrieval
- nutrient-document-processing
- project-guidelines-example
- ralphinho-rfc-pipeline
- regex-vs-llm-structured-text
- search-first
- skill-stocktake
- strategic-compact
- swift-actor-persistence
- swift-concurrency-6-2
- swift-protocol-di-testing
- team-builder
- video-editing
- videodb
- visa-doc-translate
- x-api

## How Skills Are Used
1. [[Product Builder]] SSHes into VM
2. Keyword-matches idea to skill folder names
3. Reads first 100 lines of matched SKILL.md files
4. Passes to GPT 5.3 as context for planning

## Improvement Ideas
- Use skill-registry.json instead of keyword grep
- Embed skills for semantic search
- Track which skills produce successful products
- Add custom Founder Systems-specific skills over time
