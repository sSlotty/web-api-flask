from flask import request
import requests
import config
import json
from datetime import date

def getCrpytoAll():
    url = '{}/ticker?key={}&=interval=1d,30d&convert=THB'.format(config.API['API_STOCK'],config.API['API_STOCK_KEY'])
    
    req = requests.get(url, stream=True,headers={'User-Agent':'X-Pagination-Total-Items'})
    
    if req.status_code == 200:
        return {"result":req.json(),"status":True}
    else:
        print("String could not be converted to JSON")
        return {"result":"Please try agin","status":False}

def getCryptoLimit(perPage):
    url = '{}/ticker?key={}&interval=1d,30d&convert=THB&per-page={}&page=1'.format(config.API['API_STOCK'],config.API['API_STOCK_KEY'],perPage)
    response = requests.get(url,headers={'User-Agent':'X-Pagination-Total-Items'})
    print(url)
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


def getNews(count=5):
    today = date.today()
    # c = toInteger(count)
    date_now = today.strftime("%Y/%m/%d")
    news = list()
    url = '{}/everything?q=cryptocurrency&form={}&sortBy=popularity&apiKey={}'.format(config.API['API_NEWS_URL'],date_now,config.API['API_NEWS_KEY'])
    req = requests.get(url)
    req_json = req.json()

    for i in range(count):
        news.append(req_json['articles'][i])

    if req.status_code == 200:
        return {"result":news,"status":True}
    else:
        return {"result":"Please try again","status":False}


def getChart(id):
    print(id)
    url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym=THB&limit=1000&api_key=68019fce8e3a5632bfebe1aa321b907acf74c6750d6cbaeed43091aaea17d55e'.format(id)
    req= requests.get(url)
    data = req.json()
    chart = list()
    num = (len(data['Data']['Data']))
    for i in range(num):
        chart.append(data['Data']['Data'][i])
        
    if req.status_code == 200:
        return {"result":chart,"status":True}
    else:
        return {"result":"Please try again","status":False}
    
    


