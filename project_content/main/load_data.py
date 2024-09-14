import pandas as pd
import os 

path = os.path.dirname(os.path.abspath(__file__))
data_dir =os.path.join(path, '..', 'Data')

df = pd.read_parquet(f'{data_dir}/Trusted/ibovespa_history.parquet')

# refining
df['AveragePrice']= (df['High'] + df['Low']) / 2
df['Range'] = df['High'] - df['Low']

df = df.to_parquet(f'{data_dir}/Refined/ibovespa_history_refined.parquet')
