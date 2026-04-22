from typing import Iterable
import requests

from polymarket_v2.domain.models import Market


class PolymarketGammaProvider:
    def __init__(self, timeout_seconds: int = 12) -> None:
        self.timeout_seconds = timeout_seconds

    def fetch_markets(self) -> Iterable[Market]:
        response = requests.get(
            "https://gamma-api.polymarket.com/markets",
            params={"active": "true", "closed": "false", "limit": 100, "tag_slug": "weather"},
            timeout=self.timeout_seconds,
        )
        response.raise_for_status()
        raw_markets = response.json()
        markets: list[Market] = []
        for item in raw_markets:
            outcomes = item.get("outcomes") or []
            prices = item.get("outcomePrices") or []
            token_ids = item.get("clobTokenIds") or []
            if len(outcomes) < 2 or len(prices) < 2 or len(token_ids) < 2:
                continue
            try:
                yes_index = next(i for i, name in enumerate(outcomes) if name.lower() == "yes")
                no_index = next(i for i, name in enumerate(outcomes) if name.lower() == "no")
            except StopIteration:
                continue
            try:
                markets.append(
                    Market(
                        market_id=str(item.get("id", "")),
                        question=str(item.get("question", "")),
                        yes_price=float(prices[yes_index]),
                        no_price=float(prices[no_index]),
                        yes_token_id=str(token_ids[yes_index]),
                        no_token_id=str(token_ids[no_index]),
                        liquidity=float(item.get("liquidity") or 0.0),
                        hours_to_expiry=24.0,
                        symbol="WEATHER",
                    )
                )
            except (TypeError, ValueError):
                continue
        return markets
