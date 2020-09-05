import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"outputsize":"compact","datatype":"json","function":"TIME_SERIES_DAILY","symbol":"MSFT"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "d546c636d9msh6d57bb52757acb4p161de7jsn03d3c950f164"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)