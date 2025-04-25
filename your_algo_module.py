# your_algo_module.py

import requests

def fetch_realtime_stock_data(symbol):
    """
    Fetch real-time stock data from indianstockapi.com
    """
    url = f"https://indianstockapi.com/api/stock_info?ticker={symbol.upper()}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f"Failed to fetch data for {symbol}"}
    except Exception as e:
        return {'error': str(e)}


def get_filtered_stocks():
    """
    Replace this temporary list with dynamic fetching when available.
    """
    test_symbols = ["TCS", "INFY", "RELIANCE", "HDFCBANK", "ICICIBANK"]
    filtered = []

    for symbol in test_symbols:
        data = fetch_realtime_stock_data(symbol)
        if "error" not in data:
            try:
                price = float(data.get("price", 0))
                volume = int(data.get("volume", 0))

                # Example logic: pick stocks with price > 500 and volume > 1L
                if price > 500 and volume > 100000:
                    filtered.append({
                        "symbol": symbol,
                        "price": price,
                        "volume": volume
                    })
            except:
                continue
    return filtered
