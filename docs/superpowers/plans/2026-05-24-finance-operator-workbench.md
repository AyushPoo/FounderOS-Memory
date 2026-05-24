# Finance Operator Workbench Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first real Finance Operator Workbench so the Finance Agent can route natural-language CFO requests into professional Sheets/Docs/Razorpay workflows instead of generic chat or generic table prompts.

**Implementation status:** Runtime implementation completed and pushed in `founder-agents-runtime` commit `550665a` on `main`. The first release covers professional Google Sheets artifacts for balance sheet, P&L, cash flow, runway, valuation, budget/forecast, invoice registers, plus Razorpay payment reconciliation summaries. Higher-risk accounting writes, invoice-photo OCR posting, PromptDeck deck generation, and external accounting-system updates remain future connector work.

**Architecture:** Founder Systems remains the control plane for billing, credits, access, connected accounts, rate limits, and connector execution. The runtime repo gets a finance workbench module that classifies finance intent, builds structured finance artifacts, and hands safe connector payloads to Founder Systems. High-risk accounting writes, bank actions, and tax/legal final advice stay blocked until explicit future connectors and approval flows exist.

**Tech Stack:** Python, FastAPI runtime bridge, Hermes runtime planner, Founder Systems FastAPI connector endpoints, Google Sheets/Docs, Razorpay, pytest.

---

## File Structure

- Create: `F:\Work\Website\founder-agents-runtime\bridge\finance_workbench.py`
  - Owns finance workflow classification and artifact builders.
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\app.py`
  - Calls the finance workbench before generic connector handling.
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_finance_workbench.py`
  - Unit tests for routing and builders.
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_telegram_webhook.py`
  - Integration tests for Telegram-to-connector flows.
- Modify later if needed: `F:\Work\Founder-Systems\founder_systems_api\app\integrations.py`
  - Only if the runtime requires extra formatting support beyond current Sheets formatting.
- Modify later if needed: `F:\Work\Founder-Systems\founder_systems_api\tests\test_integrations.py`
  - Connector regression tests if API changes are required.

---

### Task 1: Add Finance Workflow Router And Artifact Interface

**Files:**
- Create: `F:\Work\Website\founder-agents-runtime\bridge\finance_workbench.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_finance_workbench.py`

- [ ] **Step 1: Write failing router tests**

Add tests for casual wording and typos:

```python
from bridge.finance_workbench import classify_finance_workflow


def test_classifies_core_finance_artifacts():
    examples = {
        "make me a pnl for gradesense with revenue 50000 and costs 20000": "profit_and_loss",
        "create cashflow for FY 2026 with opening cash 10000 inflow 5000 outflow 2000": "cash_flow",
        "build runway model cash 500000 burn 120000 mrr 20000": "runway_model",
        "make a valuation model using ARR 2400000 and multiple 6x": "valuation_model",
        "create invoice tracker for vendor bills": "invoice_register",
        "pull razorpay payments and reconcile this week": "payments_reconciliation",
        "prepare finance section for pitchdeck": "investor_finance_doc",
    }
    for message, expected in examples.items():
        assert classify_finance_workflow(message).workflow == expected
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
$env:PYTHONPATH='.'; uv run --with-requirements requirements.txt pytest bridge/tests/test_finance_workbench.py::test_classifies_core_finance_artifacts -q
```

Expected: fail because `bridge.finance_workbench` does not exist.

- [ ] **Step 3: Implement workflow result type and classifier**

Create:

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FinanceWorkflow:
    workflow: str
    confidence: float
    reason: str


def _lower(text: str) -> str:
    return " ".join(str(text or "").lower().split())


def classify_finance_workflow(message_text: str) -> FinanceWorkflow:
    text = _lower(message_text)
    compact = text.replace(" ", "")
    if "razorpay" in text and any(word in text for word in {"payment", "payments", "reconcile", "settlement"}):
        return FinanceWorkflow("payments_reconciliation", 0.92, "Razorpay payment reconciliation request")
    if "valuation" in text or "multiple" in text or "arr" in text:
        return FinanceWorkflow("valuation_model", 0.86, "Valuation or ARR multiple request")
    if "runway" in text or ("burn" in text and "cash" in text):
        return FinanceWorkflow("runway_model", 0.9, "Runway or burn model request")
    if "cashflow" in compact or "cash flow" in text:
        return FinanceWorkflow("cash_flow", 0.9, "Cash flow statement request")
    if "p&l" in text or "pnl" in compact or "profit and loss" in text:
        return FinanceWorkflow("profit_and_loss", 0.9, "Profit and loss request")
    if "balance sheet" in text or "balancesheet" in compact:
        return FinanceWorkflow("balance_sheet", 0.9, "Balance sheet request")
    if "invoice" in text or "receipt" in text or "vendor bill" in text:
        return FinanceWorkflow("invoice_register", 0.82, "Invoice or receipt workflow")
    if "pitchdeck" in compact or "pitch deck" in text or "investor" in text:
        return FinanceWorkflow("investor_finance_doc", 0.8, "Investor finance artifact request")
    if "budget" in text or "forecast" in text:
        return FinanceWorkflow("budget_or_forecast", 0.78, "Budget or forecast request")
    return FinanceWorkflow("finance_question", 0.35, "General finance request")
```

