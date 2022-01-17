import requests
from rrg_db import DatabaseManager

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo")
tsda = response.json()["Time Series (Daily)"]
ack = "5. adjusted close" # 5 Adjusted Close key
dbM = DatabaseManager()

for key, value in tsda.items():
    print(key, value[ack])

