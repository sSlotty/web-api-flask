from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Member(db.Model):

    std_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    facelink = db.Column(db.Text)
    gitlink = db.Column(db.Text)
    imagelink = db.Column(db.Text)
    maillink = db.Column(db.Text)
    role = db.Column(db.Text)

    def __repr__(self):
        return "<Member %r>" % self.std_id

