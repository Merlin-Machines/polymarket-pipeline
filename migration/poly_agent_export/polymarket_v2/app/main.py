from polymarket_v2.app.settings import load_settings
from polymarket_v2.connectors.binance_account import BinanceAccountClient
from polymarket_v2.connectors.polymarket_gamma import PolymarketGammaProvider
from polymarket_v2.execution.dry_run_broker import DryRunBroker
from polymarket_v2.strategies.weather_ranges import WeatherRangesStrategy


def run_once() -> None:
    settings = load_settings()
    market_provider = PolymarketGammaProvider()
    strategy = WeatherRangesStrategy(
        edge_threshold=settings.edge_threshold,
        max_trade_usd=settings.max_trade_usd,
    )
    broker = DryRunBroker()
    binance = BinanceAccountClient(
        api_key=settings.binance_api_key,
        api_secret=settings.binance_api_secret,
    )

    print(f"[{settings.app_name}] dry_run={settings.dry_run} env={settings.env}")
    print(f"[binance] {binance.status().reason}")
    print("[markets] fetching...")
    markets = list(market_provider.fetch_markets())
    print(f"[markets] loaded={len(markets)}")

    opportunities = strategy.find_opportunities(markets)
    print(f"[strategy] opportunities={len(opportunities)}")
    for item in opportunities[:5]:
        order_id = broker.place(item)
        print(
            f"[order] {order_id} market={item.market_id} side={item.side.value} "
            f"edge={item.edge:.2%} size=${item.size_usd:.2f}"
        )


if __name__ == "__main__":
    run_once()
