import pandas as pd

# Assuming you have already loaded the data into df
def preprocess_data(df):
    # Convert 'Close' column to numeric values, coerce errors to NaN
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    # Handle missing values (e.g., fill NaNs with the previous value)
    df['Close'] = df['Close'].fillna(method='ffill')

    # Calculate 10-day Simple Moving Average (SMA)
    df['SMA_10'] = df['Close'].rolling(window=10).mean()

    return df

# Example usage
df = pd.read_excel('data/Stock_Data.xlsx')  # Replace with your data source
df = preprocess_data(df)
print(df.head())  # Print the first few rows to check the output
