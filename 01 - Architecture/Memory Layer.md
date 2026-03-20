# 🧠 Memory Layer — Architecture & Status

> Last updated: 2026-03-20

## Overview

The memory system has been fully migrated away from Mem0 (hosted) to a **custom self-hosted stack** using Qdrant + FastAPI + sentence-transformers. This gives full control over storage, retrieval logic, chunking, and deduplication.

---

## Stack

| Component | Tech | Location | Purpose |
|-----------|------|----------|---------|
| Vector DB | Qdrant | `localhost:6333` | Stores embeddings |
| Memory Server | FastAPI (`custom_memory.py`) | `localhost:8000` | API layer |
| Embedding Model | `all-MiniLM-L6-v2` (sentence-transformers) | In-process | 384-dim vectors |
| Bulk Indexer | `obsidian_sync.py` | VM home dir | One-shot GitHub → Qdrant import |

**Legacy files (unused):**
- `mem0_server.py` — old Mem0-based server, no longer in use

---

## Qdrant Collections

| Collection | Points | Notes |
|------------|--------|-------|
| `founder_memory` | 32 | ✅ Active — all Obsidian notes indexed |
| `mem0` | 0 | Empty, legacy |
| `mem0migrations` | — | Legacy |

---

## custom_memory.py — Current Server

**Running on port 8000 via PM2**

### Endpoints

| Endpoint | Method | Input | Purpose |
|----------|--------|-------|---------|
| `/` | GET | — | Health check |
| `/add` | POST | `{messages, user_id}` | Adds text to in-memory store (NOT Qdrant) ⚠️ |
| `/search` | POST | `{query, user_id}` | Searches memory + Qdrant |
| `/upsert` | POST | `{file_path, content}` | Upserts a file into Qdrant by hash ID |

### /add — Known Bug
`/add` stores to a **local Python list** — NOT Qdrant.
- Data is lost on server restart
- GitHub Sync workflow currently calls `/add` — this data is not persisted to Qdrant

**Fix needed:** Route `/add` through Qdrant upsert.

### /search — Known Bug
Returns mixed types — empty objects for Qdrant results because of a key mismatch:
- `obsidian_sync.py` stores payload as `{text, source}`
- `custom_memory.py` reads `payload.get("content")` and `payload.get("file")` — wrong keys

**Fix needed:** Change to read `payload.get("text")` and `payload.get("source")`.

### /upsert — Correct but unused
Only endpoint that correctly writes to Qdrant. Nothing calls it yet.

---

## obsidian_sync.py — Bulk Indexer

One-shot script: walks GitHub repo, downloads all .md files, embeds full content, stores in Qdrant.

**Known issues:**
- No chunking — full file per vector (degrades quality for large files)
- No deduplication — re-running calls `recreate_collection` (wipes everything)
- IDs are sequential integers — unstable across re-runs

---

## Data Flow (Current)

```
GitHub push
    → GitHub Sync (n8n)
    → POST /add  ← goes to memory_store (lost on restart)
    (nothing reaches Qdrant from live pushes)

obsidian_sync.py (manual, one-shot)
    → Qdrant founder_memory (32 notes) ← real data lives here
```

---

## What Needs to Be Built

### Priority 1 — Fix /search (30 min)
Change `payload.get("content")` → `payload.get("text")`
Change `payload.get("file")` → `payload.get("source")`

### Priority 2 — Fix /add persistence (1 hr)
Route to Qdrant upsert. Use `md5(source + chunk_index)` as stable point ID.

### Priority 3 — Chunking (2 hr)
Split .md files into 500–800 token chunks before embedding.
Metadata per chunk: `{source, chunk_id, chunk_index, total_chunks}`.

### Priority 4 — Deduplication (1 hr)
Deterministic IDs per chunk. Delete old chunks before re-insert on update.

### Priority 5 — /query endpoint (1 hr)
Clean retrieval: `{query, top_k}` → `[{text, source, score}]`

### Priority 6 — /agent endpoint (2–3 hr)
User query → retrieve context → Gemini Flash → structured output → Telegram.

---

## GitHub Sync Workflow

**ID:** `3HdXFHlJ6CI1iiPj` | Active

Current pipeline calls `/add` — needs to be switched to `/upsert` with `{file_path, content}` to actually write to Qdrant.
