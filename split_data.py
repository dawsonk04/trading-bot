import pandas as pd
from sklearn.model_selection import train_test_split

# load data with features
data = pd.read_csv('AAPL_data_features.csv', index_col='Date', parse_dates=True)

# defining feature and target var
features = data[['MA10', 'MA50', 'Volume_Change']]
target = data['Future_Price']

# splitting the data
x_train, x_test, y_Train, y_test = train_test_split(features, target, test_size=0.2, shuffle=False)