# VM Status

Last refreshed: `2026-05-10`

## Primary production host: AWS EC2

| Field | Value |
|-------|-------|
| Public IP | `52.87.13.200` |
| Internal hostname | `ip-172-31-29-50` |
| OS | Ubuntu on AWS, kernel `7.0.0-1004-aws` |
| Edge | nginx on `80/443` |
| Database | Postgres `18-main` on `127.0.0.1:5432` |
| PromptDeck API | `127.0.0.1:8011` |
| PromptDeck legacy API | `127.0.0.1:8090` |
| Founder Systems shared API | `127.0.0.1:8010` |
| Open Design | `127.0.0.1:7456` |
| Qdrant | `:6333` |
| `openclaw` | `:7890` |
| `paperclip` | `127.0.0.1:3100` |
| `n8n` | `:5678` |

## Systemd services verified running

- `founder-systems-api.service`
- `promptdeck-api.service`
- `promptdeck-legacy.service`
- `nginx.service`
- `postgresql@18-main.service`

## PM2 services verified running

- `atlas-api`
- `founder-agent`
- `memory-api`
- `analytics-api`
- `litellm-proxy`
- `n8n`
- `paperclip`

## Docker containers verified running

- `promptdeck-design-engine`
- `qdrant`

## Legacy host: Azure VM

| Field | Value |
|-------|-------|
| Public IP | `20.193.252.82` |
| Current role | Legacy / rollback only |
| Active production dependency | None verified after AWS cutover |

## Important note

The Azure VM still matters operationally only until the team explicitly decides rollback is no longer needed. It should not be treated as the active primary host anymore.
