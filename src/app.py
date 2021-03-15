from sqlite3.dbapi2 import connect
from flask import Flask
from blueprints.main import main
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)
app.register_blueprint(main,url_prefix='')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_table():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
