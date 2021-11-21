from application import app
from flask import Flask, request, Response
import random

@app.route('/race', methods=['GET'])
def race_func():
    race_list = ['Human', 'Elf', 'Dragonborn']
    race = random.choice(race_list)
    return Response(race, mimetype='text/plain')