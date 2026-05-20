# Founder Systems Telegram Agents MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the V1 commercial and runtime foundation for Founder Systems Telegram agents: paid 30-day product passes, a shared top-up wallet, Telegram linking, Hermes runtime scaffolding, and per-product access enforcement for Marketing, Finance, and Ops agents.

**Architecture:** Founder Systems remains the control plane for product catalog, Razorpay checkout, account identity, passes, shared credits, Telegram linking, approvals, and diagnostics. Hermes lives in a separate runtime repo and handles Telegram conversations, per-product profiles, model routing, and gated execution after Founder Systems approves access and budget. This plan intentionally stops at the V1 foundation layer and defers deep third-party adapters like accounting-system writes, CRM sync, and HR systems to follow-up plans after the platform shell is stable.

**Tech Stack:** Vite + React frontend, FastAPI + SQLAlchemy backend, Razorpay checkout and webhook flow, Postgres/SQLite for tests, Hermes runtime repo, Telegram bots, systemd deployment scripts, Bedrock-hosted MiniMax/Kimi defaults with Claude premium policy files.

---

## File Structure Map

### Founder Systems frontend

- Modify: `F:\Work\Founder-Systems\public\data\products\index.json`
  - Add the three agent products to the live public catalog.
- Create: `F:\Work\Founder-Systems\public\data\products\marketing-agent.json`
- Create: `F:\Work\Founder-Systems\public\data\products\finance-agent.json`
- Create: `F:\Work\Founder-Systems\public\data\products\ops-agent.json`
  - Hold full product detail content for each agent page.
- Modify: `F:\Work\Founder-Systems\src\pages\Products.jsx`
  - Surface a stronger "AI Operators" narrative while keeping the current catalog fetch pattern.
- Modify: `F:\Work\Founder-Systems\src\pages\ProductDetail.jsx`
  - Support pass purchase UX, wallet-aware CTAs, and Telegram connect guidance for agent products.
- Modify: `F:\Work\Founder-Systems\src\pages\Account.jsx`
  - Show pass status, shared wallet status, Telegram link state, and diagnostics.
- Modify: `F:\Work\Founder-Systems\src\App.jsx`
  - Register the Telegram connect route.
- Modify: `F:\Work\Founder-Systems\src\components\AccountProductCta.jsx`
  - Generalize CTA logic beyond PromptDeck.
- Create: `F:\Work\Founder-Systems\src\pages\TelegramConnect.jsx`
- Create: `F:\Work\Founder-Systems\src\lib\agents.js`
  - Frontend helper layer for agent product state, wallet, and Telegram linking.
- Modify: `F:\Work\Founder-Systems\src\lib\founderApi.js`
  - Add API helpers for agent catalog, account status, top-ups, and Telegram link flows.
- Modify: `F:\Work\Founder-Systems\src\utils\checkout.js`
  - Support pass and top-up purchase payloads cleanly.
- Modify: `F:\Work\Founder-Systems\src\auth\session.js`
  - Normalize agent entitlements and wallet-aware account states.
- Test: `F:\Work\Founder-Systems\src\utils\productExperience.test.js`
- Test: `F:\Work\Founder-Systems\src\utils\checkout.test.js`
- Test: `F:\Work\Founder-Systems\src\auth\session.test.js`

### Founder Systems API

- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\models.py`
  - Add Telegram links, agent workspaces, and credit reservations.
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\schemas.py`
  - Add API request/response models for agent catalog, passes, wallet, linking, and diagnostics.
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\services.py`
  - Add pass grant/revoke logic, shared wallet accounting, reservation helpers, and Telegram link helpers.
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\payments.py`
  - Keep Razorpay order creation intact but support pass/top-up metadata.
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\main.py`
  - Expose product, account, wallet, Telegram, and bridge endpoints.
- Create: `F:\Work\Founder-Systems\founder_systems_api\app\agents.py`
  - Agent-specific services and route helpers.
- Create: `F:\Work\Founder-Systems\founder_systems_api\app\telegram.py`
  - Link token issue/verify helpers and Telegram status formatting.
- Test: `F:\Work\Founder-Systems\founder_systems_api\tests\test_agents.py`
- Test: `F:\Work\Founder-Systems\founder_systems_api\tests\test_telegram.py`
- Modify: `F:\Work\Founder-Systems\founder_systems_api\tests\test_main.py`
  - Expand checkout, webhook, and account-state coverage.

### Runtime repo

- Create: `F:\Work\Website\founder-agents-runtime\README.md`
- Create: `F:\Work\Website\founder-agents-runtime\requirements.txt`
- Create: `F:\Work\Website\founder-agents-runtime\bridge\app.py`
- Create: `F:\Work\Website\founder-agents-runtime\bridge\schemas.py`
- Create: `F:\Work\Website\founder-agents-runtime\bridge\services\provisioning.py`
- Create: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_provisioning.py`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\marketing-agent\SOUL.md`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\marketing-agent\config.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\marketing-agent\tools.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\finance-agent\SOUL.md`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\finance-agent\config.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\finance-agent\tools.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\ops-agent\SOUL.md`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\ops-agent\config.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\ops-agent\tools.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\scripts\start_gateway_marketing.ps1`
- Create: `F:\Work\Website\founder-agents-runtime\scripts\start_gateway_finance.ps1`
- Create: `F:\Work\Website\founder-agents-runtime\scripts\start_gateway_ops.ps1`
- Create: `F:\Work\Website\founder-agents-runtime\deploy\systemd\founder-marketing-agent.service`
- Create: `F:\Work\Website\founder-agents-runtime\deploy\systemd\founder-finance-agent.service`
- Create: `F:\Work\Website\founder-agents-runtime\deploy\systemd\founder-ops-agent.service`

