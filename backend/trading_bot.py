import yfinance as yf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def get_data(ticker, period="1y", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    data.dropna(inplace=True)
    return data

def preprocess_data(data):
    features = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)
    return scaled_data, scaler

def run_bot(ticker):
    data = get_data(ticker)
    if data.empty:
        return {"error": "No data found for this ticker."}

    scaled_data, scaler = preprocess_data(data)
    
    # Convert scaled data back to a readable format just to show something useful
    df = pd.DataFrame(scaled_data, columns=['Open', 'High', 'Low', 'Close', 'Volume'])
    df["Date"] = data.index.strftime("%Y-%m-%d")
    
    return df.tail(30)  # Return only the last 30 entries for demo
