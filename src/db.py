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
        self.date = str(date_now.year) + self.parse(date_now.month) + self.parse(date_now.day)
        self.time = self.parse(date_now.hour) + ":" + self.parse(date_now.minute)

    def parse(self, num):
        if num > 9:
            return str(num)
        else:
            return "0" + str(num)

db.create_all()