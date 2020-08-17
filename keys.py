import os
import json
from pathlib import Path



def read_keys():
    home = str(Path.home())
    path = home + '/api.json'
    with open(path, 'r') as keys:
        api_keys = keys.read()
        dict_keys = ''
        dict_keys = json.loads(api_keys)
    return dict_keys
