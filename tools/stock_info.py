from datetime import datetime
from typing import Any

import pytse_client as tse


def get_stock_info(symbol: str) -> dict[str, Any]:
    """
    اطلاعات یک نماد بورسی ایران را از TSETMC برمی‌گرداند.

    Args:
        symbol: نماد سهم، مثل «فولاد».

    Returns:
        دیکشنری شامل نماد، نام شرکت، قیمت، درصد تغییر، حجم، ارزش بازار و زمان به‌روزرسانی.

    Raises:
        ValueError: اگر نماد واردشده پیدا نشود یا اطلاعات اصلی آن موجود نباشد.
    """
    if not symbol or not symbol.strip():
        raise ValueError("نماد سهم نمی‌تواند خالی باشد.")

    try:
        ticker = tse.Ticker(symbol.strip())
    except ValueError:
        raise ValueError(f"نماد «{symbol}» در TSETMC پیدا نشد.")

    try:
        realtime = ticker.get_ticker_real_time_info_response()

        if realtime.last_price is None:
            raise ValueError(f"قیمت لحظه‌ای نماد «{symbol}» در دسترس نیست.")

        yesterday_price = realtime.yesterday_price
        if yesterday_price:
            change_percent = (
                (realtime.last_price - yesterday_price) / yesterday_price
            ) * 100
        else:
            change_percent = 0.0

        update_time = realtime.last_date or realtime.date_time
        if update_time is None:
            update_time = datetime.now()

        # قیمت‌های خام TSETMC بر حسب ریال هستند؛ اینجا به تومان تبدیل می‌شوند.
        last_price_toman = float(realtime.last_price) / 10

        market_cap = ticker.market_cap
        if market_cap is not None:
            market_cap = float(market_cap) / 10

        return {
            "symbol": symbol.strip(),
            "name": str(ticker.title),
            "last_price": last_price_toman,
            "price_change_percent": float(change_percent),
            "volume": int(realtime.volume or 0),
            "market_cap": market_cap,
            "last_update": update_time.isoformat(),
        }

    except ValueError:
        raise
    except Exception as error:
        raise RuntimeError(f"دریافت اطلاعات نماد «{symbol}» ناموفق بود: {error}")
