# BillScout Agent — API Reference

## REST Endpoints (Optional FastAPI layer)

### POST /scan

Upload a receipt image and get extracted data.

```
curl -X POST http://localhost:8000/scan \
  -F "image=@receipt.jpg" \
  -F "user_id=test_user"
```

**Response:**
```json
{
  "success": true,
  "merchant": "Woolworths",
  "amount": 85.50,
  "date": "2026-06-02T14:30:00",
  "category": "groceries",
  "confidence": 0.92,
  "price_suggestions": [...]
}
```

### GET /expenses

Query user expenses.

```
GET /expenses?user_id=test_user&start=2026-06-01&end=2026-06-30&category=groceries
```

**Response:**
```json
{
  "expenses": [...],
  "total": 412.30,
  "count": 12
}
```

### POST /bank/connect

Initiate bank connection OAuth flow.

```
POST /bank/connect
{"user_id": "test_user", "bank_id": "au_woolworths"}
```

**Response:**
```json
{"auth_url": "https://yourservice.com/oauth/..."}
```

### GET /digest

Get current week's expense digest.

```
GET /digest?user_id=test_user
```

### GET /health

Health check.

```
GET /health
{"status": "ok", "skills": ["receipt_ocr", "bank_sync", "expense_tracker", "price_lookup"]}
```

## WebSocket (Agent Chat Interface)

Connect to `/ws/chat/{user_id}` for natural language queries.

**Send:**
```json
{"message": "how much did I spend on dining last month?"}
```

**Receive:**
```json
{
  "reply": "You spent $156.80 on dining last month — that's 18.5% of your total expenses. 📊",
  "data": {"total": 156.80, "category": "dining"}
}
```
