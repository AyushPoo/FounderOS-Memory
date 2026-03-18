# 🔍 Ideas Fetcher

## Overview
Scrapes 9 internet sources in parallel, deduplicates titles, ranks top 7 ideas using Gemini, stores results in Google Sheets.

## Configuration
- **Workflow ID:** pkTIpthafQ88wkAy
- **Trigger:** Called by [[Founder OS Agent]]
- **LLM:** Google Gemini (ranking)
- **Output:** Google Sheets "Founder Systems Ideas" (Sheet1)

## Sources Scraped
| # | Source | URL | Type |
|---|--------|-----|------|
| 1 | Product Hunt | producthunt.com/feed | RSS/HTML |
| 2 | Hacker News Ask | hnrss.org/ask | RSS |
| 3 | Indie Hackers | indiehackers.com/feed | RSS |
| 4 | GitHub Trending | github.com/trending?since=daily | HTML |
| 5 | Gumroad Discover | gumroad.com/discover | HTML |
| 6 | Reddit r/startups | pullpush.io API | JSON |
| 7 | Reddit r/microsaas | pullpush.io API | JSON |
| 8 | Reddit r/Entrepreneur | pullpush.io API | JSON |
| 9 | Reddit r/SaaS | pullpush.io API | JSON |

## Processing Pipeline
1. 9 parallel HTTP requests
2. HTML extraction (titles + links)
3. Merge all results
4. Take first 10 items
5. Deduplicate, limit to 20 unique titles
6. Send to Gemini for scoring:
   - Feasibility (1-10)
   - Revenue potential (1-10)
   - Ease of building for non-technical founder (1-10)
   - Total score = average
7. Return top 7 ranked ideas
8. Parse into structured data
9. Clear Google Sheet → Write new data
10. Return formatted ideas list

## Scoring Criteria
Gemini prioritizes ideas that can be built as:
- Excel templates
- Notion templates
- Google Sheets tools
- Dashboards
- Simple micro-SaaS

## Google Sheet
- **Doc ID:** 1-K6e8o2SprYeoBFOAnNdOG-JEGaqPW7uT7Qu3J4YTtk
- **Sheet:** Sheet1 (current batch) / Saved Ideas (bookmarked)
- **Columns:** Index, Name, Description, Score, Timestamp

## Issues
- [ ] Clears entire sheet each run — loses history
- [ ] Some sources may fail silently (no error handling)
- [ ] Reddit API (pullpush.io) reliability unknown