- [ ] **Step 4: Run test to verify it passes**

Run the same command. Expected: pass.

- [ ] **Step 5: Commit runtime router**

```powershell
git add bridge/finance_workbench.py bridge/tests/test_finance_workbench.py
git commit -m "feat: add finance workflow router"
```

---

### Task 2: Add Professional Sheets Artifact Builders

**Files:**
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\finance_workbench.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_finance_workbench.py`

- [ ] **Step 1: Write failing builder tests**

Add:

```python
from bridge.finance_workbench import build_finance_sheet_artifact


def test_builds_professional_sheet_artifacts():
    cases = [
        ("make pnl with revenue 50000 cogs 10000 opex 15000", "profit_and_loss", "Gross profit"),
        ("create cash flow opening cash 10000 inflow 5000 outflow 2000", "cash_flow", "Ending cash"),
        ("runway model cash 500000 burn 120000 mrr 20000", "runway_model", "Runway months"),
        ("valuation model ARR 2400000 multiple 6x", "valuation_model", "Base valuation"),
        ("invoice tracker for vendor bills", "invoice_register", "Invoice number"),
    ]
    for message, workflow, expected_text in cases:
        artifact = build_finance_sheet_artifact(workflow, message, memory_facts={"company": "GradeSense", "currency": "INR"})
        flat = " ".join(str(cell) for row in artifact.values for cell in row)
        assert artifact.action == "google_sheets_create"
        assert artifact.title.startswith("GradeSense")
        assert len(artifact.values) >= 10
        assert expected_text in flat
        assert artifact.freeze_rows >= 1
        assert artifact.column_widths
        assert artifact.bold_rows
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
$env:PYTHONPATH='.'; uv run --with-requirements requirements.txt pytest bridge/tests/test_finance_workbench.py::test_builds_professional_sheet_artifacts -q
```

Expected: fail because `build_finance_sheet_artifact` does not exist.

- [ ] **Step 3: Implement artifact dataclass and builders**

Add:

```python
@dataclass(frozen=True)
class FinanceArtifact:
    action: str
    title: str
    values: list[list[str]]
    body_text: str = ""
    freeze_rows: int = 1
    column_widths: list[int] | None = None
    bold_rows: list[int] | None = None
    currency_columns: list[int] | None = None
    missing_inputs: list[str] | None = None


def _fact(memory_facts: dict[str, str], key: str, default: str) -> str:
    value = str((memory_facts or {}).get(key) or "").strip()
    return value or default


def _num_after(text: str, labels: set[str], default: str = "0") -> str:
    import re
    lowered = _lower(text)
    for label in labels:
        match = re.search(rf"{re.escape(label)}\D+([0-9][0-9,]*(?:\.[0-9]+)?)", lowered)
        if match:
            return match.group(1).replace(",", "")
    return default


