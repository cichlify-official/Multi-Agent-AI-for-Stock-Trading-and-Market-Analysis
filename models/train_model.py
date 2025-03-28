import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import os

# Define file path
data_path = '/Users/marvin/Documents/GitHub/Multi-Agent-AI-for-Stock-Trading-and-Market-Analysis/processed_data.npy'

# Load Data
if not os.path.exists(data_path):
    raise FileNotFoundError(f"❌ File not found: {data_path}")

X = np.load(data_path)
print(f"✅ Data loaded successfully. Shape: {X.shape}")

# Check total elements and expected shape
total_elements = X.size  # Total number of elements
print(f"Total elements: {total_elements}")

# Define sequence and feature dimensions
sequence_length = 60
num_features = 4
required_elements = sequence_length * num_features  # 60 * 4 = 240

# Find nearest multiple of required_elements
nearest_multiple = (total_elements // required_elements) * required_elements
print(f"Trimming data to {nearest_multiple} elements.")

# Trim and reshape
X = X.flatten()[:nearest_multiple]  # Flatten and trim excess elements
X = X.reshape(-1, sequence_length, num_features)
print(f"✅ Reshaped data: {X.shape}")

# Define target variable
y = np.random.rand(X.shape[0])  # Replace with actual target data if available

# Train/Test Split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"✅ Data shapes — X_train: {X_train.shape}, y_train: {y_train.shape}")

# Define LSTM Model
model = Sequential()
model.add(LSTM(50, return_sequences=False, input_shape=(sequence_length, num_features)))
model.add(Dense(1))  # Single output for regression

# Compile Model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])

# Train the Model
history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=20,
    batch_size=32,
    verbose=1
)

# Save the Model
model_save_path = '/Users/marvin/Documents/GitHub/Multi-Agent-AI-for-Stock-Trading-and-Market-Analysis/models/stock_model.kera'
model_save_path = "/Users/marvin/Documents/GitHub/Multi-Agent-AI-for-Stock-Trading-and-Market-Analysis/models/stock_model.keras"
model.save(model_save_path)
print(f"🎉 Model training complete and saved at {model_save_path}!")
