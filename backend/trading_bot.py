import yfinance as yf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Load stock data
def get_data(ticker, period="1y", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    data.dropna(inplace=True)
    return data

# Preprocess data
def preprocess_data(data):
    # Selecting features
    features = data[['Open', 'High', 'Low', 'Close', 'Volume']]

    # Scaling the features
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)
    
    return scaled_data, scaler

# Main function
if __name__ == "__main__":
    ticker = "AAPL"
    data = get_data(ticker)
    print("Raw Data:\n", data.head())

    scaled_data, scaler = preprocess_data(data)
    print("Scaled Data:\n", scaled_data[:5])
