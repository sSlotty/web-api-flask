from sqlite3.dbapi2 import connect
from flask import Flask
from blueprints.main import main
import sqlite3
from flask_sqlalchemy import SQLAlchemy

from models import db, Member

app = Flask(__name__)


app.config['SECRET_KEY'] = 'app-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///member.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(main,url_prefix='')


@app.before_first_request
def create_table():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
