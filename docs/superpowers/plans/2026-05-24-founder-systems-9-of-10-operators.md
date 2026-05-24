# Founder Systems 9/10 Operators Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Do not use subagents unless Ayush explicitly reverses the "no subagents" instruction.

**Goal:** Upgrade Marketing, Finance, and Ops Telegram operators from early working demos into reliable, measurable, agentic business operators that can remember context, choose tools, create polished artifacts, and execute approved tasks safely.

**Architecture:** Founder Systems remains the control plane for users, billing, entitlements, credits, memory, connected accounts, rate limits, and analytics. Hermes remains the agent runtime and reasoning layer, but every agent must run through a domain-specific workbench that supplies capability boundaries, workflow state, tool routing, artifact templates, retries, and evaluation telemetry. Heavy jobs run through the runtime queue so Telegram stays responsive.

**Tech Stack:** Founder Systems FastAPI, Postgres, Founder Systems Vite frontend, founder-agents-runtime FastAPI bridge, Hermes runtime, Telegram Bot API, Google Workspace APIs, Razorpay, GitHub/HubSpot/Mailchimp/Meta/LinkedIn connectors, AWS systemd timers/services, pytest.

---

## Success Definition

The agents are "9/10" only when these are true:

- Marketing can complete practical CMO work: research, positioning, campaigns, email/outreach, content calendars, SEO/GSC analysis, CRM handoff, and campaign reporting.
- Finance can complete practical CFO work: ingest receipts/statements, make polished Sheets/Docs, produce IFRS-style statements, budgets, runway, valuation, investor finance docs, Razorpay/payment analysis, and accounting-system handoff.
- Ops can complete practical COO work: SOPs, support workflows, hiring trackers, security checklists, customer replies, calendar coordination, GitHub issue/project ops, and recurring operational follow-ups.
- Each agent knows what belongs to it and does not overlap into the others except by saying which operator should handle the task.
- Every tool action has clear state: `planned`, `needs_connection`, `needs_clarification`, `queued`, `running`, `done`, `failed_retryable`, or `failed_final`.
- Memory answers are correct across all three agents for shared user/company facts.
- Telegram replies are short, polished, and stateful.
- Heavy jobs do not block chat.
- Analytics shows success/failure/latency/usage per user, product, action, model, and connector.

## File Map

Runtime repo: `F:\Work\Website\founder-agents-runtime`

- Create: `bridge/operator_contracts.py`  
  Product capability boundaries, workflows, approval policies, and allowed connectors.
- Create: `bridge/workflow_state.py`  
  Persistent task state for multi-turn actions: pending drafts, tool jobs, missing fields, retries, and artifacts.
- Create: `bridge/operator_evals.py`  
  Offline evaluation harness for routing, memory, action planning, and artifact quality checks.
- Create: `bridge/tests/test_operator_contracts.py`  
  Tests that each product only accepts its own domain and hands off the rest.
- Create: `bridge/tests/test_workflow_state.py`  
  Tests multi-turn task memory, pending draft edits, and retryable failure state.
- Modify: `bridge/app.py`  
  Use contracts and workflow state before fallback chat; log action lifecycle; queue heavy tasks.
- Modify: `bridge/finance_workbench.py`  
  Upgrade spreadsheet artifacts from simple rows to professional multi-section templates.
- Create: `bridge/marketing_workbench.py`  
  Marketing-specific task builders: email/outreach, campaign plan, SEO brief, content calendar.
- Create: `bridge/ops_workbench.py`  
  Ops-specific task builders: SOP, support reply, hiring tracker, security checklist.
- Create: `bridge/tests/test_marketing_workbench.py`
- Create: `bridge/tests/test_ops_workbench.py`
- Modify: `profiles/*/SOUL.md`  
  Keep prompts strict, short, action-oriented, and aligned with the contracts.

Founder Systems repo: `F:\Work\Founder-Systems`

- Modify: `founder_systems_api/app/models.py`  
  Add operator task/run state if Postgres persistence is needed beyond runtime state files.
- Modify: `founder_systems_api/app/schemas.py`
- Modify: `founder_systems_api/app/main.py`
- Modify: `founder_systems_api/app/cost_guard.py`
- Create: `founder_systems_api/tests/test_operator_runs.py`
- Modify: `src/pages/Account.jsx`  
  Show operator task status and connected app readiness.

Analytics repo: `F:\Work\FounderOS-Analytics`

- Modify: `src/hooks/useMetrics.js`
- Modify: `src/components/CostGuardPanel.jsx`
- Create: `src/components/OperatorQualityPanel.jsx`

---

## Task 1: Operator Contracts And Boundaries

**Files:**
- Create: `F:\Work\Website\founder-agents-runtime\bridge\operator_contracts.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_operator_contracts.py`
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\app.py`

- [ ] **Step 1: Write failing tests for task classification and handoff**

Create `bridge/tests/test_operator_contracts.py`:

```python
from bridge.operator_contracts import classify_operator_intent


