from flask import Flask, Blueprint, render_template, current_app, jsonify, make_response,request
from flask.helpers import make_response
import requests
import service.cryptocurrency as crypto
import time
import sqlite3

main = Blueprint('main',__name__,static_folder='static',template_folder='templates')

@main.route('/')
@main.route('/index')
def index():
    res = crypto.getCryptoLimit(5)
    news = crypto.getNews(4)

    return render_template('index.html',response=res['result'],status=res['status'],response_new=news['result'])

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
    return render_template('about.html')


@main.route('/chart/<string:id>')
def chart(id):
    return render_template('chart.html')


@main.route('/news')
def news():
    news = crypto.getNews(20)
    return render_template('news.html',response_new=news['result'])


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