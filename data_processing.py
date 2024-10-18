# may not need this file - store this data in feature_engineering?

import pandas as pd

# read / load csv
data = pd.read_csv('AAPL_data.csv', index_col='Date', parse_dates=True)

# checking for any missing values
print(data.isnull().sum())

# fill / drop missing values

data = data.dropna()