import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_stock_data(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            data[ticker] = stock.history(start=start_date, end=end_date)['Close']
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return pd.DataFrame(data)