from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime
import yaml


with open("./src/config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)


app = Flask(__name__, template_folder='templates', static_folder = "static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+cfg["app"]["database"]["user"]+':'+cfg["app"]["database"]["password"]+'@'+cfg["app"]["database"]["host"]+'/'+cfg["app"]["database"]["name"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TURN_ON_TIME'] = datetime.datetime.utcnow()


db = SQLAlchemy(app)
ma = Marshmallow(app)

from db import *
from schemas import *

user_schema = TemperaturesSchema()

from routes import *
#from serialport import *


if __name__ == "__main__":
    #start_serial_loop()
    app.run(debug=True)