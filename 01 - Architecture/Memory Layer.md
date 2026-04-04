# ð§  Memory Layer â Architecture & Status

> Last updated: 2026-03-20 â v2.0 LIVE â

## Overview

Custom self-hosted memory stack. Fully operational as of 2026-03-20.

---

## Stack

| Component | Tech | Location | Status |
|-----------|------|----------|--------|
| Vector DB | Qdrant | `localhost:6333` | â Running |
| Memory Server | FastAPI `custom_memory.py` v2.0 | `localhost:8000` | â Running (PM2: custom-memory) |
| Embedding Model | `all-MiniLM-L6-v2` | In-process | â 384-dim Cosine |
| LLM | Gemini 2.5 Flash | Google API | â Working |
| Bulk Indexer | `obsidian_sync.py` | VM home dir | One-shot, run manually |

**Gemini API key notes:**
- Key has IP restriction â Azure VM IPv4 and IPv6 must be allowlisted (both were added 2026-03-21)
- Use model: `gemini-2.5-flash` (1.5-flash, 2.0-flash, 2.0-flash-lite all deprecated for new users)
- GCP VM IPs (34.14.219.64 etc.) are no longer relevant â GCP VM decommissioned 2026-04-04

---

## Qdrant Collections

| Collection | Points | Notes |
|------------|--------|-------|
| `founder_memory` | 32+ | â Active |
| `mem0` | 0 | Legacy, unused |
| `mem0migrations` | â | Legacy, unused |

---

## API Endpoints (v2.0)

| Endpoint | Method | Input | Output | Status |
|----------|--------|-------|--------|--------|
| `/` | GET | â | `{status, version}` | â |
| `/add` | POST | `{messages, user_id}` | Chunks + upserts to Qdrant | â Fixed |
| `/upsert` | POST | `{file_path, content}` | Chunks + upserts by stable ID | â |
| `/search` | POST | `{query, user_id}` | `{results: [{text, source, score}]}` | â Fixed |
| `/query` | POST | `{query, top_k}` | `{results, count}` | â New |
| `/agent` | POST | `{input, user_id}` | `{response, memory_used, sources}` | â New |

---

## Chunking & Deduplication

- Files split into ~600 token chunks (2400 chars) with 240 char overlap
- Each chunk ID = `md5(file_path + "::chunk_" + index)` â stable across re-runs
- Same file pushed again = upsert in place, no duplicates

---

## Data Flow (Current)

```
GitHub push
    â GitHub Sync (n8n workflow 3HdXFHlJ6CI1iiPj)
    â fetch raw .md content
    â Build Payload (file_path + content)
    â POST /upsert â chunked â Qdrant â

obsidian_sync.py (manual, one-shot)
    â full vault â Qdrant (32 notes, no chunking â legacy)
```

---

## /agent â FounderOS Brain

```
User query
    â embed query â Qdrant search (top 5 chunks)
    â build context from results
    â Gemini 2.5 Flash prompt
    â structured response: Insight / Actions / Risks
    â store interaction back to Qdrant
```

**Test result (2026-03-20):**
Query: "What is the current status of the product builder workflow?"
â memory_used: 5 chunks from Workflow Index, Product Builder, Dashboard, Idea Pipeline
â Response accurate, referenced correct broken nodes and missing connections

**Next:** Wire /agent to Telegram as `/ask` command entry point

---

## GitHub Sync Workflow

**ID:** `3HdXFHlJ6CI1iiPj` | Active â

Pipeline calls `/upsert` with `{file_path, content}` â correct, chunked, deduplicated.
