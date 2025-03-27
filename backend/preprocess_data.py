import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Load your dataset (replace with your actual path)
data = pd.read_csv('/Users/marvin/Documents/GitHub/Multi-Agent-AI-for-Stock-Trading-and-Market-Analysis/backend/data/stock_data.csv')


# Check for missing values
print(f"Missing values:\n{data.isnull().sum()}")

# Drop or fill missing values
data = data.dropna()

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

