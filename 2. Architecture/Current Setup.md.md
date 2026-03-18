# Current Setup

## Infrastructure
- VM running with pm2 (always on)
- n8n deployed and active

## Active Workflows
- Idea scraper (working)
- Telegram bot connected to n8n

## Tools Being Used
- Antigravity (development)
- Gemini API
- ChatGPT
- Browser-based agents

## Current Flow
Telegram → n8n → LLM → Output

## Issues
- No persistent memory
- Context lost across tools
- Repeated prompting required