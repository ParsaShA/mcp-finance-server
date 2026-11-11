پروژه ساده MCP مالی

1) نصب Python 3.11 یا بالاتر
2) ساخت محیط مجازی:
   python -m venv venv

3) فعال‌سازی در ویندوز:
   venv\Scripts\activate

   فعال‌سازی در Linux و macOS:
   source venv/bin/activate

4) نصب کتابخانه‌ها:
   pip install -r requirements.txt

5) فایل .env.example را به .env تغییر نام بدهید و کلید Navasan را در آن قرار دهید:
   NAVASAN_API_KEY=کلید_شما

6) تست مستقیم ابزارها:
   python test_tools.py

7) اجرای MCP Server:
   python server.py

سرور با روش stdio اجرا می‌شود و برای اتصال به کلاینت MCP مناسب است.
برای دیدن ابزارها و آزمایش فراخوانی آن‌ها می‌توانید از MCP Inspector استفاده کنید:
   npx -y @modelcontextprotocol/inspector

در تنظیمات کلاینت MCP مانند Claude Desktop، مسیر کامل python و server.py را وارد کنید.
نمونه تنظیم ویندوز:
{
  "mcpServers": {
    "finance": {
      "command": "C:\\PATH\\TO\\venv\\Scripts\\python.exe",
      "args": ["C:\\PATH\\TO\\mcp_finance_server\\server.py"]
    }
  }
}

نکته واحدها:
- خروجی قیمت سهم و نرخ دلار در این پروژه تومان است.
- داده خام TSETMC و Navasan به ریال دریافت می‌شود و در کد بر 10 تقسیم می‌شود.
- قیمت طلا در gold-api به دلار برای هر انس است.
- فرمول قیمت طلا فقط تخمینی است و هزینه‌های بازار داخلی را ندارد.

Schemaها:
در پوشه schemas سه فایل JSON Schema قرار دارد. این فایل‌ها برای مستندسازی ورودی ابزارها هستند.
در خود MCP، SDK ورودی ابزارها را از روی Type Hint تابع‌ها می‌سازد.