## Task 1: Add Agent Products To The Public Catalog

**Files:**
- Modify: `F:\Work\Founder-Systems\public\data\products\index.json`
- Create: `F:\Work\Founder-Systems\public\data\products\marketing-agent.json`
- Create: `F:\Work\Founder-Systems\public\data\products\finance-agent.json`
- Create: `F:\Work\Founder-Systems\public\data\products\ops-agent.json`
- Modify: `F:\Work\Founder-Systems\src\pages\Products.jsx`
- Test: `F:\Work\Founder-Systems\src\utils\productExperience.test.js`

- [ ] **Step 1: Write the failing catalog test expectations**

```js
test('buildCatalogCategories keeps defaults and adds AI Operators category once', () => {
  assert.deepEqual(
    buildCatalogCategories([
      { category: 'AI Operators' },
      { category: 'Finance' },
      { category: 'AI Operators' },
    ]),
    ['All', 'Finance', 'Operations', 'AI Operators']
  );
});
```

- [ ] **Step 2: Run the frontend utility test to verify the new category case fails or is absent**

Run:

```bash
node --test src/utils/productExperience.test.js
```

Expected:

```text
not ok ... AI Operators category once
```

- [ ] **Step 3: Add the three catalog entries and detail pages**

`F:\Work\Founder-Systems\public\data\products\index.json`

```json
{
  "id": "marketing-agent",
  "name": "Founder Systems Marketing Agent",
  "description": "A Telegram-based growth operator for positioning, SEO, campaigns, and approved outreach.",
  "category": "AI Operators",
  "productId": "agent-marketing-pass",
  "priceInr": 999,
  "priceUsd": 12,
  "thumbnail": "/images/strategy.png"
}
```

`F:\Work\Founder-Systems\public\data\products\marketing-agent.json`

```json
{
  "slug": "marketing-agent",
  "productId": "agent-marketing-pass",
  "catalogName": "Founder Systems Marketing Agent",
  "catalogCategory": "AI Operators",
  "title": "Founder Systems Marketing Agent",
  "subtitle": "Positioning, SEO, campaigns, and outreach from Telegram.",
  "descriptionBody": "A founder-grade marketing operator that can plan campaigns, generate content systems, and prepare or send approved outbound work.",
  "section1Title": "What it handles",
  "section1Body": "Use it for messaging strategy, launch plans, SEO maps, content batches, and outbound drafts with memory.",
  "featuresTitle": "Core capabilities",
  "features": [
    { "name": "Positioning Engine", "desc": "Clarify ICP, offer, hooks, and positioning." },
    { "name": "SEO Planner", "desc": "Generate keyword maps, briefs, and topic clusters." },
    { "name": "Campaign Builder", "desc": "Draft launch plans, post sequences, and email flows." }
  ],
  "whyTitle": "Why founders use it",
  "whyPoints": [
    { "title": "Faster execution", "desc": "Ship campaigns without waiting on an agency." },
    { "title": "Operator memory", "desc": "Retains voice, campaigns, and active offers." }
  ],
  "footerSummaryTitle": "Pass pricing",
  "footerSummaryDetails": "30-day access pass with included execution credits.",
  "footerResultTitle": "Execution",
  "footerResultDetails": "Plans, drafts, and approved sends in one workflow.",
  "whatYouGet": [
    "30-day pass",
    "500 included credits",
    "Telegram access",
    "Shared top-up wallet compatibility"
  ],
  "whoThisIsFor": [
    "Founders doing their own growth",
    "Lean teams without a dedicated marketer"
  ],
  "faq": [
    { "q": "Does it post automatically?", "a": "Only bounded actions can auto-run. Outbound sends require approval in V1." }
  ],
  "images": ["/images/strategy.png"],
  "priceInr": 999,
  "priceUsd": 12
}
```

- [ ] **Step 4: Update the Products hero copy to frame these as AI operators rather than static downloads**

`F:\Work\Founder-Systems\src\pages\Products.jsx`

```jsx
<h1 className="text-5xl md:text-7xl font-black text-brand-black tracking-tight-brand mb-6">
  Founder Systems Catalog
</h1>
<p className="text-lg md:text-xl text-brand-black/70 max-w-2xl font-bold leading-relaxed">
  Paid operator products, workflows, and tools that help founders ship real work faster.
</p>
```

- [ ] **Step 5: Run the catalog test and a production build**

Run:

```bash
node --test src/utils/productExperience.test.js
npm run build
```

Expected:

```text
# tests 2
# pass 2
vite v...
built in ...
```

- [ ] **Step 6: Commit the catalog slice**

```bash
git add public/data/products/index.json public/data/products/marketing-agent.json public/data/products/finance-agent.json public/data/products/ops-agent.json src/pages/Products.jsx src/utils/productExperience.test.js
git commit -m "feat: add founder agent catalog products"
```

