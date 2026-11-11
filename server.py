from mcp.server.fastmcp import FastMCP

from tools.stock_info import get_stock_info as stock_function
from tools.gold_price import get_gold_price as gold_function
from tools.usd_rate import get_usd_rate as dollar_function

mcp = FastMCP("Finance Server")


@mcp.tool()
def get_stock_info(symbol: str) -> dict:
    """دریافت اطلاعات یک نماد بورسی ایران از TSETMC."""
    return stock_function(symbol)


@mcp.tool()
def get_gold_price() -> dict:
    """دریافت قیمت جهانی هر انس طلا به دلار."""
    return gold_function()


@mcp.tool()
def get_usd_rate() -> dict:
    """دریافت نرخ دلار به تومان از Navasan."""
    return dollar_function()


if __name__ == "__main__":
    mcp.run()
