# 💹 MCP Finance Server

## 🎯 Overview

This project is a Python-based **MCP (Model Context Protocol) server** that provides financial data through three tools.

It allows AI assistants to access stock market information, global gold prices, and USD exchange rates using a unified interface.

## 🔌 What is MCP?

MCP (Model Context Protocol) is a standard that allows AI applications to communicate with external tools and data sources.

In this project, the MCP server connects an AI assistant to financial APIs and services, enabling it to retrieve and process real-time financial information.

## 🛠️ Available Tools

The server provides three main tools:

| Tool | Description | Data Source |
|---|---|---|
| `get_stock_info(symbol)` | Retrieves stock market information for Iranian companies | TSETMC |
| `get_gold_price()` | Retrieves the global gold price per ounce in USD | Gold API |
| `get_usd_rate()` | Retrieves the USD exchange rate in Iranian Toman | Navasan API |

## 📊 Example Scenario: Estimating the 18K Gold Price

One of the main use cases of this project is estimating the price of one gram of 18-karat gold in Iran.

The AI assistant calls the gold price and USD exchange rate tools, then calculates the estimated price using the following formulas:

**Step 1: Calculate the 24K gold price per gram**

```python
gold_24k = (gold_price_usd / 31.1) * usd_rate
```

**Step 2: Calculate the 18K gold price per gram**

```python
gold_18k = gold_24k * 0.75
```

If either API request fails, the assistant must report the error instead of calculating an estimated price.

## 📁 Project Structure

```text
mcp_finance_server/
│
├── server.py
├── requirements.txt
├── test_tools.py
├── prompt_template.py
├── .env.example
├── README.md
│
├── tools/
│   ├── __init__.py
│   ├── stock_info.py
│   ├── gold_price.py
│   └── usd_rate.py
│
└── schemas/
    ├── stock_info_schema.json
    ├── gold_price_schema.json
    └── usd_rate_schema.json
```

## ⚙️ Technologies

- **Python** – Main programming language
- **MCP** – Communication between AI assistants and external tools
- **FastMCP** – Building and running the MCP server
- **Requests** – Sending HTTP requests to external APIs
- **pytse-client** – Retrieving Iranian stock market data
- **python-dotenv** – Managing environment variables

## 🚀 Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/USERNAME/MCP-Finance-Server.git
cd MCP-Finance-Server
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Configure the API key**

Create a `.env` file in the project root and add your Navasan API key:

```env
NAVASAN_API_KEY=your_api_key_here
```

**6. Run the MCP server**

```bash
python server.py
```

## ⚠️ Notes and Limitations

- The USD exchange rate tool requires a valid Navasan API key.
- The project depends on external APIs, so availability and response formats may change.
- The estimated 18K gold price is a mathematical estimate based on the global gold price and USD exchange rate. It does not include local market premiums, taxes, or other trading costs.
- Never upload your `.env` file or API keys to GitHub.

## 📝 Conclusion

This project demonstrates how MCP can connect AI assistants to external financial data sources.

It provides a simple foundation for building AI-powered financial applications that can retrieve market data, combine information from multiple APIs, and perform basic financial calculations.
