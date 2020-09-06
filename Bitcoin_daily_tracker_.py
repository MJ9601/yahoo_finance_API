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
# data=pd.read_json(orient='index')
# print(data)

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


# date.append(key)
# close_USD.append(float(value["4b. close (USD)"]))
# volume.append(float(value["5. volume"]))
# open_USD.append(float(value["1b. open (USD)"]))
# high_USD.append(float(value["2b. high (USD)"]))
# low_USD.append(float(value["3b. low (USD)"]))
# market_USD.append(float(value["6. market cap (USD)"]))
    

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

# for i in range(len(date)):
#     print(f'{date[i]}, {close_USD[i]}, {volume[i]}, {open_USD[i]}, {high_USD[i]}, {low_USD[i]}, {market_USD[i]}')

fig = plt.figure()
ax=plt.subplot2grid((1,1), (0,0))
ax.fill_between(date, close_USD, close_USD[0],
            
            alpha=0.5, facecolor='g',
            interpolate=True,
            label='Profect'
             )

ax.fill_between(date, close_USD, close_USD[0],
            
            alpha=0.5, facecolor='r',
            interpolate=True,
            label='Loss'
             )


ax.plot_date(date, close_USD, '-', label='Price')

for label in ax.xaxis.get_ticklabels():
    label.set_rotation(30)
date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)
# plt.gcf().autofmt_xdate()


plt.legend()
plt.xlabel('Date')
plt.ylabel('Price (USD)')
ax.grid(True, color='g', linestyle=':', linewidth=.5)
# solid line '-' or 'solid'
# dashed line '--' or 'dashed'
# dashed-dotted line '-.' or 'dashedot'
# dotted line ':' or 'dotted'


ax.xaxis.label.set_color('c')
ax.yaxis.label.set_color('r')
ax.set_yticks([0, 5000, 10000, 15000, 20000]) # set value for the y axis



# plt.tight_layout()
plt.subplots_adjust(bottom=0.20, left=0.121, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()





# with open('finance_data.csv', 'w', ) as datafile:
#     csv_writer = csv.writer(datafile)
#     csv_writer.writerow(response)