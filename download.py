import datetime
import wget
import pandas as pd
from parser import parser
import os
date = datetime.datetime(2020,4,3)
while date < datetime.datetime.today():
    
    filename =date.strftime("%Y%m%d")
    print(filename)
    url="https://s3-eu-west-1.amazonaws.com/public.bitmex.com/data/trade/"+filename+".csv.gz"

    wget.download(url, filename+'.csv.gz')
    df = pd.read_csv(filename+'.csv.gz', compression='gzip',
                    error_bad_lines=False)
    df.drop(columns=['foreignNotional','grossValue','side','tickDirection',
        'trdMatchID', 'homeNotional'], inplace=True)
    df['timestamp'] = df['timestamp'].str.replace('D',' ')
    df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True, unit='ns')
    btc_df=df[df['symbol']=='XBTUSD']

    btc_parser = parser('XBTUSD')
    btc_candles = btc_parser.calculate_bars(btc_df)
    btc_candles.set_index('Timestamp',inplace=True)
    btc_candles.to_csv('./btc/'+filename+'_btc.csv')

    os.remove(filename+'.csv.gz')
    date =date+ datetime.timedelta(days=1)
    