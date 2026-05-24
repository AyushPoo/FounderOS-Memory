# Finance Operator Workbench Design

## Goal

Make the Founder Systems Finance Agent behave like a CFO operator, not a single-purpose spreadsheet generator. The agent should understand finance work requests, choose the right finance workflow, use connected user-owned tools, create polished artifacts, remember workspace context, and ask for approval only when the requested action writes to an external system or materially changes financial records.

## Current Problem

The live Finance Agent can call a small set of connector actions, but many finance requests fall through to generic chat or a weak generic Google Sheets path. That creates inconsistent behavior:

- A balance sheet can be created only because there is a specific rule for it.
- Other finance artifacts, such as forecasts, P&L, cash flow, invoice registers, budgets, valuation models, or investor finance docs, do not have equivalent builders.
- The generic sheet creator asks for columns even when the finance intent is obvious.
- The agent has connected tools, but it does not have a durable finance workflow layer that plans and executes multi-step CFO work.

The result feels dumb because the system is treating many CFO tasks as generic chat or generic tables.

## Product Principle

Founder Systems remains the control plane for billing, credits, user identity, entitlements, connected accounts, rate limits, and execution safety.

Hermes/runtime remains the agent plane for reasoning, product identity, memory use, planning, and tool selection.

The Finance Operator Workbench is a runtime capability layer that lets Hermes choose finance workflows while Founder Systems executes approved tool calls safely through user-owned integrations.

## Finance-Owned Scope

Finance owns:

- Financial statements: balance sheet, P&L, cash flow, trial balance-style summaries.
- Planning: budgets, runway, burn, forecast scenarios, hiring/cost plans, pricing and unit economics.
- Revenue and payments: Razorpay payment summaries, reconciliation workpapers, receivables trackers.
- Accounting support: invoice extraction, expense classification, books update proposals, journal-entry drafts.
- Investor finance: valuation, cap table summaries, term sheet drafts, board/investor finance updates, PromptDeck finance inputs.
- Finance documents: invoices, vendor notes, payment follow-up drafts, finance policies, MIS reports.

Finance does not own:

- Marketing copy, campaign execution, SEO content, ads, outbound messaging, or lead nurture.
- Hiring workflows, customer support, security operations, SOP ownership, or project execution.
- Final tax, legal, audit, investment, payroll, banking, or accounting-system authority.

When a request crosses domains, Finance should complete the finance-owned part and name the handoff.

## User Experience Target

The user should be able to say:

- "Make a runway model for GradeSense with 5L cash, 1.2L monthly burn, 20K MRR growing 10% monthly."
- "Take this invoice photo and update my expense tracker."
- "Create an IFRS-style balance sheet in Sheets."
- "Pull Razorpay payments and reconcile this week."
- "Make the finance section for my pitch deck."
- "Build a valuation model for a SaaS startup using ARR and comparables."
- "Draft a term sheet summary for this investment offer."

The agent should:

1. Understand the finance intent even with typos or casual wording.
2. Infer the likely artifact and tool.
3. Use memory for company, currency, fiscal year, known website, and prior assumptions.
4. Create a useful first draft when enough information exists.
5. Ask one focused question only when a required input is genuinely missing.
6. Use connected tools when available.
7. Fall back to a downloadable or paste-ready artifact if a connector is missing.
8. Report tool failures clearly and retry only when safe.

## Architecture

### 1. Finance Intent Router

Add a finance-specific router before generic sheet/doc handling. It maps natural language to finance workflows.

Workflow categories:

- `financial_statement`
- `budget_or_forecast`
- `runway_model`
- `valuation_model`
- `invoice_or_receipt_processing`
- `payments_reconciliation`
- `books_update_proposal`
- `investor_finance_pack`
- `term_sheet_or_financing_doc`
- `finance_email_or_followup`
- `finance_question`

The router should use deterministic cues first and Hermes planning second. Deterministic cues handle high-confidence common cases; Hermes handles broad wording and edge cases.

### 2. Finance Artifact Builders

Create dedicated artifact builders that output structured payloads instead of generic rows.

Initial builders:

- Balance sheet builder: IFRS-style statement of financial position with formulas, sections, checks, and notes.
- P&L builder: revenue, COGS, gross profit, operating expenses, EBITDA, net profit, assumptions.
- Cash flow builder: opening cash, inflows, outflows, net cash movement, ending cash.
- Runway builder: cash, burn, revenue, growth, scenario rows, runway months.
- Budget builder: departments, monthly spend, owner, committed/planned status.
- Invoice register builder: vendor/customer, invoice date, due date, amount, tax, status, category.
- Valuation builder: revenue/ARR inputs, method, multiples, low/base/high valuation, assumptions.
- Investor finance doc builder: concise finance narrative for deck, memo, or update.

Each builder returns:

- `artifact_type`
- `title`
- `values` for Sheets or `body_text` for Docs
- formatting hints for Sheets
- assumptions and missing inputs
- confidence

### 3. Tool Action Layer

Finance can use these actions in V1:

