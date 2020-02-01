from flask import Blueprint, jsonify, request, render_template
from app.repository.repository import getWeather


views = Blueprint("views",__name__)

@views.route('/')
def reactPage():
    return 'React Page here'

@views.route('/weather')
def showWeather():
    city = request.args.get("q")
    return getWeather(city)