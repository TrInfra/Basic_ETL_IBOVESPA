import os
import pandas as pd
from auth import credentials
from pandas_gbq import to_gbq
from dotenv import load_dotenv


load_dotenv()

path= os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, '..', '..', 'Data')

df= pd.read_parquet(f'{file_path}/Trusted/ibovespa_history.parquet', engine='pyarrow')

project_info = os.getenv("PROJECT_ID")


to_gbq(
    df,
    credentials=credentials,
    destination_table='IBOVESPA_History.history',
    project_id=project_info,
    if_exists='replace'
)