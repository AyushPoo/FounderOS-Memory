# 🧠 Memory Layer — Architecture & Status

> Last updated: 2026-03-20 — v2.0 LIVE ✅

## Overview

Custom self-hosted memory stack. Fully operational as of 2026-03-20.

---

## Stack

| Component | Tech | Location | Status |
|-----------|------|----------|--------|
| Vector DB | Qdrant | `localhost:6333` | ✅ Running |
| Memory Server | FastAPI `custom_memory.py` v2.0 | `localhost:8000` | ✅ Running (PM2: custom-memory) |
| Embedding Model | `all-MiniLM-L6-v2` | In-process | ✅ 384-dim Cosine |
| LLM | Gemini 2.5 Flash | Google API | ✅ Working |
| Bulk Indexer | `obsidian_sync.py` | VM home dir | One-shot, run manually |

**Gemini API key notes:**
- Key has IP restriction — both IPv4 (`34.14.219.64`) and IPv6 (`fda3:e722:ac3:10:57:b85c:a62:20b1`) must be allowed
- Use model: `gemini-2.5-flash` (1.5-flash, 2.0-flash, 2.0-flash-lite all deprecated for new users)

---

## Qdrant Collections

| Collection | Points | Notes |
|------------|--------|-------|
| `founder_memory` | 32+ | ✅ Active |
| `mem0` | 0 | Legacy, unused |
| `mem0migrations` | — | Legacy, unused |

---

## API Endpoints (v2.0)

| Endpoint | Method | Input | Output | Status |
|----------|--------|-------|--------|--------|
| `/` | GET | — | `{status, version}` | ✅ |
| `/add` | POST | `{messages, user_id}` | Chunks + upserts to Qdrant | ✅ Fixed |
| `/upsert` | POST | `{file_path, content}` | Chunks + upserts by stable ID | ✅ |
| `/search` | POST | `{query, user_id}` | `{results: [{text, source, score}]}` | ✅ Fixed |
| `/query` | POST | `{query, top_k}` | `{results, count}` | ✅ New |
| `/agent` | POST | `{input, user_id}` | `{response, memory_used, sources}` | ✅ New |

---

## Chunking & Deduplication

- Files split into ~600 token chunks (2400 chars) with 240 char overlap
- Each chunk ID = `md5(file_path + "::chunk_" + index)` — stable across re-runs
- Same file pushed again = upsert in place, no duplicates

---

## Data Flow (Current)

```
GitHub push
    → GitHub Sync (n8n workflow 3HdXFHlJ6CI1iiPj)
    → fetch raw .md content
    → Build Payload (file_path + content)
    → POST /upsert → chunked → Qdrant ✅

obsidian_sync.py (manual, one-shot)
    → full vault → Qdrant (32 notes, no chunking — legacy)
```

---

## /agent — FounderOS Brain

```
User query
    → embed query → Qdrant search (top 5 chunks)
    → build context from results
    → Gemini 2.5 Flash prompt
    → structured response: Insight / Actions / Risks
    → store interaction back to Qdrant
```

**Test result (2026-03-20):**
Query: "What is the current status of the product builder workflow?"
→ memory_used: 5 chunks from Workflow Index, Product Builder, Dashboard, Idea Pipeline
→ Response accurate, referenced correct broken nodes and missing connections

**Next:** Wire /agent to Telegram as `/ask` command entry point

---

## GitHub Sync Workflow

**ID:** `3HdXFHlJ6CI1iiPj` | Active ✅

Pipeline calls `/upsert` with `{file_path, content}` — correct, chunked, deduplicated.
