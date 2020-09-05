import csv
import json
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import requests


url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"market":"CNY","symbol":"BTC","function":"DIGITAL_CURRENCY_DAILY"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "d546c636d9msh6d57bb52757acb4p161de7jsn03d3c950f164"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
res = json.loads(response.text)
date = []
close_USD = []
volume = []
open_USD = []
high_USD = []
low_USD = []
market_USD = []
for key, value in res["Time Series (Digital Currency Daily)"].items():

    date.append(key)
    close_USD.append(float(value["4b. close (USD)"]))
    volume.append(float(value["5. volume"]))
    open_USD.append(float(value["1b. open (USD)"]))
    high_USD.append(float(value["2b. high (USD)"]))
    low_USD.append(float(value["3b. low (USD)"]))
    market_USD.append(float(value["6. market cap (USD)"]))
    

date = pd.to_datetime(date)
date.sort_values()

# date format
# %Y = full year 2020
# %y = partial year 20
# %m = month
# %d = day
# %H = hour
# %M = minute
# %S = second

for i in range(len(date)):
    print(f'{date[i]}, {close_USD[i]}, {volume[i]}, {open_USD[i]}, {high_USD[i]}, {low_USD[i]}, {market_USD[i]}')






# with open('finance_data.csv', 'w', ) as datafile:
#     csv_writer = csv.writer(datafile)
#     csv_writer.writerow(response)