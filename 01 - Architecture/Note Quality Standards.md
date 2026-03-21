# Note Quality Standards

Every note in the vault should have a status tag to help agents know what to trust.

## Status Tags
- `status: draft` — rough notes, may be incomplete or inaccurate
- `status: verified` — reviewed and confirmed accurate
- `status: outdated` — was accurate but needs update
- `status: live` — actively maintained, reflects current state

## Freshness
- `updated: YYYY-MM-DD` — when the note was last meaningfully updated
- Notes older than 30 days without update should be reviewed

## Confidence
- `confidence: high` — based on direct observation or testing
- `confidence: medium` — based on docs or second-hand info
- `confidence: low` — speculative or unverified

## How Agents Should Use This
1. When retrieving context, prefer `verified` and `live` notes over `draft`
2. Flag `outdated` notes to the user when encountered
3. When writing new notes, always include status + updated date
4. During periodic reviews, update status tags

## Current Note Status Audit
| Folder | Notes | Needs Review |
|--------|-------|--------------|
| 00 - Home | Dashboard, Vision | Vision needs status tag |
| 01 - Architecture | 5 files | Architecture Overview = live, Memory Layer = live |
| 02 - Workflows | 5 files | Workflow Index = live, others need update |
| 03 - Products | 4 files | Website Schema = live, Outcomes = live |
| 04 - Skills | 1 file | Skill Registry = live |
| 06 - Logs | 3 files | All live (auto-updated) |
| 08 - Resources | 5 files | All verified |