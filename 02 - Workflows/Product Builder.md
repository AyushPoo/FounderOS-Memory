# Product Builder

Last refreshed: `2026-05-10`

## Current status

| Field | Value |
|-------|-------|
| Workflow name | `Product Builder` |
| Workflow ID | `vo7WHaL6rq7yKRvm` |
| Active | No |
| Role | Historical planner/orchestrator workflow |

## Interpretation

The older `Product Builder` workflow should no longer be treated as the live center of the system. The current active automation layer is spread across:

- `Build Product Bridge`
- the active `Builder - *` workflows
- `Quality Gate`
- `GitHub Publisher`
- `Website Publisher`
- `Product Publisher`

## Practical conclusion

- Do not assume the old Azure GPT planner notes are still true.
- Treat this page as a legacy pointer, not an implementation guide.
- If Product Builder is intended to come back, it needs a fresh redesign around the AWS stack and current publishing flow.
