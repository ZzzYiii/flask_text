import datetime

from app.ext import db


class Shop(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    price = db.Column(db.Numeric(10, 2))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    expiration_date = db.Column(db.String(64))
    status = db.Column(db.Integer)