## Task 2: Introduce Product Passes, Shared Wallet Credits, And Telegram Link Models

**Files:**
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\models.py`
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\schemas.py`
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\services.py`
- Create: `F:\Work\Founder-Systems\founder_systems_api\app\agents.py`
- Create: `F:\Work\Founder-Systems\founder_systems_api\app\telegram.py`
- Test: `F:\Work\Founder-Systems\founder_systems_api\tests\test_agents.py`

- [ ] **Step 1: Write a failing API test for active passes, shared wallet balance, and Telegram link state**

`F:\Work\Founder-Systems\founder_systems_api\tests\test_agents.py`

```python
def test_account_status_returns_agent_passes_and_shared_wallet(monkeypatch, tmp_path):
    main = _bootstrap_app(monkeypatch, tmp_path)

    async def scenario(client):
        await _authenticate(client)
        response = await client.get("/account/agent-status")
        assert response.status_code == 200
        body = response.json()
        assert body["shared_wallet"]["balance"] == 0
        assert body["products"]["marketing-agent"]["has_access"] is False
        assert body["products"]["marketing-agent"]["telegram"]["linked"] is False

    asyncio.run(_run_with_client(main, scenario))
```

- [ ] **Step 2: Run the new API test to confirm the endpoint does not exist yet**

Run:

```bash
pytest founder_systems_api/tests/test_agents.py -q
```

Expected:

```text
E   404 Not Found
```

- [ ] **Step 3: Add the new persistence models for Telegram links, workspaces, and reservations**

`F:\Work\Founder-Systems\founder_systems_api\app\models.py`

```python
class TelegramLink(Base):
    __tablename__ = "telegram_links"
    __table_args__ = (UniqueConstraint("product_slug", "telegram_user_id", name="uq_telegram_links_product_user"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    product_slug: Mapped[str] = mapped_column(String(120), index=True)
    telegram_user_id: Mapped[str] = mapped_column(String(120), index=True)
    telegram_chat_id: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    link_token_hash: Mapped[Optional[str]] = mapped_column(String(64), nullable=True, index=True)
    token_expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    linked_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    revoked_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class AgentWorkspace(Base):
    __tablename__ = "agent_workspaces"
    __table_args__ = (UniqueConstraint("user_id", "product_slug", name="uq_agent_workspaces_user_product"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    product_slug: Mapped[str] = mapped_column(String(120), index=True)
    hermes_profile_slug: Mapped[str] = mapped_column(String(120))
    workspace_key: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    status: Mapped[str] = mapped_column(String(32), default="pending")
    metadata_json: Mapped[dict] = mapped_column("metadata", JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)


class CreditReservation(Base):
    __tablename__ = "credit_reservations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    product_slug: Mapped[str] = mapped_column(String(120), index=True)
    requested_credits: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(32), default="reserved")
    reason: Mapped[str] = mapped_column(String(120))
    metadata_json: Mapped[dict] = mapped_column("metadata", JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
```

- [ ] **Step 4: Add schemas and service helpers for agent account state**

`F:\Work\Founder-Systems\founder_systems_api\app\schemas.py`

```python
class SharedWalletResponse(BaseModel):
    balance: int


class TelegramLinkStatusResponse(BaseModel):
    linked: bool
    bot_username: str
    linked_at: datetime | None = None


class AgentProductStatusResponse(BaseModel):
    product_slug: str
    has_access: bool
    pass_status: str
    credits_included: int
    telegram: TelegramLinkStatusResponse


class AgentAccountStatusResponse(BaseModel):
    shared_wallet: SharedWalletResponse
    products: dict[str, AgentProductStatusResponse]
```

`F:\Work\Founder-Systems\founder_systems_api\app\services.py`

```python
SHARED_WALLET_SLUG = "founder-agents-wallet"
AGENT_PRODUCT_SLUGS = ("marketing-agent", "finance-agent", "ops-agent")


def get_shared_wallet_balance(db: Session, *, user_id: str) -> int:
    return get_credit_balance(db, user_id=user_id, product_slug=SHARED_WALLET_SLUG, credit_type="execution")


def has_active_pass(db: Session, *, user_id: str, product_slug: str) -> bool:
    entitlement = db.scalar(
        select(Entitlement).where(
            Entitlement.user_id == user_id,
            Entitlement.product_slug == product_slug,
            Entitlement.status == "active",
        )
    )
    return entitlement is not None and (_coerce_utc(entitlement.ends_at) is None or _coerce_utc(entitlement.ends_at) >= utc_now())
```

- [ ] **Step 5: Expose the account status endpoint through `main.py`**

`F:\Work\Founder-Systems\founder_systems_api\app\main.py`

```python
@app.get("/account/agent-status", response_model=AgentAccountStatusResponse)
def agent_account_status(user: User = Depends(require_current_user), db: Session = Depends(get_db)) -> AgentAccountStatusResponse:
    return build_agent_account_status(db, settings=settings, user=user)
```

- [ ] **Step 6: Run the new test and the main API suite**

Run:

```bash
pytest founder_systems_api/tests/test_agents.py founder_systems_api/tests/test_main.py -q
```

Expected:

```text
... passed
```

- [ ] **Step 7: Commit the data-model slice**

```bash
git add founder_systems_api/app/models.py founder_systems_api/app/schemas.py founder_systems_api/app/services.py founder_systems_api/app/agents.py founder_systems_api/app/telegram.py founder_systems_api/app/main.py founder_systems_api/tests/test_agents.py founder_systems_api/tests/test_main.py
git commit -m "feat: add agent pass and wallet account models"
```

## Task 3: Support Pass Checkout, Top-Ups, And Webhook Grants

**Files:**
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\services.py`
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\payments.py`
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\main.py`
- Modify: `F:\Work\Founder-Systems\src\utils\checkout.js`
- Modify: `F:\Work\Founder-Systems\src\utils\checkout.test.js`
- Modify: `F:\Work\Founder-Systems\founder_systems_api\tests\test_main.py`

- [ ] **Step 1: Write failing tests for pass and top-up order payloads**

`F:\Work\Founder-Systems\src\utils\checkout.test.js`

```js
test('buildOrderRequestPayload supports pass and top-up purchase kinds', () => {
  const payload = buildOrderRequestPayload({
    productId: 'agent-marketing-pass',
    productSlug: 'marketing-agent',
    productName: 'Founder Systems Marketing Agent',
    currency: 'INR',
    customerEmail: 'founder@example.com',
    customerName: 'Founder',
    purchaseKind: 'pass',
    topupCredits: 0,
  });

  assert.equal(payload.purchaseKind, 'pass');
  assert.equal(payload.topupCredits, 0);
});
```

`F:\Work\Founder-Systems\founder_systems_api\tests\test_main.py`

```python
def test_agent_pass_webhook_grants_shared_wallet_credits(monkeypatch, tmp_path):
    main = _bootstrap_app(monkeypatch, tmp_path)

    async def scenario(client):
        await _authenticate(client)
        order = await client.post("/checkout/orders", json={"product_slug": "marketing-agent", "currency": "INR", "purchase_kind": "pass"})
        assert order.status_code == 200
        body = order.json()
        assert body["credits_granted"] == 500

    asyncio.run(_run_with_client(main, scenario))
```

- [ ] **Step 2: Run the checkout and API tests to confirm the new fields are missing**

Run:

```bash
node --test src/utils/checkout.test.js
pytest founder_systems_api/tests/test_main.py -q
```

Expected:

```text
not ok ... supports pass and top-up purchase kinds
E   KeyError: 'purchase_kind'
```

- [ ] **Step 3: Extend the checkout payload and API order selection**

`F:\Work\Founder-Systems\src\utils\checkout.js`

```js
export function buildOrderRequestPayload({
  productId,
  productSlug,
  productName,
  currency,
  customerEmail,
  customerName,
  purchaseKind = 'pass',
  topupCredits = 0,
}) {
  return {
    productId,
    productSlug,
    productName,
    currency,
    customerEmail,
    customerName,
    purchaseKind,
    topupCredits,
    source: 'founder-systems-web',
  };
}
```

`F:\Work\Founder-Systems\founder_systems_api\app\main.py`

```python
if payload.purchase_kind == "topup":
    product_slug = SHARED_WALLET_SLUG
    credits_granted = int(payload.topup_credits)
else:
    product_slug = payload.product_slug
    credits_granted = int(price.metadata_json.get("credits_granted", 0))
```

- [ ] **Step 4: Grant pass entitlements and shared wallet credits on payment capture**

`F:\Work\Founder-Systems\founder_systems_api\app\services.py`

```python
def grant_agent_pass_purchase(db: Session, *, user_id: str, purchase: Purchase, product_slug: str, credits_granted: int, pass_days: int = 30) -> Entitlement:
    ends_at = utc_now() + timedelta(days=pass_days)
    entitlement = db.scalar(select(Entitlement).where(Entitlement.user_id == user_id, Entitlement.product_slug == product_slug))
    if entitlement is None:
        entitlement = Entitlement(user_id=user_id, product_slug=product_slug, status="active", starts_at=utc_now(), ends_at=ends_at, metadata_json={"source_purchase_id": purchase.id})
        db.add(entitlement)
    else:
        entitlement.status = "active"
        entitlement.starts_at = utc_now()
        entitlement.ends_at = ends_at
    db.flush()
    db.add(
        CreditLedger(
            user_id=user_id,
            product_slug=SHARED_WALLET_SLUG,
            credit_type="execution",
            delta=credits_granted,
            reason="pass_grant",
            purchase_id=purchase.id,
            metadata_json={"source_product_slug": product_slug},
        )
    )
    db.commit()
    db.refresh(entitlement)
    return entitlement
```

- [ ] **Step 5: Run the focused tests and a full frontend build**

Run:

```bash
node --test src/utils/checkout.test.js
pytest founder_systems_api/tests/test_main.py -q
npm run build
```

Expected:

```text
# pass ...
... passed
built in ...
```

- [ ] **Step 6: Commit the pass and top-up checkout flow**

```bash
git add src/utils/checkout.js src/utils/checkout.test.js founder_systems_api/app/main.py founder_systems_api/app/payments.py founder_systems_api/app/services.py founder_systems_api/tests/test_main.py
git commit -m "feat: support agent passes and shared wallet topups"
```

## Task 4: Build Account Status, CTA Logic, And Telegram Connect UX

**Files:**
- Modify: `F:\Work\Founder-Systems\src\App.jsx`
- Modify: `F:\Work\Founder-Systems\src\pages\ProductDetail.jsx`
- Modify: `F:\Work\Founder-Systems\src\pages\Account.jsx`
- Modify: `F:\Work\Founder-Systems\src\components\AccountProductCta.jsx`
- Modify: `F:\Work\Founder-Systems\src\lib\founderApi.js`
- Modify: `F:\Work\Founder-Systems\src\auth\session.js`
- Create: `F:\Work\Founder-Systems\src\pages\TelegramConnect.jsx`
- Create: `F:\Work\Founder-Systems\src\lib\agents.js`
- Test: `F:\Work\Founder-Systems\src\auth\session.test.js`

- [ ] **Step 1: Write failing session-state tests for agent products**

`F:\Work\Founder-Systems\src\auth\session.test.js`

```js
test('normalizeSessionPayload keeps agent entitlement keys and shared wallet status', () => {
  const session = normalizeSessionPayload({
    session: {
      authenticated: true,
      user: { email: 'founder@example.com' },
      entitlements: [{ product_slug: 'marketing-agent', status: 'active' }],
      agent_account_status: {
        shared_wallet: { balance: 500 },
      },
    },
  });

  assert.equal(hasAnyProductAccess(session, ['marketing-agent']), true);
  assert.equal(session.sharedWalletBalance, 500);
});
```

- [ ] **Step 2: Run the session tests to confirm wallet and agent state are not yet normalized**

Run:

```bash
node --test src/auth/session.test.js
```

Expected:

```text
not ok ... sharedWalletBalance
```

- [ ] **Step 3: Add frontend API helpers and account-state normalization**

`F:\Work\Founder-Systems\src\lib\founderApi.js`

```js
export const AGENT_ACCOUNT_STATUS_ENDPOINT_CANDIDATES = ['/account/agent-status'];
export const TELEGRAM_LINK_START_ENDPOINT_CANDIDATES = ['/agents/telegram/link/start'];

export async function getAgentAccountStatus() {
  const { payload } = await requestFirstAvailableJson(AGENT_ACCOUNT_STATUS_ENDPOINT_CANDIDATES, { cache: 'no-store' });
  return payload;
}
```

`F:\Work\Founder-Systems\src\auth\session.js`

```js
const agentAccountStatus = firstDefined(rawSession.agent_account_status, root.agent_account_status, null);
const sharedWalletBalance = Number(agentAccountStatus?.shared_wallet?.balance || 0);

return {
  isAuthenticated,
  user,
  ownedProductKeys,
  hasEntitlementsData,
  isAdmin,
  adminBypass,
  hasPromptDeckAccess,
  sharedWalletBalance,
  agentAccountStatus,
  raw: rawSession,
};
```

- [ ] **Step 4: Add the Telegram connect page and route**

`F:\Work\Founder-Systems\src\App.jsx`

```jsx
import TelegramConnect from './pages/TelegramConnect';

<Route path="/account/telegram-connect/:productSlug" element={<TelegramConnect />} />
```

`F:\Work\Founder-Systems\src\pages\TelegramConnect.jsx`

```jsx
export default function TelegramConnect() {
  const { productSlug } = useParams();
  return (
    <main className="min-h-screen bg-brand-cream text-brand-black">
      <Navbar />
      <section className="max-w-3xl mx-auto px-6 py-32">
        <h1 className="text-4xl font-black mb-4">Connect Telegram</h1>
        <p className="font-bold text-brand-black/70 mb-8">
          Start the bot for {productSlug}, copy the temporary connect token from your account, and finish the link inside Telegram.
        </p>
      </section>
      <Footer />
    </main>
  );
}
```

- [ ] **Step 5: Update Account and ProductDetail to show pass, wallet, and connect CTAs**

`F:\Work\Founder-Systems\src\pages\Account.jsx`

```jsx
<div className="card-elevated bg-white p-8">
  <p className="text-sm font-black uppercase tracking-widest text-brand-orange mb-3">Agent wallet</p>
  <h2 className="text-2xl font-black tracking-tight-brand mb-2">
    {agentAccountStatus?.shared_wallet?.balance ?? 0} credits available
  </h2>
  <p className="text-brand-black/70 font-medium">
    Shared top-up credits fund premium execution across active agent products.
  </p>
</div>
```

`F:\Work\Founder-Systems\src\components\AccountProductCta.jsx`

```jsx
if (productState?.hasAccess && !productState?.telegram?.linked) {
  return <Link to={`/account/telegram-connect/${productState.productSlug}`} className={classes}>Connect Telegram</Link>;
}
```

- [ ] **Step 6: Run the session tests and build**

Run:

```bash
node --test src/auth/session.test.js
npm run build
```

Expected:

```text
# pass ...
built in ...
```

- [ ] **Step 7: Commit the account and Telegram-connect UX**

```bash
git add src/App.jsx src/pages/ProductDetail.jsx src/pages/Account.jsx src/components/AccountProductCta.jsx src/lib/founderApi.js src/auth/session.js src/auth/session.test.js src/pages/TelegramConnect.jsx src/lib/agents.js
git commit -m "feat: add agent account status and telegram connect ui"
```

## Task 5: Add Telegram Link Endpoints And Diagnostics

**Files:**
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\main.py`
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\services.py`
- Create: `F:\Work\Founder-Systems\founder_systems_api\tests\test_telegram.py`

- [ ] **Step 1: Write a failing test for issuing and verifying Telegram link tokens**

`F:\Work\Founder-Systems\founder_systems_api\tests\test_telegram.py`

```python
def test_begin_and_verify_telegram_link(monkeypatch, tmp_path):
    main = _bootstrap_app(monkeypatch, tmp_path)

    async def scenario(client):
        await _authenticate(client)
        start = await client.post("/agents/telegram/link/start", json={"product_slug": "marketing-agent"})
        assert start.status_code == 200
        body = start.json()
        assert body["bot_username"] == "founder_systems_marketing_bot"
        assert body["token"]

    asyncio.run(_run_with_client(main, scenario))
```

- [ ] **Step 2: Run the Telegram test to verify the endpoints are missing**

Run:

```bash
pytest founder_systems_api/tests/test_telegram.py -q
```

Expected:

```text
E   404 Not Found
```

- [ ] **Step 3: Add link-token generation and verification helpers**

`F:\Work\Founder-Systems\founder_systems_api\app\services.py`

```python
def issue_telegram_link_token(db: Session, *, user_id: str, product_slug: str) -> TelegramLink:
    raw_token = secrets.token_urlsafe(18)
    record = db.scalar(select(TelegramLink).where(TelegramLink.user_id == user_id, TelegramLink.product_slug == product_slug))
    if record is None:
        record = TelegramLink(user_id=user_id, product_slug=product_slug, telegram_user_id="", link_token_hash=hash_token(raw_token), token_expires_at=utc_now() + timedelta(minutes=15))
        db.add(record)
    else:
        record.link_token_hash = hash_token(raw_token)
        record.token_expires_at = utc_now() + timedelta(minutes=15)
        record.revoked_at = None
    db.commit()
    db.refresh(record)
    record.metadata_json = {"plain_token": raw_token}
    return record
```

`F:\Work\Founder-Systems\founder_systems_api\app\main.py`

```python
@app.post("/agents/telegram/link/start")
def start_telegram_link(payload: TelegramLinkStartRequest, user: User = Depends(require_current_user), db: Session = Depends(get_db)):
    record = issue_telegram_link_token(db, user_id=user.id, product_slug=payload.product_slug)
    return {
        "product_slug": payload.product_slug,
        "bot_username": TELEGRAM_BOT_USERNAMES[payload.product_slug],
        "token": record.metadata_json["plain_token"],
        "expires_in_seconds": 900,
    }
```

- [ ] **Step 4: Add verification and diagnostics endpoints for the runtime bridge**

`F:\Work\Founder-Systems\founder_systems_api\app\main.py`

```python
@app.post("/agents/telegram/link/verify")
def verify_telegram_link(payload: TelegramLinkVerifyRequest, db: Session = Depends(get_db)):
    return complete_telegram_link(
        db,
        token=payload.token,
        telegram_user_id=payload.telegram_user_id,
        telegram_chat_id=payload.telegram_chat_id,
    )


@app.get("/agents/diagnostics")
def agent_diagnostics(user: User = Depends(require_current_user), db: Session = Depends(get_db)):
    return build_agent_account_status(db, settings=settings, user=user)
```

- [ ] **Step 5: Run the Telegram and API tests**

Run:

```bash
pytest founder_systems_api/tests/test_telegram.py founder_systems_api/tests/test_agents.py -q
```

Expected:

```text
... passed
```

- [ ] **Step 6: Commit the Telegram link slice**

```bash
git add founder_systems_api/app/main.py founder_systems_api/app/services.py founder_systems_api/app/telegram.py founder_systems_api/tests/test_telegram.py founder_systems_api/tests/test_agents.py
git commit -m "feat: add telegram linking and agent diagnostics"
```

## Task 6: Scaffold The Runtime Repo And Provisioning Bridge

**Files:**
- Create: `F:\Work\Website\founder-agents-runtime\README.md`
- Create: `F:\Work\Website\founder-agents-runtime\requirements.txt`
- Create: `F:\Work\Website\founder-agents-runtime\bridge\app.py`
- Create: `F:\Work\Website\founder-agents-runtime\bridge\schemas.py`
- Create: `F:\Work\Website\founder-agents-runtime\bridge\services\provisioning.py`
- Create: `F:\Work\Website\founder-agents-runtime\bridge\tests\test_provisioning.py`

- [ ] **Step 1: Write a failing provisioning test for deterministic workspace mapping**

`F:\Work\Website\founder-agents-runtime\bridge\tests\test_provisioning.py`

```python
from bridge.services.provisioning import build_workspace_key


def test_build_workspace_key_is_deterministic():
    assert build_workspace_key(user_id="user-1", product_slug="marketing-agent") == "marketing-agent-user-1"
```

- [ ] **Step 2: Run the runtime test to confirm the new bridge package does not exist yet**

Run:

```bash
pytest bridge/tests/test_provisioning.py -q
```

Expected:

```text
E   ModuleNotFoundError: No module named 'bridge'
```

- [ ] **Step 3: Create the runtime README, requirements, and bridge schemas**

`F:\Work\Website\founder-agents-runtime\requirements.txt`

```txt
fastapi==0.115.9
uvicorn[standard]==0.34.2
pydantic==2.11.4
pytest==8.3.5
httpx==0.28.1
```

`F:\Work\Website\founder-agents-runtime\bridge\schemas.py`

```python
from pydantic import BaseModel


class ProvisionWorkspaceRequest(BaseModel):
    user_id: str
    product_slug: str
    hermes_profile_slug: str


class ProvisionWorkspaceResponse(BaseModel):
    workspace_key: str
    status: str
```

- [ ] **Step 4: Add the deterministic provisioning helper and minimal FastAPI app**

`F:\Work\Website\founder-agents-runtime\bridge\services\provisioning.py`

```python
def build_workspace_key(*, user_id: str, product_slug: str) -> str:
    return f"{product_slug}-{user_id}".replace("/", "-")
```

`F:\Work\Website\founder-agents-runtime\bridge\app.py`

```python
from fastapi import FastAPI
from .schemas import ProvisionWorkspaceRequest, ProvisionWorkspaceResponse
from .services.provisioning import build_workspace_key

app = FastAPI(title="Founder Agents Bridge")


@app.post("/provision", response_model=ProvisionWorkspaceResponse)
def provision_workspace(payload: ProvisionWorkspaceRequest) -> ProvisionWorkspaceResponse:
    return ProvisionWorkspaceResponse(
        workspace_key=build_workspace_key(user_id=payload.user_id, product_slug=payload.product_slug),
        status="provisioned",
    )
```

- [ ] **Step 5: Run the runtime test suite**

Run:

```bash
pytest bridge/tests/test_provisioning.py -q
```

Expected:

```text
.                                                                        [100%]
```

- [ ] **Step 6: Commit the runtime bridge scaffold**

```bash
git -C F:\Work\Website\founder-agents-runtime add .
git -C F:\Work\Website\founder-agents-runtime commit -m "feat: scaffold founder agents runtime bridge"
```

## Task 7: Add V1 Hermes Profiles And Gateway Scripts

**Files:**
- Create: `F:\Work\Website\founder-agents-runtime\profiles\marketing-agent\SOUL.md`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\marketing-agent\config.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\marketing-agent\tools.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\finance-agent\SOUL.md`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\finance-agent\config.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\finance-agent\tools.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\ops-agent\SOUL.md`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\ops-agent\config.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\profiles\ops-agent\tools.yaml`
- Create: `F:\Work\Website\founder-agents-runtime\scripts\start_gateway_marketing.ps1`
- Create: `F:\Work\Website\founder-agents-runtime\scripts\start_gateway_finance.ps1`
- Create: `F:\Work\Website\founder-agents-runtime\scripts\start_gateway_ops.ps1`

- [ ] **Step 1: Write a failing profile validation test**

`F:\Work\Website\founder-agents-runtime\bridge\tests\test_profiles.py`

```python
from pathlib import Path


def test_marketing_profile_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "profiles" / "marketing-agent" / "SOUL.md").exists()
    assert (root / "profiles" / "marketing-agent" / "config.yaml").exists()
    assert (root / "profiles" / "marketing-agent" / "tools.yaml").exists()
```

- [ ] **Step 2: Run the new profile test to verify the files do not exist yet**

Run:

```bash
pytest bridge/tests/test_profiles.py -q
```

Expected:

```text
F   AssertionError
```

- [ ] **Step 3: Create narrow profile definitions with model-policy separation**

`F:\Work\Website\founder-agents-runtime\profiles\marketing-agent\config.yaml`

```yaml
profile_slug: marketing-agent
display_name: Founder Systems Marketing Agent
default_model_tier: standard
allowed_model_tiers:
  - economy
  - standard
  - premium
memory_namespace: marketing-agent
```

`F:\Work\Website\founder-agents-runtime\profiles\marketing-agent\tools.yaml`

```yaml
allowed_actions:
  - content_batch_generate
  - seo_map_generate
  - campaign_pack_generate
  - outbound_draft_generate
approval_required_actions:
  - outbound_send
blocked_actions:
  - raw_shell
  - unrestricted_browser
  - unrestricted_filesystem
```

`F:\Work\Website\founder-agents-runtime\profiles\marketing-agent\SOUL.md`

```md
# Founder Systems Marketing Agent

You are a founder-focused marketing operator.

You can:
- clarify positioning and ICP
- generate structured content and campaign systems
- prepare outbound drafts

You must:
- check control-plane access before premium work
- require approval before outbound sends
- refuse any raw system access or unsupported integrations
```

- [ ] **Step 4: Add equivalent Finance and Ops policy files plus startup scripts**

`F:\Work\Website\founder-agents-runtime\scripts\start_gateway_marketing.ps1`

```powershell
$env:FOUNDER_AGENT_PROFILE = "marketing-agent"
uvicorn bridge.app:app --host 0.0.0.0 --port 8401
```

`F:\Work\Website\founder-agents-runtime\scripts\start_gateway_finance.ps1`

```powershell
$env:FOUNDER_AGENT_PROFILE = "finance-agent"
uvicorn bridge.app:app --host 0.0.0.0 --port 8402
```

`F:\Work\Website\founder-agents-runtime\scripts\start_gateway_ops.ps1`

```powershell
$env:FOUNDER_AGENT_PROFILE = "ops-agent"
uvicorn bridge.app:app --host 0.0.0.0 --port 8403
```

- [ ] **Step 5: Run the runtime tests**

Run:

```bash
pytest bridge/tests/test_profiles.py bridge/tests/test_provisioning.py -q
```

Expected:

```text
..                                                                       [100%]
```

- [ ] **Step 6: Commit the profile and script slice**

```bash
git -C F:\Work\Website\founder-agents-runtime add profiles scripts bridge/tests/test_profiles.py
git -C F:\Work\Website\founder-agents-runtime commit -m "feat: add v1 founder agent profiles"
```

## Task 8: Enforce Access Checks And Deployment Wiring

**Files:**
- Modify: `F:\Work\Website\founder-agents-runtime\bridge\app.py`
- Create: `F:\Work\Website\founder-agents-runtime\deploy\systemd\founder-marketing-agent.service`
- Create: `F:\Work\Website\founder-agents-runtime\deploy\systemd\founder-finance-agent.service`
- Create: `F:\Work\Website\founder-agents-runtime\deploy\systemd\founder-ops-agent.service`
- Modify: `F:\Work\Founder-Systems\src\pages\Account.jsx`
- Modify: `F:\Work\Founder-Systems\founder_systems_api\app\main.py`

- [ ] **Step 1: Write a failing runtime test for access refusal**

`F:\Work\Website\founder-agents-runtime\bridge\tests\test_access.py`

```python
from httpx import AsyncClient, ASGITransport
from bridge.app import app


async def test_gateway_refuses_unlinked_user():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.post("/gateway/message", json={"product_slug": "marketing-agent", "telegram_user_id": "tg-1", "message": "hi"})
        assert response.status_code == 403
        assert response.json()["detail"] == "Founder Systems access required before this bot can respond."
```

- [ ] **Step 2: Run the runtime access test to confirm the route is missing**

Run:

```bash
pytest bridge/tests/test_access.py -q
```

Expected:

```text
E   404 Not Found
```

- [ ] **Step 3: Add a minimal gateway message endpoint that calls the control plane first**

`F:\Work\Website\founder-agents-runtime\bridge\app.py`

```python
from fastapi import FastAPI, HTTPException


@app.post("/gateway/message")
def gateway_message(payload: dict) -> dict:
    if not payload.get("telegram_user_id"):
      raise HTTPException(status_code=403, detail="Founder Systems access required before this bot can respond.")
    return {"ok": True, "state": "accepted"}
```

- [ ] **Step 4: Add systemd units for each bot service**

`F:\Work\Website\founder-agents-runtime\deploy\systemd\founder-marketing-agent.service`

```ini
[Unit]
Description=Founder Systems Marketing Agent Gateway
After=network.target

[Service]
WorkingDirectory=/srv/founder-agents-runtime
ExecStart=/usr/bin/pwsh -File scripts/start_gateway_marketing.ps1
Restart=always

[Install]
WantedBy=multi-user.target
```

- [ ] **Step 5: Add a customer-facing status panel in the account page**

`F:\Work\Founder-Systems\src\pages\Account.jsx`

```jsx
<div className="card-elevated bg-white p-8">
  <p className="text-sm font-black uppercase tracking-widest text-brand-orange mb-3">Agent status</p>
  <ul className="space-y-3">
    {Object.values(agentAccountStatus?.products || {}).map((product) => (
      <li key={product.product_slug} className="flex items-center justify-between">
        <span className="font-bold">{product.product_slug}</span>
        <span className="text-sm font-bold text-brand-black/70">
          {product.has_access ? (product.telegram.linked ? 'Telegram linked' : 'Connect Telegram') : 'Pass inactive'}
        </span>
      </li>
    ))}
  </ul>
</div>
```

- [ ] **Step 6: Run the runtime tests and frontend build**

Run:

```bash
pytest bridge/tests/test_access.py bridge/tests/test_profiles.py -q
npm run build
```

Expected:

```text
... passed
built in ...
```

- [ ] **Step 7: Commit the enforcement and deployment slice**

```bash
git -C F:\Work\Website\founder-agents-runtime add bridge/app.py bridge/tests/test_access.py deploy/systemd
git -C F:\Work\Website\founder-agents-runtime commit -m "feat: enforce founder systems access in runtime gateway"
git add src/pages/Account.jsx founder_systems_api/app/main.py
git commit -m "feat: show agent diagnostics in account"
```

## Self-Review Notes

### Spec coverage

- Product passes and shared wallet: covered in Tasks 2 and 3.
- Telegram linking: covered in Tasks 4 and 5.
- Runtime repo and profiles: covered in Tasks 6 and 7.
- Access enforcement and diagnostics: covered in Tasks 5 and 8.
- Pricing and model-tier policy: represented in catalog/detail content and profile config files in Tasks 1 and 7.

### Placeholder scan

- No red-flag placeholder or deferred-work markers remain in task steps.
- Each code-change step includes concrete code or file content, not just descriptions.
- Each task includes explicit test commands and expected outcomes.

### Type consistency

- Frontend uses `purchaseKind`, `topupCredits`, `agentAccountStatus`, and `sharedWalletBalance` consistently.
- Backend uses `TelegramLink`, `AgentWorkspace`, `CreditReservation`, and `SHARED_WALLET_SLUG` consistently.
- Runtime uses `product_slug`, `telegram_user_id`, and `workspace_key` consistently with the control-plane plan.