def build_finance_sheet_artifact(workflow: str, message_text: str, *, memory_facts: dict[str, str] | None = None) -> FinanceArtifact | None:
    facts = memory_facts or {}
    company = _fact(facts, "company", _fact(facts, "company_name", "Founder Systems"))
    currency = _fact(facts, "currency", "INR")
    widths = [260, 180, 150, 360]
    if workflow == "profit_and_loss":
        revenue = _num_after(message_text, {"revenue", "sales", "income"})
        cogs = _num_after(message_text, {"cogs", "cost of goods", "direct cost"})
        opex = _num_after(message_text, {"opex", "expenses", "operating expense"})
        return FinanceArtifact(
            action="google_sheets_create",
            title=f"{company} Profit and Loss",
            values=[
                [company],
                ["Profit and Loss Statement", "", "", ""],
                ["Currency", currency, "", ""],
                ["Line item", "Classification", "Amount", "Notes"],
                ["Revenue", "Income", revenue, "User-provided or assumed"],
                ["COGS", "Direct cost", cogs, "User-provided or assumed"],
                ["Gross profit", "", "=C5-C6", ""],
                ["Operating expenses", "Opex", opex, "User-provided or assumed"],
                ["EBITDA", "", "=C7-C8", ""],
                ["Net profit", "", "=C9", "Before tax unless tax provided"],
                ["Assumptions", "", "", "Management draft; not audited"],
            ],
            freeze_rows=4,
            column_widths=widths,
            bold_rows=[1, 2, 4, 7, 9, 10],
            currency_columns=[3],
        )
    # Implement cash_flow, runway_model, valuation_model, invoice_register, budget_or_forecast similarly.
    return None
```

Complete all cases in the test, using the same dataclass contract.

- [ ] **Step 4: Run test to verify it passes**

Run the focused builder test. Expected: pass.

- [ ] **Step 5: Commit builders**

```powershell
git add bridge/finance_workbench.py bridge/tests/test_finance_workbench.py
git commit -m "feat: add finance sheet artifact builders"
```

---

### Task 3: Route Finance Telegram Requests Through The Workbench

**Files:**
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\app.py`
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\finance_workbench.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_telegram_webhook.py`

- [ ] **Step 1: Write failing Telegram integration tests**

Add tests that prove obvious CFO requests do not hit generic sheet prompts:

```python
def test_finance_pnl_request_creates_professional_sheet(monkeypatch):
    # Set FOUNDER_PRODUCT_SLUG=finance-agent.
    # Mock access-check as active.
    # Mock google/sheets/create and capture payload.
    # Send: "make a pnl for GradeSense revenue 50000 cogs 10000 opex 15000"
    # Assert payload title contains "Profit and Loss".
    # Assert payload values include "Gross profit" and formulas.
    # Assert Telegram confirmation says Created Google Sheet.


def test_finance_runway_request_creates_professional_sheet(monkeypatch):
    # Same pattern.
    # Send: "build runway model for GradeSense cash 500000 burn 120000 mrr 20000"
    # Assert payload values include "Runway months".
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
$env:PYTHONPATH='.'; uv run --with-requirements requirements.txt pytest bridge/tests/test_telegram_webhook.py::test_finance_pnl_request_creates_professional_sheet bridge/tests/test_telegram_webhook.py::test_finance_runway_request_creates_professional_sheet -q
```

Expected: fail because `app.py` does not call the workbench yet.

- [ ] **Step 3: Add workbench execution helper in `app.py`**

Import:

```python
from .finance_workbench import build_finance_sheet_artifact, classify_finance_workflow
```

Add before the generic sheet handler in `_maybe_handle_connector_action`:

```python
if product_slug == "finance-agent" and wants_create and _connector_action_allowed(product_slug, "google_sheets_create"):
    memory_context = _load_founder_systems_memory_context(product_slug=product_slug, telegram_user_id=telegram_user_id)
    facts = _facts_from_memory_context(memory_context)
    workflow = classify_finance_workflow(message_text)
    artifact = build_finance_sheet_artifact(workflow.workflow, message_text, memory_facts=facts)
    if artifact is not None:
        result = _connector_action_response(
            "google_sheets_create",
            _connector_payload(
                product_slug=product_slug,
                telegram_user_id=telegram_user_id,
                action="google_sheets_create",
                message_text=message_text,
                extra={
                    "title": artifact.title,
                    "values": artifact.values,
                    "freeze_rows": artifact.freeze_rows,
                    "column_widths": artifact.column_widths or [],
                    "bold_rows": artifact.bold_rows or [],
                    "currency_columns": artifact.currency_columns or [],
                    "approval_text": "Approved by user request in Telegram",
                },
            ),
        )
        url = str(result.get("spreadsheet_url") or "").strip()
        return f"Created Google Sheet: {artifact.title}\n{url or result.get('spreadsheet_id')}\nCredits used: {result.get('credits_spent', 0)}"
