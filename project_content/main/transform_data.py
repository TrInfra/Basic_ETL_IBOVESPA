import pandas as pd
import os 

path= os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(path, '..', 'Data')

df = pd.read_csv(f'{csv_path}/Raw/ibovespa_history.csv',date_format='Y-%m-%d')
df = df.drop(['Dividends', 'Stock Splits'],axis='columns')

df['Date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce').dt.date

removeVolumeIf = 0 

df.drop(df[df['Volume'] == removeVolumeIf].index, inplace=True) 

df_parquet = df.to_parquet(f'{csv_path}/Trusted/ibovespa_history.parquet',engine='pyarrow',index=False)
