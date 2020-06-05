import pandas as pd 
import datetime

date = datetime.datetime(2019,1,1)
df = pd.DataFrame(columns=['Timestamp','Ticks','Open','High','Low','Close','Volume'])
while date < datetime.datetime.today()-datetime.timedelta(days=1):
    
    filename =date.strftime("%Y%m%d")+"_btc.csv"
    print(filename)
    date =date+ datetime.timedelta(days=1)
    temp_df = pd.read_csv('./btc/'+filename)
    df=df.append(temp_df,ignore_index=True)
print(df.head(20))
print(df.tail(20))
print(df.shape)

df.to_csv('XBTUSD_vbar.csv')