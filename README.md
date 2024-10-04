## About project
The goal of this project is to illustrate the daily work of a data engineer, with a focus on the ETL process (Extract, Transform, and Load), which forms the foundation of their work. For this, I used the yfinance API to extract data from the Ibovespa index.

Ibovespa is the main performance indicator of the Brazilian stock market, reflecting the behavior of the shares of companies with the highest trading volume on B3, Brazil's official stock exchange. It acts as a barometer of the performance of the leading listed companies and is widely used by investors and analysts to track the market.
### Project
- [project](project_etl/)  


## Environments Configuration
First of all, let's download the necessary libraries to run the project:

```shell
pip install yfinance==0.2.44
pip install google-auth==2.35.0
pip install pandas==2.2.2
pip install pandas-gbq==0.23.1
```
Now let's create a .env file to hide your project information in Google BigQuery.

Google BigQuery is a fully-managed data warehouse that allows for super-fast SQL queries using the processing power of Google's infrastructure. In this project, it's used to store and analyze the financial data extracted from the Ibovespa index.

Before running the project, make sure to create a project in Google Cloud, enable the BigQuery API, and generate the credentials file (Credentials.json) from the IAM & Admin section.

.env
```python
GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/Credentials.json"
PROJECT_ID="your_project_id"
```
To get your credentials, read the BigQuery documentation or watch the video.
[Click here to watch](https://www.youtube.com/watch?v=rWcLDax-VmM&ab_channel=Codingthecosmos)


## Project Structure
```python
project_etl
    ├───Data
       ├───Raw 
       ├───Trusted
    ├───src
        ├───extract
              └─── extract_data.py
        ├───load
              └───__pycache__
              └───auth.py
              └───load_data.py
        ├───transform
              └───transform_data.py
```
