from flask import Blueprint, jsonify, request, render_template


views = Blueprint("views",__name__)

@views.route('/')
def reactPage():
    return 'React Page here'

@views.route('/weather')
def showWeather():
    return 'get weather'