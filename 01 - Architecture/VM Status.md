# 🖥️ VM Status

## Connection
- **IP:** 34.14.219.64
- **Provider:** GCP (Google Cloud Platform)
- **Access:** SSH password auth
- **nip.io URL:** https://34.14.219.64.nip.io

## Resources (as of 2026-03-18)
| Resource | Value | Status |
|----------|-------|--------|
| Disk | 9.2GB / 9.7GB | 🔴 100% FULL |
| n8n RAM | 658MB | ⚠️ High |
| PM2 | Running (5 days uptime) | ✅ |
| PostgreSQL | Running | ✅ |

## ⚠️ Critical: Disk Full
The VM disk is completely full. This WILL cause:
- n8n crashes
- Failed workflow executions
- Database corruption risk

### Fix — Delete duplicate skill repos:
```bash
# These are 3 copies of the same repo:
rm -rf /home/ayushpoojary1/founder-os-skills/everything-claude-code
rm -rf /home/ayushpoojary1/founder-os/skill-repos/everything-claude-code
# Keep only /home/ayushpoojary1/founder-os/skills/everything-claude-code
```

This should free ~2-3GB immediately.

## Running Processes
- **PM2:** God Daemon managing n8n
- **n8n:** Main workflow engine (PID tracked by PM2)
- **n8n task-runner:** Separate process for code execution
- **PostgreSQL:** Chat memory database

## Last Checked
2026-03-18T09:46:00Z by OpenClaw agent
