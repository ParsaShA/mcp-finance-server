from tools.stock_info import get_stock_info
from tools.gold_price import get_gold_price
from tools.usd_rate import get_usd_rate


if __name__ == "__main__":
    print("Stock test:")
    print(get_stock_info("فولاد"))

    print("\nGold test:")
    print(get_gold_price())

    print("\nDollar test:")
    print(get_usd_rate())
