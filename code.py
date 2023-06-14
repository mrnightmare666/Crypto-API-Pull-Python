from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

#provides functions for working with JSON data in Python
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f5f31361-b943-4caf-b7f9-f4d767f04f10',
}

session = Session()
session.headers.update(headers)

try:
  #sends an HTTP GET request to the specified url with the given parameters
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #Making the data more presentable
  prettified_response = json.dumps(data, indent=4)
  print(prettified_response)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
  import pandas as pd
  
#This allows you to see all the columns, not just like 15
pd.set_option('display.max_columns', None)

#Presents the data in a table format
pd.json_normalize(data['data'])
