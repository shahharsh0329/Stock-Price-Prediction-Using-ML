import pandas as pd
from src.data_loader import fetch_stock_data
from src.preprocessing import preprocess_data 
from src.visualization import plot_stock_price 
from src.model import train_model

# Define Stock Parameters
ticker = "RELIANCE.NS"
start_date = "2020-01-01"
end_date = "2024-01-01"
save_path = "data/Stock_Data.xlsx"

# Step 1: Fetch Stock Data
df = fetch_stock_data(ticker, start_date, end_date, save_path)

# Step 2: Preprocess Data
df = preprocess_data(df)

# Step 3: Visualize Data
plot_stock_price(df, ticker)

# Step 4: Train Model
model, y_test, y_pred = train_model(df)