```

- [ ] **Step 4: Run tests to verify they pass**

Run the two tests. Expected: pass.

- [ ] **Step 5: Run adjacent finance tests**

Run:

```powershell
$env:PYTHONPATH='.'; uv run --with-requirements requirements.txt pytest bridge/tests/test_finance_workbench.py bridge/tests/test_telegram_webhook.py::test_finance_balance_sheet_request_creates_structured_google_sheet bridge/tests/test_telegram_webhook.py::test_finance_balance_sheet_request_tolerates_common_typos bridge/tests/test_telegram_webhook.py::test_finance_balance_sheet_request_asks_for_figures_before_google_sheet -q
```

Expected: pass.

- [ ] **Step 6: Commit workbench routing**

```powershell
git add bridge/app.py bridge/finance_workbench.py bridge/tests/test_finance_workbench.py bridge/tests/test_telegram_webhook.py
git commit -m "feat: route finance requests through workbench"
```

---

### Task 4: Add Razorpay Reconciliation Summary Workflow

**Files:**
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\app.py`
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\finance_workbench.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_telegram_webhook.py`

- [ ] **Step 1: Write failing test**

Add:

```python
def test_finance_razorpay_reconciliation_summarizes_payments(monkeypatch):
    # Mock Razorpay action result with paid/failed payments and minor-unit amounts.
    # Send: "pull Razorpay payments and reconcile this week"
    # Assert Telegram output has paid total, failed count, and top payments.
```

- [ ] **Step 2: Run test to verify it fails**

Expected: current output is a raw payment list, not a reconciliation summary.

- [ ] **Step 3: Implement summary formatter**

Add function:

```python
def summarize_razorpay_payments(items: list[dict[str, object]]) -> str:
    paid = [item for item in items if str(item.get("status") or "").lower() in {"captured", "paid", "authorized"}]
    failed = [item for item in items if str(item.get("status") or "").lower() in {"failed"}]
    total_minor = sum(int(item.get("amount") or 0) for item in paid)
    currency = str((paid[0] if paid else items[0]).get("currency") or "INR").upper() if items else "INR"
    total = total_minor / 100
    lines = [
        f"Razorpay reconciliation draft:",
        f"Collected: {currency} {total:,.2f}",
        f"Successful payments: {len(paid)}",
        f"Failed payments: {len(failed)}",
    ]
    return "\n".join(lines)
```

- [ ] **Step 4: Use summary in Razorpay branch**

Replace the raw list output in the Finance Agent branch with `summarize_razorpay_payments(items)`.

- [ ] **Step 5: Run test to verify it passes**

Run the focused test. Expected: pass.

- [ ] **Step 6: Commit Razorpay summary**

```powershell
git add bridge/app.py bridge/finance_workbench.py bridge/tests/test_telegram_webhook.py
git commit -m "feat: summarize finance payment reconciliation"
```

---

### Task 5: Add Finance Memory Use And Artifact State

**Files:**
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\finance_workbench.py`
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\app.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_finance_workbench.py`
- Test: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_telegram_webhook.py`

- [ ] **Step 1: Write failing tests**

Add tests for memory-driven output:

```python
def test_artifact_uses_company_currency_and_fiscal_year_from_memory():
    artifact = build_finance_sheet_artifact(
        "profit_and_loss",
        "make pnl revenue 50000 expenses 20000",
        memory_facts={"company": "GradeSense", "currency": "INR", "fiscal_year": "FY 2026-27"},
    )
    flat = " ".join(str(cell) for row in artifact.values for cell in row)
    assert artifact.title.startswith("GradeSense")
    assert "INR" in flat
    assert "FY 2026-27" in flat
```

