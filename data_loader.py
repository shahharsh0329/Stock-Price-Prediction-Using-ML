import yfinance as yf
import pandas as pd
# data_loader.py

import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date, save_path=None):
    """Fetch historical stock data from Yahoo Finance and save it as Excel (optional)."""
    df = yf.download(ticker, start=start_date, end=end_date)
    
    if save_path:
        df.to_excel(save_path)
    
    return df

# Example usage
if __name__ == "__main__":
    df = fetch_stock_data("RELIANCE.NS", "2020-01-01", "2024-01-01", "data/Stock_Data.xlsx")
    print(df.head())  # Print the first 5 rows to verify it's working
