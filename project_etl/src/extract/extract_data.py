import yfinance as yf
from datetime import datetime
import pandas as pd
from IPython.display import display
import os 

path = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(path, '..','..', 'Data') 

ibovespa = yf.Ticker('^BVSP')

currentdate = datetime.now().strftime('%Y-%m-%d')
hist_bvsp= ibovespa.history(start='2007-01-01', end=currentdate)

df= hist_bvsp
df= df.sort_values('Date', ascending=False)
df= df.to_csv(f'{data_dir}/Raw/ibovespa_history.csv', sep=',', index=True)