import csv
import json
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
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
data = pd.DataFrame(res)

last_refreshed = data.loc['6. Last Refreshed']['Meta Data']
Time_zone = data.loc['7. Time Zone']['Meta Data']

data.dropna(axis='index', how='all', subset=['Time Series (Digital Currency Daily)'], inplace=True)

data.dropna(axis='columns', how='all', inplace=True)
data.columns=['treding stuff']

data.index.rename('Date', inplace=True)


data['openUSD'] = (data['treding stuff'].apply(lambda x: x.get('1b. open (USD)', 0))).astype(float)
data['highUSD'] = (data['treding stuff'].apply(lambda x: x.get('2b. high (USD)', 0))).astype(float)
data['lowUSD'] = (data['treding stuff'].apply(lambda x: x.get('3b. low (USD)', 0))).astype(float)
data['CloseUSD'] = (data['treding stuff'].apply(lambda x: x.get('4b. close (USD)', 0))).astype(float)
data['Valume'] = (data['treding stuff'].apply(lambda x: x.get('5. volume', 0))).astype(float)
data['MarketCapUSD'] = (data['treding stuff'].apply(lambda x: x.get('6. market cap (USD)', 0))).astype(float)


starting_point = data.loc['2020-01-01']['CloseUSD'].min()
data.index = pd.to_datetime(data.index)




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

# ploting
fig = plt.figure()
ax=plt.subplot2grid((1,1), (0,0))
ax.fill_between(data.index, data['CloseUSD'], starting_point,
            where=(data['CloseUSD'] > starting_point),
            alpha=0.5, facecolor='g',
            interpolate=True,
            label='Profect'
             )

ax.fill_between(data.index, data['CloseUSD'], starting_point,
            where=(data['CloseUSD'] < starting_point),
            alpha=0.5, facecolor='r',
            interpolate=True,
            label='Loss'
             )


ax.plot_date(data.index, data['CloseUSD'], '-', label='Price')

<<<<<<< HEAD
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(30)
date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.gcf().autofmt_xdate()
=======
# for label in ax.xaxis.get_ticklabels():
#     label.set_rotation(30)
# date_format = mpl_dates.DateFormatter('%b, %d %Y')
# plt.gca().xaxis.set_major_formatter(date_format)


# years = mdates.YearLocator()   # every year
# months = mdates.MonthLocator()  # every month
# years_fmt = mdates.DateFormatter('%Y')

# # format the ticks
# ax.xaxis.set_major_locator(years)
# ax.xaxis.set_major_formatter(years_fmt)
# # ax.xaxis.set_minor_locator(months)

# # myFmt = mdates.DateFormatter('%d')
# # ax.xaxis.set_major_formatter(myFmt)

fig.autofmt_xdate()
# locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
# formatter = mdates.ConciseDateFormatter(locator)


# ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
# ax.format_ydata = lambda x: '$%1.2f' % x  # format the price.
# ax.grid(True)
>>>>>>> 0c9117a0f750e2c234becc7d830c1a5d67600c3c


plt.legend()
# plt.xlabel('Date')
plt.ylabel('Price (USD)')

# ax.grid(True, color='g', linestyle=':', linewidth=.5)
# solid line '-' or 'solid'
# dashed line '--' or 'dashed'
# dashed-dotted line '-.' or 'dashedot'
# dotted line ':' or 'dotted'


ax.xaxis.label.set_color('c')
ax.yaxis.label.set_color('r')
# ax.set_yticks([0, 5000, 10000, 15000, 20000]) # set value for the y axis



plt.tight_layout()
plt.subplots_adjust(bottom=0.20, left=0.121, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()

# with open('finance_data.csv', 'w', ) as datafile:
#     csv_writer = csv.writer(datafile)
#     csv_writer.writerow(response)


