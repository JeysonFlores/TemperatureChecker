from __main__ import db
from datetime import datetime

class Temperatures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.Float)
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))

    def __init__(self,temp):
        self.temp = temp
        date_now = datetime.now()
        self.date = str(date_now.year) + str(date_now.month) + str(date_now.day)
        self.time = str(date_now.hour) + ":" + str(date_now.minute)

db.create_all()