- Google Sheets create for models, trackers, registers, statements, forecasts.
- Google Docs create for finance docs, memos, term sheets, invoice notes, board updates.
- Razorpay payments list for payment summaries and reconciliation inputs.
- Gmail send only for finance-owned emails after approval, if Gmail is connected.
- PromptDeck handoff for finance sections and deck-ready content when PromptDeck is available.

Future actions:

- Google Drive file read/write.
- OCR for invoice/photo extraction.
- Tally, Zoho Books, QuickBooks, Xero read/write proposals.
- Bank statement parsing.
- Payroll and tax read-only summaries.

### 4. Memory

Finance should read and write workspace memory through Founder Systems:

User/company facts:

- founder name
- company name
- website
- currency
- fiscal year
- jurisdiction
- business model
- revenue streams
- price points
- cost categories
- current cash
- monthly burn
- monthly revenue
- connected finance tools

Task facts:

- current artifact type
- last created spreadsheet/doc URL
- assumptions used
- pending approval action
- current draft version
- source files used

Memory must be shared enough that Marketing/Ops know company facts, but Finance-specific assumptions should stay tagged as finance memory.

### 5. Approval Rules

No approval needed:

- Create a new Sheet or Doc for the user.
- Draft a finance model, memo, term sheet, or report.
- Read connected data from Razorpay or reporting tools.
- Analyze uploaded files or screenshots.

Approval needed:

- Send an email.
- Share a file externally.
- Modify an existing accounting/bookkeeping/payroll/tax system.
- Create a payment, refund, payout, or bank action.
- Store or reuse sensitive financial details beyond normal workspace memory.

Blocked in V1:

- Autonomous money movement.
- Autonomous tax filing.
- Autonomous accounting-system writes without explicit connector and approval.
- Final legal/tax/audit/investment advice.

### 6. Quality Bar

Finance artifacts must look like a professional operator produced them:

- Clear title and period.
- Clean structure and sectioning.
- Useful formulas where applicable.
- Assumptions and notes.
- Balance/check rows.
- Currency/number formatting.
- No random generic rows.
- No "what columns should it have?" for obvious finance artifacts.
- Concise Telegram confirmation with URL and credits used.

### 7. Failure Behavior

If a connector is missing:

- Say the missing connector.
- Give the exact Founder Systems connection link if available.
- Create a fallback Sheet/Doc-ready artifact when possible.

If a tool fails:

- Retry once only if the operation is idempotent or safe.
- If it still fails, state the exact failure and next fix.
- Do not pretend the action succeeded.

If required inputs are missing:

- Ask one focused question.
- Provide an example answer.
- Do not ask broad generic setup questions.

## Implementation Approach

Implement in layers:

1. Add finance workflow types and router tests.
2. Add artifact builder module with tests for each first-class finance artifact.
3. Replace generic Finance Sheets handling with the finance workbench path.
4. Add connector payload formatting for every finance sheet artifact.
5. Add memory reads/writes for finance facts and last artifact state.
6. Add OCR/photo intake only after the artifact routing foundation is stable.
7. Add PromptDeck handoff after finance narrative/doc generation is reliable.

## Initial V1 Scope

Build first:

- Balance sheet
- P&L
- Cash flow
- Runway model
- Budget
- Invoice register
- Razorpay reconciliation summary
- Valuation model
- Investor finance memo/doc

Do not build first:

- Full accounting-system writes.
- Bank integrations.
- Payroll integrations.
- Tax filing.
- Full PromptDeck deck generation from Telegram.
- OCR pipeline for invoices.

These are V1.5 after the core workbench behaves correctly.

## Test Strategy

Runtime tests:

- Casual/typo-heavy finance requests route to the correct workflow.
- Obvious finance artifacts never fall into generic "what columns" prompts.
- Each artifact builder returns professional structure, formulas where useful, and notes.
- Missing inputs produce one focused question.
- Connected action payloads include product/user metadata and credit-safe approval text.
- Memory facts are used for company name, currency, fiscal year, and website.

Founder Systems API tests:

- Google Sheets formatting supports frozen rows, widths, bold rows, and currency columns.
- Connector actions reserve/finalize/release credits correctly.
- Missing connectors return actionable errors.
- Future file/OCR/action endpoints deny empty wallet, blocked users, disabled models, and cap violations.

Manual live tests:

- Create P&L in Sheets.
- Create cash flow in Sheets.
- Create runway model in Sheets.
- Create valuation model in Sheets.
- Pull Razorpay payments and create reconciliation summary.
- Ask "what did we use last time?" and verify memory.

## Success Criteria

The Finance Agent is ready when:

- A user can ask for common CFO artifacts in natural language and get a professional Sheet or Doc.
- The agent understands context and prior facts across Finance conversations.
- It uses Google Sheets, Docs, Gmail, and Razorpay through Founder Systems controls.
- It does not overlap into Marketing or Ops work.
- It asks fewer, better questions.
- It reports failures honestly.
- It never burns credits without attribution and never performs high-risk external actions without approval.
