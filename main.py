import yfinance as yf
import pandas as pd

# fetch data for ticker / symbol
ticker = 'AAPL'
data = yf.download(ticker, start = '2020-01-01', end = '2023-10-17')

# save a csv file
data.to_csv(f'{ticker}_data.csv')