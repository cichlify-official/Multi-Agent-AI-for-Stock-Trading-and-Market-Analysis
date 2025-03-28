import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Load your dataset (replace with your actual path)
data = pd.read_csv('/Users/marvin/Documents/GitHub/Multi-Agent-AI-for-Stock-Trading-and-Market-Analysis/backend/data/stock_data.csv')

# Check for missing values
print(f"Missing values before cleanup:\n{data.isnull().sum()}")

# Convert all numeric columns to float, coercing errors to NaN
data[['Open', 'High', 'Low', 'Volume', 'Close']] = data[['Open', 'High', 'Low', 'Volume', 'Close']].apply(pd.to_numeric, errors='coerce')

# Drop rows with any NaN values
data = data.dropna()

# Verify missing values again
print(f"\nMissing values after cleanup:\n{data.isnull().sum()}")

# Define the features and target
features = data[['Open', 'High', 'Low', 'Volume']]
target = data['Close']

# Initialize the scaler
scaler = MinMaxScaler(feature_range=(0, 1))

# Fit and transform the features
scaled_features = scaler.fit_transform(features)

# Combine scaled features with the target
processed_data = np.hstack((scaled_features, target.values.reshape(-1, 1)))

# Save processed data for training
np.save('processed_data.npy', processed_data)

print("✅ Data preprocessing complete. Saved as 'processed_data.npy'")
