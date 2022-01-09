from __main__ import db

class Temperatures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.Float)
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))

    def __init__(self,temp,date,time):
        self.temp = temp
        self.date = date
        self.time = time

db.create_all()