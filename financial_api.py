import requests
import csv
import json
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import matplot.yahoo_APIs.key1

key = matplot.yahoo_APIs.key1.key()
print(key)
# company = 'IBM'
# outputsize = 'compact'
# response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={company}&outputsize={outputsize}&apikey={key}')

# res = json.loads(response.text)
# df = pd.DataFrame(res)
