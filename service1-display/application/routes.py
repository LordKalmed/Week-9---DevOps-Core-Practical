from application import app
from flask import Flask, request, render_template, url_for
import requests

@app.route('/')
def home():
    return render_template('Homepage.html')

@app.route('/view', methods = ['GET'])
def view():
    race  = requests.get('http://name_generator_service2-race:5001/race')
    class_  = requests.get('http://name_generator_service3-class:5002/class')
    name_gen  = requests.get('http://name_generator_service4-name:5003/name_gen')
    title_gen = requests.get('http://name_generator_service4-name:5003/name_gen')
    return render_template('View.html')