# Bank Setup Guide (Australia)

## Basiq (Recommended)

### 1. Get API Key

1. Sign up at https://basiq.io
2. Go to Dashboard → API Key
3. Copy your `BX8...` key

### 2. Institution Coverage

Basiq supports 120+ AU institutions including:
- Major: Commonwealth, ANZ, Westpac, NAB, BNZ
- Retail: ING, Macquarie, Suncorp
- Mutual: Bank of Queensland, Bendigo Bank, Heritage Bank
- Digital: Up Bank, 86400, Alex Bank

### 3. OAuth Flow

The user selects their bank → redirected to Basiq → user authenticates with their bank → returns with auth code → BillScout exchanges for access token.

### 4. Rate Limits

| Tier | Requests/min | Requests/day |
|------|--------------|--------------|
| Free | 15 | 500 |
| Starter | 60 | 5,000 |
| Pro | 120 | 50,000 |

**Mitigation:** Cache institution lists, batch transaction fetches.

## Plaid (AU Coverage)

Plaid has limited AU support — works for some institutions but not all. Use Basiq as primary.

## Salt Edge

Good for EU + AU coverage. Alternate option if Basiq rate limits are hit.

## Security Notes

- Never store raw bank credentials
- Access tokens are encrypted at rest (AES-256)
- Refresh tokens rotated on each use
- User can revoke access at any time via bank portal
