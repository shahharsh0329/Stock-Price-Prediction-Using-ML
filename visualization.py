import matplotlib.pyplot as plt
import pandas as pd

def plot_stock_data(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['SMA_10'], label='10-day SMA')
    plt.title('Stock Price and 10-day Moving Average')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

# Assuming df is preprocessed and available
import pandas as pd
import matplotlib.pyplot as plt

def preprocess_data(df):
    # Your preprocessing steps here (e.g., handling missing values, calculating SMA)
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df['Close'] = df['Close'].fillna(method='ffill')
    df['SMA_10'] = df['Close'].rolling(window=10).mean()
    return df

# Now call it in your script
df = pd.read_excel('data/Stock_Data.xlsx')  # Replace with your data source
df = preprocess_data(df)

plot_stock_data(df)