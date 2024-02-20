import yfinance as yf
import pandas as pd

# Define the ticker symbol
tickerSymbol = 'SPY'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', interval="30m", start='2024-1-1', end='2024-2-1')

# Specify the column order
columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']

# Save the data to a CSV file
tickerDf.to_csv(f'csv_dir/{tickerSymbol}.csv')

print(f"Data saved to '{tickerSymbol}.csv'")