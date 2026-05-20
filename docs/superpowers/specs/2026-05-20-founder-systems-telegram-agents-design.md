# Founder Systems Telegram Agents Design

Date: 2026-05-20

Primary plan source:
- `F:\Work\FounderOS-Memory\03 - Products\2026-05-20 Founder Systems Telegram Agents Architecture Plan.md`

Primary repos:
- `F:\Work\Founder-Systems`
- `F:\Work\Founder-Systems\founder_systems_api`

New runtime repo:
- `F:\Work\Website\founder-agents-runtime`

## Goal

Launch Founder Systems agent products on Telegram with Hermes as the runtime layer and Founder Systems as the control plane. V1 should launch three paid specialist agents first:

- Marketing Agent
- Finance Agent
- Ops Agent

Cofounder Agent ships later after the first three are stable.

The business goal is not to sell generic chat access. It is to sell specialist founder operators that can do meaningful work through bounded execution flows, not only explain what to do.

## Core Architecture

### Founder Systems responsibilities

Founder Systems is the source of truth for all business state:

- product catalog
- product passes and pricing
- checkout and top-ups through Razorpay
- account identity
- Telegram linking
- entitlements and pass expiry
- shared credit wallet
- credit reservations and finalization
- approval records
- audit logs
- admin diagnostics

Founder Systems must remain the control plane. Hermes must not become the commercial system.

### Hermes responsibilities

Hermes is the runtime plane:

- Telegram conversation handling
- per-product profiles
- per-product memory
- task planning and execution
- model routing decisions within allowed policy
- execution through approved tools and adapters

Hermes should ask Founder Systems for access, budget, and approval state before starting premium or write-capable work.

### Execution adapters

A separate execution layer should handle domain actions safely:

- finance ingestion and accounting adapters
- messaging and outbound marketing adapters
- support and HR workflow adapters
- storage and artifact-generation adapters

These adapters should expose bounded actions with explicit policies rather than broad shell, filesystem, or browser access.

## Product Shape

### Marketing Agent

Job to be done:
- handle founder marketing work across positioning, content, campaigns, and outreach

V1 responsibilities:
- ICP and market framing
- positioning and messaging
- SEO clustering and briefs
- launch plans
- campaign drafts
- content systems
- outbound drafts and approval-ready sends
- creative and channel recommendations

V1 premium execution examples:
- content batch generation
- SEO map generation
- campaign pack generation
- approved outbound message sends

### Finance Agent

Job to be done:
- handle finance and accounting operations without promising unrestricted autonomy

V1 responsibilities:
- ingest statements and finance files
- classify transactions
- produce draft books and finance summaries
- generate P&L, cash flow, and runway views
- support reconciliations
- review pricing, forecast, and fundraising models

V1 premium execution examples:
- statement-to-ledger processing
- forecast packs
- board finance summaries
- model review artifacts

### Ops Agent

Job to be done:
- handle repeatable business operations across support, SOPs, workflows, and internal execution

V1 responsibilities:
- SOP drafting
- process design
- support workflow handling
- HR/admin checklist flows
- project and cadence setup
- internal docs and follow-ups

V1 premium execution examples:
- support workflow runs
- SOP bundles
- hiring workflow kits
- structured follow-up sequences

### Cofounder Agent

Job to be done:
- orchestrate cross-functional work across the specialist agents

This should not launch first. It ships only after the first three prove stable in retention, support load, and runtime economics.

## Product Positioning

The value proposition should be:

- specialist AI operators for founders
- can complete meaningful work, not just answer questions
- accessible in Telegram
- backed by memory, workflows, approvals, and structured outputs

The messaging should avoid claiming to fully replace a human employee without qualification. A safer and still strong promise is:

- handles a large share of the work
- executes repeatable workflows
- prepares and completes tasks with approvals when needed

## Business Model

### Access model

Use prepaid per-product access passes instead of open-ended postpaid usage.

Each product has its own paid 30-day pass:

- a user buys Marketing access separately from Finance or Ops
- no shared pass across products in V1
- access stops when the pass expires

### Wallet model

Use one shared top-up wallet across subscribed products.

Rules:
- product access is determined by the active product pass
- usage budget is determined by the shared wallet plus included credits
- a top-up does not unlock a product by itself
- premium actions stop when the wallet is empty

### Included credits

Each product pass includes a bundle of execution credits. These credits are consumed by premium work, not casual chat. Credits are best understood as prepaid execution budget, not raw token accounting.

### Top-ups

Users can buy additional credits through Razorpay. Top-ups should be one-time prepaid purchases. The platform must never rely on post-use reimbursement.

## Pricing Strategy

### Competitive anchor

The product cannot win by being a more expensive version of Claude or ChatGPT. The price must feel credible relative to consumer AI subscriptions while justifying itself through specialist workflows and execution.

### Recommended V1 pricing

- Marketing Agent: `Rs. 999 / 30 days` + `500 credits`
- Ops Agent: `Rs. 999 / 30 days` + `500 credits`
- Finance Agent: `Rs. 1499 / 30 days` + `750 credits`
- Cofounder Agent later: `Rs. 2499 / 30 days` + `1250 credits`

Recommended top-ups:
- `Rs. 499` for `250 credits`
- `Rs. 999` for `600 credits`
- `Rs. 1999` for `1400 credits`

### Credit unit

Use:

- `1 credit = Rs. 0.50` of model budget

This keeps credit numbers high enough to feel usable while staying grounded in real cost accounting.

### Margin guardrail

The system should target a hard cap for included model spend on each pass. No premium action should start without a budget reservation. This keeps model cost bounded before the user runs the task.

