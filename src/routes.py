from __main__ import app
from flask_restful import abort
from flask import jsonify, render_template
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