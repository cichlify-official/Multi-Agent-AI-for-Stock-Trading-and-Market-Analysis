import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the stock and period
ticker = "AAPL"  # You can change this to any ticker you want
period = "1y"    # Options: '1d', '5d', '1mo', '3mo', '1y', '5y', 'max'

# Download historical data
data = yf.download(ticker, period=period)

# Show the first few rows
print("📊 First 5 rows of data:")
print(data.head())

# Summary statistics
print("\n📈 Summary statistics:")
print(data.describe())

# Check for missing values
print("\n🔍 Missing values:")
print(data.isnull().sum())

# Plot the closing price over time
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f"{ticker} Stock Price Over {period}")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

# Simple Moving Average (SMA)
data['SMA20'] = data['Close'].rolling(window=20).mean()
data['SMA50'] = data['Close'].rolling(window=50).mean()

# Relative Strength Index (RSI)
delta = data['Close'].diff(1)
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
data['RSI'] = 100 - (100 / (1 + rs))

# Moving Average Convergence Divergence (MACD)
ema12 = data['Close'].ewm(span=12, adjust=False).mean()
ema26 = data['Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = ema12 - ema26
data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

# Show the latest data with indicators
print("📊 Latest Data with Indicators:")
print(data[['Close', 'SMA20', 'SMA50', 'RSI', 'MACD', 'Signal_Line']].tail())

# Plotting the indicators
plt.figure(figsize=(14, 8))

# Price with SMA
plt.subplot(3, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['SMA20'], label='SMA20', color='orange', linestyle='--')
plt.plot(data['SMA50'], label='SMA50', color='green', linestyle='--')
plt.title(f"{ticker} Close Price with SMAs")
plt.legend()
plt.grid(True)

# RSI
plt.subplot(3, 1, 2)
plt.plot(data['RSI'], label='RSI', color='purple')
plt.axhline(70, color='red', linestyle='--', linewidth=1)  # Overbought
plt.axhline(30, color='green', linestyle='--', linewidth=1)  # Oversold
plt.title("Relative Strength Index (RSI)")
plt.legend()
plt.grid(True)

# MACD
plt.subplot(3, 1, 3)
plt.plot(data['MACD'], label='MACD', color='magenta')
plt.plot(data['Signal_Line'], label='Signal Line', color='black', linestyle='--')
plt.title("MACD & Signal Line")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
