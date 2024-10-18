import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

data = pd.read_csv('AAPL_data_features.csv', index_col='Date', parse_dates=True)

# defining feature and target var
features = data[['MA10', 'MA50', 'Volume_Change']]
target = data['Future_Price']

# splitting the data
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, shuffle=False)

# initalize the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# train with previous data
model.fit(x_train, y_train)

# make predictions
predictions = model.predict(x_test)
mse = root_mean_squared_error(y_test, predictions)

print(f'Root MS Error: {mse}')