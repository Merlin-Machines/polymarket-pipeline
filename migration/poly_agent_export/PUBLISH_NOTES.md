# Poly Agent Export Publish Notes

Published via Codex on 2026-04-22 to preserve a safe, travel-friendly copy.

## Included

- Sanitized environment template (`.env.example`)
- Architecture map and V2 migration plan
- Initial `polymarket_v2` scaffold (dry-run safe)

## Intentionally not included

- Raw secret-bearing `.env` from the original export

## Next steps

1. Continue migrating legacy strategy/execution logic into `polymarket_v2` modules.
2. Add signed Polymarket CLOB connector guarded by `LIVE_TRADING_ENABLED=true`.
3. Add Binance account adapter (read-only first, then signed endpoints).
