
from flask import request

import json
import urllib

import keys

api_keys = keys.read_keys()
currency_key = api_keys['fixer.io']
    # ? access_key = API_KEY

def get_currency(url, base):
    if url == None:
        print('you have not entered a valid url or API key for currency data')
    else:
        url = url + f'?access_key={currency_key}' + f'&base={base}'
        all_currency = urllib.request.urlopen(url).read()
        parsed_currency = json.loads(all_currency)
        print('API call for get_currency(), result: \n',parsed_currency)
    return parsed_currency

    