from flask import request
import requests
import config
import json


def getCrpytoAll():
    url = '{}/ticker?key={}&=interval=1d,30d&convert=THB&per-page=10'.format(config.API['API_STOCK'],config.API['API_STOCK_KEY'])
    
    req = requests.get(url, stream=True,headers={'User-Agent':'X-Pagination-Total-Items'})
    
    if req.status_code == 200:
        return {"result":req.json(),"status":True}
    else:
        print("String could not be converted to JSON")
        return {"result":"Please try agin","status":False}

def getCryptoLimit(perPage):
    url = '{}/ticker?key={}&interval=1d,30d&convert=THB&per-page={}'.format(config.API['API_STOCK'],config.API['API_STOCK_KEY'],perPage)
    response = requests.get(url,headers={'User-Agent':'X-Pagination-Total-Items'})
    
    if response.status_code == 200:
        return {"result":response.json(),"status":True}
    else: 
        return {"result":"Please try agin","status":False}
    
def getAboutCrypto(id):
    url = '{}?key={}&ids={}'.format(config.API['API_STOCK'],config.API['API_STOCK_KEY'],id)
    req = requests.get(url)
    
    if req.status_code == 200:
        return {"result":req.json(),"status":True}
    else:
        return {"result":"Please try agin","status":False}


