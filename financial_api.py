import requests
import csv
import json
import pandas as pd 
import numpy as np 

from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import matplotlib.ticker as mticker
import mplfinance as mplf


import key1

key = key1.key()

company = 'twtr'
outputsize = 'compact'
response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={company}&outputsize={outputsize}&apikey={key}')

res = json.loads(response.text)
df = pd.DataFrame(res)

df.dropna(axis='index', how ='all', subset=['Time Series (Daily)'], inplace=True)

df.index.rename('Date', inplace=True)
df.dropna(axis='columns', how='all', inplace=True)

df['open'] = (df['Time Series (Daily)'].apply(lambda x: x.get('1. open', 0))).astype(float)
df['high'] = (df['Time Series (Daily)'].apply(lambda x: x.get('2. high', 0))).astype(float)
df['low'] = (df['Time Series (Daily)'].apply(lambda x: x.get('3. low', 0))).astype(float)
df['Close'] = (df['Time Series (Daily)'].apply(lambda x: x.get('4. close', 0))).astype(float)
df['adjusted close'] = (df['Time Series (Daily)'].apply(lambda x: x.get('5. adjusted close', 0))).astype(float)
df['Valume'] = (df['Time Series (Daily)'].apply(lambda x: x.get('6. volume', 0))).astype(float)
df['dividend amount'] = (df['Time Series (Daily)'].apply(lambda x: x.get('7. dividend amount', 0))).astype(float)
df['split coefficient'] = (df['Time Series (Daily)'].apply(lambda x: x.get('8. split coefficient', 0))).astype(float)

df.drop(columns=['Time Series (Daily)'], inplace=True)

df.index = pd.to_datetime(df.index)

buying_point = df.loc['2020-07-07']['Close'].min()
buying_date = df.loc['2020-07-07'].index

# ploting
fig = plt.figure()
ax=plt.subplot2grid((1,1), (0,0))
ax.fill_between(df.index, df['Close'], buying_point,
            where=(df['Close'] > buying_point),
            alpha=0.5, facecolor='g',
            interpolate=True,
            label='Profect'
             )

ax.fill_between(df.index, df['Close'], buying_point,
            where=(df['Close'] < buying_point),
            alpha=0.5, facecolor='r',
            interpolate=True,
            label='Loss'
             )


ax.plot_date(df.index, df['Close'], '-', label='Price')
ax.axvline(buying_date , color='#786763')
ax.axhline(buying_point, color ='g')

for label in ax.xaxis.get_ticklabels():
    label.set_rotation(30)

ax.spines['left'].set_color('c')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.tick_params(axis='x', color='#786763')

date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.gcf().autofmt_xdate()


# ax.grid(True)#, color='g')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title(company)
plt.show()