def test_marketing_accepts_outreach_and_seo():
    assert classify_operator_intent("marketing-agent", "send an outreach email to schools").decision == "accept"
    assert classify_operator_intent("marketing-agent", "check search console for gradesense").decision == "accept"


def test_finance_accepts_statements_and_rejects_campaigns():
    assert classify_operator_intent("finance-agent", "make an IFRS balance sheet in Google Sheets").decision == "accept"
    result = classify_operator_intent("finance-agent", "write LinkedIn posts for our launch")
    assert result.decision == "handoff"
    assert result.target_product_slug == "marketing-agent"


def test_ops_accepts_support_hiring_security_and_rejects_finance():
    assert classify_operator_intent("ops-agent", "create a hiring tracker for sales reps").decision == "accept"
    result = classify_operator_intent("ops-agent", "make a runway model")
    assert result.decision == "handoff"
    assert result.target_product_slug == "finance-agent"
```

- [ ] **Step 2: Run tests to verify red**

Run:

```powershell
$env:PYTHONPATH='.'; uv run --with-requirements requirements.txt pytest bridge/tests/test_operator_contracts.py -q
```

Expected: import failure for `bridge.operator_contracts`.

- [ ] **Step 3: Implement `operator_contracts.py`**

Create a focused classifier using contract keywords, near-word matching, and explicit handoff targets.

- [ ] **Step 4: Wire handoff into `bridge/app.py`**

Before connector routing, if decision is `handoff`, send a short response:

```text
That is better handled by Finance Operator. I can help with marketing work here, or you can open the Finance bot from Founder Systems.
```

- [ ] **Step 5: Verify**

Run:

```powershell
$env:PYTHONPATH='.'; uv run --with-requirements requirements.txt pytest bridge/tests/test_operator_contracts.py bridge/tests/test_telegram_webhook.py::test_telegram_webhook_explains_known_but_unsupported_linkedin_action -q
```

Expected: all pass.

---

## Task 2: Workflow State For Multi-Turn Tasks

**Files:**
- Create: `F:\Work\Website\founder-agents-runtime\bridge\workflow_state.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_workflow_state.py`
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\app.py`

- [ ] **Step 1: Write failing tests**

```python
from bridge.workflow_state import WorkflowStore


def test_pending_email_can_be_edited_after_send_failure(tmp_path):
    store = WorkflowStore(tmp_path / "state.json")
    store.save_pending_task(
        product_slug="marketing-agent",
        telegram_user_id="tg-1",
        task_type="gmail_send",
        payload={"recipient": "a@example.com", "subject": "Hello", "body": "Hi"},
    )
    store.patch_pending_task("marketing-agent", "tg-1", {"body": "Hi\\nPhone: 123"})
    task = store.get_pending_task("marketing-agent", "tg-1")
    assert task["payload"]["body"].endswith("Phone: 123")


def test_done_task_is_recallable_as_previous_artifact(tmp_path):
    store = WorkflowStore(tmp_path / "state.json")
    store.mark_done("finance-agent", "tg-1", "sheet", {"url": "https://sheet"})
    assert store.last_done("finance-agent", "tg-1")["artifact"]["url"] == "https://sheet"
```

- [ ] **Step 2: Implement state store**

Persist per `product_slug:telegram_user_id`:

```json
{
  "pending_task": {},
  "last_done": {},
  "last_failed": {},
  "artifacts": []
}
```

- [ ] **Step 3: Wire into email, Sheets, Docs, and artifact actions**

Store every prepared draft before send; keep previous artifact after completion; support edits like "add my number to previous mail".

- [ ] **Step 4: Verify**

Run:

```powershell
$env:PYTHONPATH='.'; uv run --with-requirements requirements.txt pytest bridge/tests/test_workflow_state.py bridge/tests/test_telegram_webhook.py -q
```

---

## Task 3: Marketing Workbench

**Files:**
- Create: `F:\Work\Website\founder-agents-runtime\bridge\marketing_workbench.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_marketing_workbench.py`
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\app.py`

- [ ] **Step 1: Add tests for polished outreach**

Test that a vague request creates either a concise clarification or a professional draft, never a generic random email.

- [ ] **Step 2: Implement structured builders**

Builders:

- `build_outreach_email`
- `build_campaign_plan`
- `build_seo_brief`
- `build_content_calendar`
- `build_linkedin_post_pack`

- [ ] **Step 3: Wire Gmail and Docs**

Drafts go to Telegram for review. Direct sends require either clear command intent or prior pending draft state.

- [ ] **Step 4: Verify with real Gmail smoke test**

Use a test account and confirm message body is the drafted body, not an approval instruction.

---

## Task 4: Finance Workbench 2.0

**Files:**
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\finance_workbench.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_finance_workbench.py`

- [ ] **Step 1: Add tests for professional statement structure**

