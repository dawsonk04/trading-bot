import pandas as pd

# load the pre-processed data
data = pd.read_csv('AAPL_data_preprocessed.csv', index_col='Date', parse_dates=True)

# assuming data in is dataframe  
data['MA10'] = data['Close'].rolling(window=10).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()
data['Volume_Change'] = data['Volume'].pct_change()

data['Future_Price'] = data['Close'].shift(-1)

# again drop rows with NaN values from rolling calcs
data = data.dropna()