import matplotlib.pyplot as plt
import pandas as pd

def plot_stock_data(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['SMA_10'], label='10-day SMA')
    plt.title('Stock Price and 10-day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

# Assuming df is preprocessed and available
df = pd.read_excel('data/Stock_Data.xlsx')  # Replace with your data source
df = preprocess_data(df)  # Assuming you have a preprocessing function
plot_stock_data(df)