Balance sheet must include:

- title rows
- reporting period
- assets/current assets/non-current assets
- liabilities/current/non-current
- equity
- totals
- balance check
- notes
- formula-ready rows

- [ ] **Step 2: Upgrade templates**

Use multi-section values and formatting metadata that Google Sheets can apply.

- [ ] **Step 3: Add document outputs**

Support:

- investor finance memo
- term sheet draft
- board finance update
- variance analysis

---

## Task 5: Ops Workbench

**Files:**
- Create: `F:\Work\Website\founder-agents-runtime\bridge\ops_workbench.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_ops_workbench.py`
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\app.py`

- [ ] **Step 1: Add tests for ops artifacts**

Tests cover SOP, support response, hiring tracker, security checklist.

- [ ] **Step 2: Implement ops builders**

Builders:

- `build_sop`
- `build_support_reply`
- `build_hiring_tracker`
- `build_security_checklist`
- `build_weekly_ops_review`

- [ ] **Step 3: Wire Google Docs/Sheets/GitHub**

Support docs go to Docs; trackers go to Sheets; engineering ops can create GitHub issues.

---

## Task 6: Connector Reliability Layer

**Files:**
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\integrations.py`
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\main.py`
- Test: `F:\Work\Founder-Systems\founder_systems_api\tests\test_integrations.py`

- [ ] **Step 1: Add retryable/final failure schema**

Every connector action returns:

```json
{
  "ok": true,
  "state": "done|needs_connection|failed_retryable|failed_final",
  "human_message": "short message",
  "artifact_url": "optional",
  "usage_units": 0
}
```

- [ ] **Step 2: Add retries**

Retry network and 429/5xx failures with capped backoff. Do not retry 401/403 without reconnection.

- [ ] **Step 3: Add connector health endpoints**

Analytics can show connected, expired, failed, and last-used state.

---

## Task 7: Operator Analytics And Upgrade Readiness

**Files:**
- Modify: `F:\Work\FounderOS-Analytics\src\hooks\useMetrics.js`
- Create: `F:\Work\FounderOS-Analytics\src\components\OperatorQualityPanel.jsx`
- Modify: `F:\Work\FounderOS-Analytics\src\pages\Dashboard.jsx`

- [ ] **Step 1: Show operator quality**

Metrics:

- completion rate
- failure rate
- median/p95 latency
- queue depth
- usage units by product
- connector failures
- handoff count

- [ ] **Step 2: Show upgrade warnings**

Surface VM monitor metrics and alerts in analytics.

---

## Task 8: Evaluation Harness And Release Gate

**Files:**
- Create: `F:\Work\Website\founder-agents-runtime\bridge\operator_evals.py`
- Create: `F:\Work\Website\founder-agents-runtime\evals\operator_scenarios.json`
- Create: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_operator_evals.py`

- [ ] **Step 1: Add golden scenarios**

At least 20 per operator:

- 8 normal tasks
- 4 vague tasks requiring clarification
- 4 connected-tool tasks
- 2 memory tasks
- 2 out-of-domain handoffs

- [ ] **Step 2: Implement evaluator**

Evaluator checks:

- correct product domain
- correct action/reply/clarify/handoff
- output length
- no fake claim of tool usage
- required fields collected

- [ ] **Step 3: Make eval mandatory before deploy**

Add command:

```powershell
$env:PYTHONPATH='.'; uv run --with-requirements requirements.txt python -m bridge.operator_evals
```

Minimum release gate:

- routing accuracy >= 90%
- memory accuracy >= 95%
- fake action claims = 0
- connector action state coverage = 100%

---

## Task 9: Production Rollout

**Files:**
- Modify: `F:\Work\Website\founder-agents-runtime\README.md`
- Modify: systemd services on AWS

- [ ] **Step 1: Deploy runtime**

Restart:

```bash
sudo systemctl restart founder-marketing-agent founder-finance-agent founder-ops-agent
```

- [ ] **Step 2: Smoke test**

Test one chat, one memory question, one connector task, one handoff, one queued heavy task per agent.

- [ ] **Step 3: Push to GitHub**

```powershell
git add .
git commit -m "feat: upgrade founder systems operators"
git push origin main
```

---

## Self-Review

Spec coverage:

- Marketing/Finance/Ops domain separation: Tasks 1, 3, 4, 5.
- Agentic execution and connectors: Tasks 3, 4, 5, 6.
- Memory: Task 2.
- Quality and 9/10 measurement: Tasks 7, 8.
- Heavy jobs and responsiveness: already started, extended by Tasks 2, 6, 7.
- Production deployment: Task 9.

No placeholder scan:

- No `TBD` or `TODO`.
- Each task has file targets, test expectations, and commands.

Type consistency:

- Product slugs remain `marketing-agent`, `finance-agent`, `ops-agent`.
- Runtime remains the agent/action layer.
- Founder Systems remains control plane.
