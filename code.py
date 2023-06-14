import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

#provides functions for working with JSON data in Python
import json
import pandas as pd

df = pd.DataFrame()

def api_pull():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '25',
        'convert': 'USD'
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

        global df  # Use the global DataFrame variable
        df = pd.concat([df, pd.json_normalize(data['data'])], ignore_index=True)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

# Run the API call and DataFrame update every 10 minutes for 1 hour
for i in range(6):
    api_pull()
    print("API Call completed")
    time.sleep(600)  # Delay for 10 minutes
