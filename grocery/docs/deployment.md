# BillScout Agent — Deployment Guide

## Docker

```bash
# Build image
docker build -t bill-scout-agent .

# Run with env
docker run -d \
  --name bill-scout \
  -p 8000:8000 \
  -v $(pwd)/data:/app/data \
  -e BASIQ_API_KEY=your_key \
  -e DISCORD_BILL_SCOUT_WEBHOOK=your_webhook \
  bill-scout-agent
```

## Docker Compose

```yaml
services:
  bill-scout:
    build: .
    volumes:
      - ./data:/app/data
    env_file:
      - .env
    restart: unless-stopped
```

## Railway / Render / Fly.io

- Set environment variables via dashboard
- Use Dockerfile above
- Mount persistent volume for `data/` directory

## Cron Jobs

```bash
# Weekly digest every Sunday at 9am AEST
0 9 * * 0 cd /app && python -m src.weekly_digest

# Bank sync daily at 6am
0 6 * * * cd /app && python -m src.bank.sync --all-users
```

## Health Check

```bash
curl http://localhost:8000/health
# Expected: {"status": "ok", "skills": ["receipt_ocr", "bank_sync", "expense_tracker"]}
```
