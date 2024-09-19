import os
from dotenv import load_dotenv
from google.oauth2 import service_account

load_dotenv()

key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

#credentials = service_account.Credentials.from_service_account_file(key_path)

credentials= service_account.Credentials.from_service_account_file(
    key_path,
    scopes=['https://www.googleapis.com/auth/bigquery']   
)
