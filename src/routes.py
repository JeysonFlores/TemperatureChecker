from __main__ import app
from flask_restful import abort
from flask import jsonify, render_template
from sqlalchemy import func
from functools import wraps
import datetime
import secrets
from __main__ import Temperatures


app.config['SECRET_KEY'] = secrets.token_urlsafe(16)


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"message": "Invalid request"})

@app.errorhandler(403)
def unauthorized_request(e):
    return jsonify({"message": "Unauthorized request"})

@app.errorhandler(404)
def unknown_route(e):
    return jsonify({"message": "Invalid route"})

@app.errorhandler(405)
def invalid_method(e):
    return jsonify({"message": "Invalid method"})

@app.route('/stats')
def stats():
    return jsonify({"active-date": str(app.config['TURN_ON_TIME']), "active-time": str(datetime.datetime.utcnow() - app.config['TURN_ON_TIME'])})

@app.route('/')
def root():
    return render_template('main.html')

@app.route('/date/<date>')
def date(date):
    temps = Temperatures.query.filter_by(date = date).all()
    max_temp = max(temps, key=lambda x:x.temp)
    min_temp = min(temps, key=lambda x:x.temp)
    avg_temp = 0
    for temp in temps:
        avg_temp += temp.temp
    avg_temp /= len(temps)

    year = str(date)[0:4]
    month = str(date)[4:6]
    day = str(date)[6:8]
    print(max_temp.temp)
    print(min_temp.temp)
    print(avg_temp)
    print(year)
    print(month)
    print(day)

    return render_template('date.html', temperatures = temps, year = year, month = month, day = day, min=min_temp.temp, max=max_temp.temp, avg=avg_temp)
