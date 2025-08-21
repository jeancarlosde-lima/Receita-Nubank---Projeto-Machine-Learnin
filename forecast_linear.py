
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings

warnings.filterwarnings("ignore")

# Load the data
try:
    revenue_df = pd.read_csv('nu_revenue.csv', index_col=0, parse_dates=True)
except FileNotFoundError:
    print("Error: nu_revenue.csv not found. Please run the get_data.py script first.")
    exit()

# Clean data
revenue_df.dropna(inplace=True)

# --- Feature Engineering ---
# Create a numeric time index
revenue_df['time'] = np.arange(len(revenue_df.index))

# --- Train/Test Split ---
X = revenue_df[['time']]
y = revenue_df['Revenue']

# --- Linear Regression Model ---
model = LinearRegression()
model.fit(X, y)

# --- Forecasting ---
# Create future time steps
future_steps = 4
last_time_step = X['time'].iloc[-1]
future_time_steps = np.arange(last_time_step + 1, last_time_step + 1 + future_steps).reshape(-1, 1)

# Make predictions
future_forecast = model.predict(future_time_steps)

# Create future dates for plotting
last_date = revenue_df.index[-1]
future_dates = pd.date_range(start=last_date, periods=future_steps + 1, freq='QS-DEC')[1:]

# Create a pandas series with the forecast
forecast_series = pd.Series(future_forecast, index=future_dates)

# --- Visualization ---
plt.figure(figsize=(14, 7))
plt.plot(revenue_df.index, y, label='Historical Revenue', marker='o')
plt.plot(forecast_series.index, forecast_series, label='Forecasted Revenue (Linear Regression)', marker='x', linestyle='--', color='green')

plt.title('Nubank Quarterly Revenue Forecast (Linear Regression)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue (in billions USD)', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig('nu_revenue_forecast_linear.png')

print("Forecast plot saved as nu_revenue_forecast_linear.png")
print("\nForecasted Revenue for the next 4 quarters:")
# Display forecast in billions
print(forecast_series / 1e9)
