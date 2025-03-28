import numpy as np
from tensorflow import keras
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Define paths
model_path = "/Users/marvin/Documents/GitHub/Multi-Agent-AI-for-Stock-Trading-and-Market-Analysis/models/stock_model.keras"

# Load the model
model = keras.models.load_model(model_path)

# Load or create test data (replace with actual test data)
X_test = np.random.rand(10, 60, 4)  # Replace with your real test data
y_test = np.random.rand(10)          # Replace with actual target values

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"✅ Mean Absolute Error (MAE): {mae}")
print(f"✅ Mean Squared Error (MSE): {mse}")
print(f"✅ Root Mean Squared Error (RMSE): {rmse}")
