import pandas as pd
class parser:
    def __init__(self, pair):
        self.volume = 0.0
        self.open = 0
        self.high = float('-inf')
        self.low = float('inf')
        self.close = 0
        self.ticks = 0
        self.pair = pair
        self.bbar=[]
        self.threshold = 100000000 if pair == 'XBTUSD' else 10000000

    def calculate_bars(self, df):
        for index, row in df.iterrows():

            self.volume = self.volume+row['size']
            if self.ticks == 0:
                self.open = row['price']
            if row['price'] > self.high:
                self.high = row['price']
            if row['price'] < self.low:
                self.low = row['price']
            self.ticks = self.ticks+1
            if(self.volume >= self.threshold):

                self.close = row['price']
                self.bbar.append([row['timestamp'], self.ticks, self.open, self.high, self.low, self.close, self.volume])
                self.volume = 0.0
                self.open = 0
                self.high = float('-inf')
                self.low = float('inf')
                self.close = 0
                self.ticks = 0


        return pd.DataFrame(data=self.bbar, columns=['Timestamp', 'Ticks', 'Open', 'High', 'Low', 'Close', 'Volume'])
