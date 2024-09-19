import pandas as pd
import os 

path= os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(path, '..', '..', 'Data')

df = pd.read_csv(f'{data_dir}/Raw/ibovespa_history.csv',date_format='Y-%m-%d')
df = df.drop(['Dividends', 'Stock Splits'],axis='columns')

#df['Date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce').dt.date
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', utc=True)
removeVolumeIf = 0 

df.drop(df[df['Volume'] == removeVolumeIf].index, inplace=True) 

# refining
df['AveragePrice']= (df['High'] + df['Low']) / 2
df['Range'] = df['High'] - df['Low']

df_parquet = df.to_parquet(f'{data_dir}/Trusted/ibovespa_history.parquet',engine='pyarrow',index=False)

