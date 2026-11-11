import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_usd_rate() -> dict:
    """
    نرخ دلار را از Navasan دریافت می‌کند.

    Returns:
        دیکشنری شامل نرخ فروش دلار به تومان و زمان به‌روزرسانی.

    Raises:
        ValueError: اگر کلید API تنظیم نشده باشد یا نرخ دلار در پاسخ نباشد.
    """
    api_key = os.getenv("NAVASAN_API_KEY")

    if not api_key:
        raise ValueError("کلید NAVASAN_API_KEY تنظیم نشده است.")

    url = "https://api.navasan.tech/latest/"
    response = requests.get(
        url,
        params={"api_key": api_key},
        timeout=10
    )
    response.raise_for_status()
    data = response.json()

    # در پاسخ‌های رایج Navasan، نرخ دلار زیر کلید usd قرار دارد.
    usd_info = data.get("usd") or data.get("usd_sell") or data.get("usd_buy")

    if not usd_info:
        raise ValueError("اطلاعات دلار در پاسخ Navasan وجود ندارد.")

    raw_value = usd_info.get("value")
    if raw_value is None:
        raw_value = usd_info.get("price")

    if raw_value is None:
        raise ValueError("مقدار نرخ دلار در پاسخ Navasan پیدا نشد.")

    # مستندات Navasan نرخ‌ها را ریالی معرفی می‌کند؛ برای خروجی تومان تقسیم بر 10 می‌کنیم.
    usd_sell_toman = float(raw_value) / 10

    return {
        "usd_sell_toman": usd_sell_toman,
        "last_update": usd_info.get("date"),
    }