## Model Strategy

### High-level rule

Do not default everything to Claude. Default work should route to lower-cost but still capable models, while premium/high-stakes work can upgrade to Claude.

### Recommended model tiers

Economy:
- `MiniMax M2.5`

Standard:
- `Kimi K2 Thinking`
- `Kimi K2.5`

Premium:
- `Claude Sonnet 4`

Deep premium later:
- `Claude Opus`

### Why

On current pricing, MiniMax and Kimi are materially cheaper than Claude Sonnet, which gives users more perceived room before credits run out. Claude should be a higher-cost tier used when quality or reliability needs justify it.

### User-facing mode design

Expose simple choices:
- Economy
- Standard
- Premium

Avoid exposing a raw model picker in V1. The system can map these modes to specific approved models internally.

## Credit Burn Policy

Credits should be burned by premium actions, not by every message.

Examples of premium actions:
- document and statement processing
- long-form artifact generation
- structured campaign packs
- forecast packs
- high-effort support workflow execution
- external write actions

Example burn table:

| Task tier | MiniMax M2.5 | Kimi K2 Thinking | Kimi K2.5 | Claude Sonnet 4 |
|---|---:|---:|---:|---:|
| Light | 2 credits | 3 credits | 3 credits | 12 credits |
| Medium | 4 credits | 7 credits | 8 credits | 32 credits |
| Heavy | 11 credits | 22 credits | 24 credits | 100 credits |

This is intentionally coarse. V1 should keep pricing understandable instead of trying to expose raw token economics.

## Action Policy

Every action should fall into one of three classes:

- Auto
- Approve
- Blocked

### Auto

Low-risk internal tasks:
- drafting
- classification
- summarization
- internal artifact generation
- data extraction

### Approve

High-risk or external-impact tasks:
- outbound messaging
- accounting writes
- customer-facing responses outside approved templates
- anything that changes external systems
- anything that spends a large amount of credits

### Blocked

Disallowed tasks:
- unrestricted shell
- unrestricted filesystem
- unrestricted browser
- high-risk financial actions
- unsanctioned account access

## Access And Budget Flow

Every premium flow should follow this sequence:

1. user sends task in Telegram
2. Hermes classifies the task
3. Hermes asks Founder Systems for:
   - entitlement status
   - pass status
   - pricing estimate
   - approval requirement
   - credit reservation
4. Founder Systems either rejects, reserves, or requests approval
5. Hermes executes only after approval and reservation are valid
6. Founder Systems finalizes or releases the reservation
7. all events are logged for support and auditing

Rules:
- no active pass means no access
- no available credits means no premium task
- reservations must happen before expensive work starts
- unused reserved credits must be released
- balances must never go negative

## Data Model

Founder Systems should add or formalize the following entities:

- `products`
- `product_passes` or recurring entitlement records
- `wallet_accounts`
- `credit_ledger`
- `credit_reservations`
- `telegram_links`
- `agent_workspaces`
- `approval_events`
- `agent_events`

Important distinction:
- business state lives in Founder Systems Postgres
- conversational state lives in Hermes memory

## Repo Boundaries

### `F:\Work\Founder-Systems`

Owns:
- product pages
- pricing pages
- account and Telegram linking UI
- pass purchase and top-up UI
- wallet visibility
- customer status panels

### `F:\Work\Founder-Systems\founder_systems_api`

Owns:
- product and pricing API
- Razorpay integration
- pass entitlement logic
- wallet and ledger logic
- Telegram link tokens
- reservation/finalization API
- diagnostics and admin endpoints

### `F:\Work\Website\founder-agents-runtime`

Owns:
- Hermes install and profile layout
- per-product prompts and policies
- model routing
- gateway services
- provisioning bridge
- execution adapters
- deployment scripts and service units

## Telegram Strategy

Use one Telegram bot per product in V1.

Benefits:
- cleaner expectations
- simpler entitlement mapping
- cleaner safety boundaries
- easier support and rollback

Telegram should never be the access source of truth. Telegram identity is only the handle used to attach an entitled Founder Systems account to the runtime.

## Free Taste Strategy

Do not offer unlimited free use.

Recommended free experience:
- short trial window or starter allocation
- very small credit amount
- no premium external actions
- no Telegram execution until linked and paid if that simplifies abuse prevention
- cheapest model tier only

The purpose is to let people feel the product without exposing the platform to unbounded model spend.

## Quality Gates

V1 is not ready until the following are true:

- a user can buy a product pass and see it in account
- a user can buy top-up credits and see them in the shared wallet
- a user can link Telegram successfully
- unpaid or expired users are rejected cleanly
- premium runs reserve credits before work starts
- no negative balances are possible
- external actions are approval-gated according to policy
- support can inspect pass, wallet, Telegram link, and last runtime state without SSH

## Build Order

Recommended order:

1. Founder Systems product and pricing surfaces
2. Founder Systems API entities for passes, wallet, and Telegram linking
3. Razorpay product pass and top-up flows
4. Telegram linking UX
5. Hermes runtime repo and bridge
6. Product profiles
7. Access enforcement
8. Approval flows
9. Onboarding and diagnostics
10. Cofounder Agent later

## Final Recommendation

Build Founder Systems Telegram agents as prepaid specialist execution products:

- one paid 30-day pass per product
- one shared top-up wallet across products
- MiniMax and Kimi as the default execution tiers
- Claude as premium quality tier
- premium tasks consume credits
- external and risky actions require approval
- Founder Systems owns commercial truth
- Hermes owns runtime behavior

This gives the product real differentiation from ChatGPT or Claude while protecting cash flow and keeping the pricing understandable.
