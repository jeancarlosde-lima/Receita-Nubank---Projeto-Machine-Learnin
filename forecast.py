
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
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
revenue_df = revenue_df.asfreq('QS-DEC') # Set frequency to quarterly, start of December

# --- Train/Test Split ---
# Let's use all available data for training and forecast the future
train_data = revenue_df['Revenue']

# --- SARIMA Model ---
# The parameters (p,d,q)(P,D,Q,m) are chosen based on typical financial data.
# (p,d,q): Non-seasonal orders
# (P,D,Q,m): Seasonal orders (m=4 for quarterly data)
# This is a starting point; for a real project, we would tune these parameters.
sarima_model = SARIMAX(train_data,
                       order=(1, 1, 1),
                       seasonal_order=(1, 1, 0, 4),
                       enforce_stationarity=False,
                       enforce_invertibility=False)

# Fit the model
sarima_fit = sarima_model.fit(disp=False)

print(sarima_fit.summary())

# --- Forecasting ---
# Forecast the next 4 quarters
forecast_steps = 4
forecast = sarima_fit.get_forecast(steps=forecast_steps)

# Get the confidence intervals
forecast_ci = forecast.conf_int()
forecast_index = pd.date_range(start=train_data.index[-1], periods=forecast_steps + 1, freq='QS-DEC')[1:]

# Create a pandas series with the forecast
forecast_series = pd.Series(forecast.predicted_mean.values, index=forecast_index)

# --- Visualization ---
plt.figure(figsize=(14, 7))
plt.plot(train_data.index, train_data, label='Historical Revenue', marker='o')
plt.plot(forecast_series.index, forecast_series, label='Forecasted Revenue', marker='x', color='red')

# Shade the confidence interval
plt.fill_between(forecast_ci.index,
                 forecast_ci.iloc[:, 0],
                 forecast_ci.iloc[:, 1], color='r', alpha=0.15, label='95% Confidence Interval')

plt.title('Nubank Quarterly Revenue Forecast (SARIMA)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue (in billions USD)', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig('nu_revenue_forecast.png')

print("\nForecast plot saved as nu_revenue_forecast.png")
print("\nForecasted Revenue for the next 4 quarters:")
# Display forecast in billions
print(forecast_series / 1e9)
