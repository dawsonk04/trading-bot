import backtrader as bt
import pandas as pd
import joblib

class PandasDataExtended(bt.feeds.PandasData):
    lines = ('MA10', 'MA50', 'Volume_Change')
    params = (
        ('MA10', -1),
        ('MA50', -1),
        ('Volume_Change', -1)
    )

class MLStrat(bt.Strategy):
    params = dict(model = None)

    def __init__(self):
        self.ma10 = self.data[0].MA10
        self.ma50 = self.data[0].MA50
        self.volume_change = self.data[0].Volume_Change
        self.model = self.params.model
        self.order = None

    def next(self):
        # prep features
        features = [
            self.ma10[0],
            self.ma50[0],
            self.volume_change[0]
        ]

        if any(pd.isnull(features)):
            return
        
        prediction = self.model.predict([features])[0]

        if not self.position:
            if prediction > self.data[0].close[0]:
                self.buy()
            else:
                if prediction <= self.data[0].close[0]:
                    self.sell()
    
    data = pd.read_csv('AAPL_data_features.csv', index_col='Date', parse_dates=True)

    data.rename(columns= {
        'Open' : 'open',
        'High' : 'high',
        'Low' : 'low',
        'Close' : 'close',
        'Volume' : 'volume'
    }, inplace= True)

    # prep data feeding

    data_feed = PandasDataExtended(
        dataname = data,
        datetime = None,
        open = 'open',
        high = 'high',
        low = 'low',
        close = 'close',
        volume = 'volume',
        MA10 = 'MA10',
        MA50 = 'MA50',
        Volume_Change = 'Volume_Change',
        openinterest = -1
    )

    # init cerbro
    cerebro = bt.Cerebro()

    # add data
    cerebro.adddata(data_feed)

    # load model
    model = joblib.load('random_forest_model.pkl')

    # add start
    cerebro.addstrategy(MLStrat, model = model)

    # set cash
    cerebro.broker.setcash(1000.00)

    # backtest
    cerebro.run()

    print(f'Portfolio Value: {cerebro.broker.getvalue()}')
    cerebro.plot()