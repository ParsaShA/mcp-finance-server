import requests


def get_gold_price() -> dict:
    """
    قیمت جهانی هر انس طلا را به دلار دریافت می‌کند.

    Returns:
        دیکشنری شامل نماد طلا، قیمت دلاری هر انس، نام و زمان به‌روزرسانی.
    """
    url = "https://api.gold-api.com/price/XAU"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    return {
        "symbol": data["symbol"],
        "price_usd_per_ounce": float(data["price"]),
        "name": data.get("name", "Gold"),
        "last_update": data.get("updatedAt"),
    }
