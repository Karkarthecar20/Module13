

def fetch_daily_stock_prices(api_key, ticker_symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker_symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        time_series = data.get("Time Series (Daily)", {})
        for date, prices in time_series.items():
            print(f"Date: {date}")
            print(f"Open: {prices['1. open']}")
            print(f"High: {prices['2. high']}")
            print(f"Low: {prices['3. low']}")
            print(f"Close: {prices['4. close']}")
            print(f"Volume: {prices['5. volume']}")
            print("-" * 20)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def fetch_latest_stock_price(api_key, ticker_symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker_symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        time_series = data.get("Time Series (Daily)", {})
        if time_series:
            latest_date = max(time_series.keys())
            latest_prices = time_series[latest_date]
            print(f"Latest Date: {latest_date}")
            print(f"Open: {latest_prices['1. open']}")
            print(f"High: {latest_prices['2. high']}")
            print(f"Low: {latest_prices['3. low']}")
            print(f"Close: {latest_prices['4. close']}")
            print(f"Volume: {latest_prices['5. volume']}")
        else:
            print("No time series data found.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def main():
    api_key = "3LAUO6JIF3GH81KT"
    ticker_symbol = input("Enter ticker symbol: ")
    fetch_latest_stock_price(api_key, ticker_symbol)

if __name__ == "__main__":
    main()