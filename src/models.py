from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

db = SQLAlchemy()

class Member(db.Model):
    __tablename_ = "member"

    std_id = db.Colum(db.Integer,primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    facelink = db.Column(db.Text())
    gitlink = db.Column(db.Text())
    imagelink = db.Column(db.Text())
    maillink = db.Column(db.Text())
    role = db.Column(db.Text())