- [ ] **Step 2: Implement memory fields in artifact builders**

Every builder should include company, currency, fiscal year, and assumptions if available.

- [ ] **Step 3: Store last artifact state**

After successful finance workbench connector action, store local facts:

```python
_store_user_memory_facts(
    product_slug=product_slug,
    telegram_user_id=telegram_user_id,
    facts={
        "last_finance_artifact_type": workflow.workflow,
        "last_finance_artifact_title": artifact.title,
        "last_finance_artifact_url": url or str(result.get("spreadsheet_id") or ""),
    },
)
```

Also sync to Founder Systems with `_sync_founder_systems_memory_facts`.

- [ ] **Step 4: Run memory tests**

Expected: pass.

- [ ] **Step 5: Commit memory integration**

```powershell
git add bridge/app.py bridge/finance_workbench.py bridge/tests/test_finance_workbench.py bridge/tests/test_telegram_webhook.py
git commit -m "feat: remember finance artifact context"
```

---

### Task 6: Deploy And Verify Live Finance Agent

**Files:**
- Runtime deploy only unless API changed.

- [ ] **Step 1: Run focused runtime tests**

```powershell
$env:PYTHONPATH='.'; uv run --with-requirements requirements.txt pytest bridge/tests/test_finance_workbench.py bridge/tests/test_telegram_webhook.py::test_finance_balance_sheet_request_creates_structured_google_sheet bridge/tests/test_telegram_webhook.py::test_finance_pnl_request_creates_professional_sheet bridge/tests/test_telegram_webhook.py::test_finance_runway_request_creates_professional_sheet -q
```

Expected: pass.

- [ ] **Step 2: Deploy runtime bridge**

```powershell
$envFile='F:\Work\FounderOS-Memory\.env'
$vars=@{}
Get-Content $envFile | ForEach-Object { if ($_ -match '^\s*([^#=]+)=(.*)$') { $vars[$matches[1].Trim()]=$matches[2].Trim().Trim('"') } }
$key=$vars['VM_SSH_KEY_PATH']
$remote="$($vars['AWS_VM_USER'])@$($vars['AWS_VM_HOST'])"
scp -i $key -o StrictHostKeyChecking=no F:\Work\Website\founder-agents-runtime\bridge\app.py "${remote}:/tmp/founder_agents_bridge_app.py"
scp -i $key -o StrictHostKeyChecking=no F:\Work\Website\founder-agents-runtime\bridge\finance_workbench.py "${remote}:/tmp/finance_workbench.py"
ssh -i $key -o StrictHostKeyChecking=no $remote "set -e; sudo cp /tmp/founder_agents_bridge_app.py /home/ayush/apps/founder-agents-runtime/bridge/app.py; sudo cp /tmp/finance_workbench.py /home/ayush/apps/founder-agents-runtime/bridge/finance_workbench.py; sudo chown ayush:ayush /home/ayush/apps/founder-agents-runtime/bridge/app.py /home/ayush/apps/founder-agents-runtime/bridge/finance_workbench.py; sudo systemctl restart founder-finance-agent; sleep 5; systemctl is-active founder-finance-agent"
```

- [ ] **Step 3: Health check**

```powershell
ssh -i $key -o StrictHostKeyChecking=no $remote "curl -fsS http://127.0.0.1:8402/health"
```

Expected: `{"ok":true,"service":"founder-agents-bridge"}`.

- [ ] **Step 4: Push runtime main**

```powershell
git push origin main
```

Expected: push succeeds.

---

## V1.5 Follow-Up Plan

Do after V1 is stable:

- Add invoice/photo OCR pipeline.
- Add Google Drive file intake.
- Add PromptDeck finance-section handoff.
- Add accounting app connectors as proposal-first tools.
- Add existing-file update flows for Sheets/Docs.
- Add multi-step task state so the agent can revise a previously created artifact instead of creating a new one every time.
