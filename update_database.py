from rrg_db import DatabaseManager
import requests
import time

dbM = DatabaseManager()
dbM.drop_table()
dbM.create_table()

apikey = open("apikey.txt", "r").read()
ack = "5. adjusted close" # 5 Adjusted Close key"

def buildUrl(symbol, apikey):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + symbol + "&apikey=" + apikey
    # url += "&outputsize=full"
    return url

for symbol in dbM.config["symbols"]:
    print("Inserting %s data from AlphaVantage into Database..." % symbol)

    response = requests.get(buildUrl(symbol, apikey))

    if "Time Series (Daily)" not in response.json():
        # Error handling
        # "Note" => too many requests per minute
        # "Error Message" => invalid symbol

        if "Note" in response.json():
            print("Too many requests, waiting ", end ="")

            while "Note" in response.json():
                time.sleep(10)
                print(".", end ="")
                response = requests.get(buildUrl(symbol, apikey))

            print()


        if "Error Message" in response.json():
            print("Invalid symbol, next symbol...\n")
            continue

    tsda = response.json()["Time Series (Daily)"] # Time Series (Daily) Adjusted
    dbM = DatabaseManager()

    for key, value in tsda.items():
        dbM.insert_data(key, value[ack], symbol)
        # print(key, value[ack], symbol)
