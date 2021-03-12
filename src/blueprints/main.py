from flask import Flask,Blueprint,render_template,current_app
import requests
import service.cryptocurrency as crypto
main = Blueprint('main',__name__,static_folder='static',template_folder='templates')

@main.route('/')
@main.route('/index')
def index():
    res,status = crypto.getCryptoLimit(5)
    print(status)
    return render_template('index.html',response=res,status = status)

@main.route('/more-market')
def viewAll():
    res,status = crypto.getCrpytoAll()
    return render_template('more_market.html',response = res,status = status)

@main.route('/about-market/<string:id>')
def about_market(id):
    return render_template('about-market.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/chart/<string:id>')
def chart(id):
    return render_template('chart.html')


@main.route('/news')
def news():
    return render_template('news.html')