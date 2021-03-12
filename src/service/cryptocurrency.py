import requests
import config

def getCrpytoAll():
    url = '{}/ticker?key={}&=interval=1d,30d&convert=THB&page=1'.format(config.API['API_STOCK'],config.API['API_STOCK_KEY'])
    # print(url)
    response = requests.get(url)
    
    if response.status == requests.codes.OK:
        return response.json(),True
    else:
        return response.json(),False

def getCryptoLimit(perPage):
    url = '{}ticker?key={}&interval=1d,30d&convert=THB&page=1&per-page={}'.format(config.API['API_STOCK'],config.API['API_STOCK_KEY'],perPage)
    print(url)
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json(), True
    else: 
        return response.json(), False