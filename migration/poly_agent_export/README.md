# Poly Agent Export (Sanitized) + V2 Scaffold

This directory stores the sanitized migration package published on 2026-04-22.

## Why this exists

- Preserve the extracted Polymarket agent material in GitHub safely.
- Keep secrets out of source control.
- Start a cleaner `polymarket_v2` implementation in parallel.

## Contents

- `.env.example` and `.gitignore` safety baseline
- `ARCHITECTURE_AND_V2_PLAN.md` migration analysis
- `polymarket_v2/` scaffold modules for app/domain/strategy/execution/connectors/api

## Binance roadmap

`polymarket_v2/connectors/binance_account.py` is intentionally read-only scaffold logic first.
Signed endpoint support and account/order operations should be added only after risk guards and tests are in place.
