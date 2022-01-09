from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime
import yaml


with open("./src/config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+cfg["app"]["database"]["user"]+':'+cfg["app"]["database"]["password"]+'@'+cfg["app"]["database"]["host"]+'/'+cfg["app"]["database"]["name"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TURN_ON_TIME'] = datetime.datetime.utcnow()


db = SQLAlchemy(app)
ma = Marshmallow(app)

from db import *
from schemas import *

user_schema = TemperaturesSchema()

from routes import *


if __name__ == "__main__":
    app.run(debug=True)