import yfinance as yf
import pandas as pd

# Define the ticker symbol for Nubank
ticker = "NU"

# Download historical data
nu_data = yf.download(ticker, period="max", interval="1d")

# Save the data to a CSV file
nu_data.to_csv("nubank_data.csv")

print("Dados do Nubank baixados e salvos em nubank_data.csv")
