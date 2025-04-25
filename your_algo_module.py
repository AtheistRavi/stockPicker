import yfinance as yf
import requests

# Fetch stock symbols from NSE
def fetch_nse_stock_symbols():
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.nseindia.com/"
    }
    try:
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)  # set cookies
        response = session.get(url, headers=headers, timeout=10)
        data = response.json()
        symbols = [item["symbol"] for item in data["data"]]
        return symbols
    except Exception as e:
        print("Error fetching stock symbols:", e)
        return ["RELIANCE", "INFY", "TCS"]  # fallback list

# Get stock data using yfinance
def get_realtime_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol + ".NS")  # NSE symbols
        data = stock.history(period="1d", interval="5m")
        if not data.empty:
            price = round(data['Close'].iloc[-1], 2)
            # Example static metrics — replace with real fetch if needed
            pe = 20
            de_ratio = 0.4
            return price, pe, de_ratio
        return None, None, None
    except Exception as e:
        print(f"Error fetching data for {symbol}:", e)
        return None, None, None

# Filter stocks based on PE and D/E
def get_filtered_stocks():
    stock_symbols = fetch_nse_stock_symbols()
    filtered_stocks = []
    for symbol in stock_symbols:
        price, pe, de_ratio = get_realtime_stock_data(symbol)
        if price and pe < 25 and de_ratio < 0.6:
            filtered_stocks.append({
                "symbol": symbol,
                "price": price,
                "pe": pe,
                "de_ratio": de_ratio
            })
    filtered_stocks.sort(key=lambda x: x["price"], reverse=True)
    return filtered_stocks
