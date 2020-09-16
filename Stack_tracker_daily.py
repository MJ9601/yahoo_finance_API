import requests
import key1

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"outputsize":"compact","datatype":"json","function":"TIME_SERIES_DAILY","symbol":"MSFT"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': key1.key2()
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)