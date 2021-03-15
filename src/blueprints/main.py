from flask import Flask, Blueprint, render_template, current_app, jsonify, make_response,request
from flask.helpers import make_response
import requests
import service.cryptocurrency as crypto
import time
from models import db,Member
import locale

locale.setlocale( locale.LC_ALL, '' )

main = Blueprint('main',__name__,static_folder='static',template_folder='templates')

@main.route('/')
@main.route('/index')
def index():
    res = crypto.getCryptoLimit(5)
    news = crypto.getNews(4)
    newResults = [];
    for i in range(len(res['result'])):
        # print(res['result'][i]['1d']['volume_change'].format())

        price = "฿ {:,.2f}".format(float(res['result'][i]['price']))
        d_volume = "{:,.2f}".format(float(res['result'][i]['1d']['volume']))
        d_volume_change = "{:,.2f}".format(float(res['result'][i]['1d']['volume_change']))
        high = "฿ {:,.2f}".format(float(res['result'][i]['high']))

        result = {
            'id':res['result'][i]['id'],
            'currency':res['result'][i]['currency'],
            'symbol':res['result'][i]['symbol'],
            'name':res['result'][i]['name'],
            'logo_url':res['result'][i]['logo_url'],
            'rank':res['result'][i]['rank'],
            'high':high,
            'price':price,
            '1d_volume':d_volume,
            '1d_volume_change':d_volume_change,
        }
        newResults.append(result)
    
    print(newResults)
        

    return render_template('index.html',response=newResults,status=res['status'],response_new=news['result'])

@main.route('/more-market')
def viewAll():
    return render_template('more_market.html')
    


@main.route('/about-market/<string:id>')
def about_market(id):
    req = crypto.getAboutCrypto(id)
    pass
    return render_template('about-market.html')

@main.route('/about')
def about():
    member = []
    records = Member.query.all()
    for data in records:
        recordsObj = {
            'std_id': data.std_id,
            'name': data.name,
            'role':data.role,
            'img': data.imagelink,
            'facebook': data.facelink,
            'git':data.gitlink,
            'mail': data.maillink
        }
        member.append(recordsObj)

    return render_template('about.html',response=member)

@main.route('/chart', methods=['GET','post'])
def chart():
    return render_template('chart.html')


@main.route('/news')
def news():
    news = crypto.getNews(20)
    return render_template('news.html',response_new=news['result'])

@main.route('/loadChart')
def loadChart():
    id = request.args.get('id')
    req = crypto.getChart(id)
    return req


@main.route('/load')
def load():

    posts = list()

    get = crypto.getCrpytoAll()
    for data in get["result"]:
        posts.append(data)

    count_post = len(posts)
    quantity = 20
    print(count_post)
    print(quantity)

    time.sleep(0.02)
    if request.args:

        counter = int(request.args.get("c"))

        if counter == 0:
            print(f"Returning posts 0 to {quantity}")
            res = make_response(jsonify(posts[0:quantity]),200)

        elif counter == posts:
            print("No more posts to load")
            res = make_response(jsonify({}), 200)

        else:
            print(f"Returning posts {counter} to {counter + quantity}")
            res = make_response(jsonify(posts[counter: counter + quantity]),200)

    return res