
import yfinance as yf
import pandas as pd

# Define the ticker symbol for Nubank
ticker_symbol = "NU"

# Create a Ticker object
nu_ticker = yf.Ticker(ticker_symbol)

# Get quarterly financial data
quarterly_financials = nu_ticker.quarterly_financials

# Check if the financials data is available
if quarterly_financials.empty:
    print(f"Could not retrieve financial data for {ticker_symbol}. Please check the ticker symbol.")
else:
    # Transpose the data to have dates as rows
    quarterly_financials = quarterly_financials.T

    # Select the 'Total Revenue' column
    if 'Total Revenue' in quarterly_financials.columns:
        revenue = quarterly_financials[['Total Revenue']].copy()

        # Convert index to datetime objects
        revenue.index = pd.to_datetime(revenue.index)

        # Sort the data by date
        revenue = revenue.sort_index()
        
        # Rename the column to 'Revenue'
        revenue.rename(columns={'Total Revenue': 'Revenue'}, inplace=True)
        
        # Save the data to a CSV file
        revenue.to_csv('nu_revenue.csv')

        print("Quarterly revenue data for Nubank saved to nu_revenue.csv")
        print(revenue.head())
    else:
        print("Total Revenue data not found in the financial statements.")
        print("Available columns:", quarterly_financials.columns)

