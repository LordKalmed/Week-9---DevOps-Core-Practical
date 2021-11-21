from application import app
from flask import Flask, request, Response
import random
import requests

@app.route('/name_gen', methods=['POST'])
def name_gen():
    race_name  = requests.get('http://name_generator_service2-race:5001/race')
    human_list = ['Om', 'Vardam', 'Sondisk']
    elf_list = ['Beiran', 'Pakian', 'Zinyarus']
    dragonborn_list = ['Paravax', 'Faccethir', 'Krochuas']
    if race_name=='Human':
        name = random.choice(human_list)
        return Response(name, mimetype='text/plain')
    elif race_name=='Elf':
        name = random.choice(elf_list)
        return Response(name, mimetype='text/plain')
    elif race_name=='Dragonborn':
        name = random.choice(dragonborn_list)
        return Response(name, mimetype='text/plain')

def title_gen():
    class_name  = requests.get('http://name_generator_service3-class:5002/class')
    fighter_list =['Brave', 'Strong', 'Tactical']
    wizard_list = ['Wise', 'Powerful', 'Devious']
    rogue_list = ['Cunning', 'Cutthroat', 'Silent']
    if class_name=="Fighter":
        title = random.choice(fighter_list)
        return Response(title, mimetype='text/plain')
    elif class_name=="Wizard":
        title = random.choice(wizard_list)
        return Response(title, mimetype='text/plain')
    elif class_name=="Rogue":
        title = random.choice(rogue_list)
        return Response(title, mimetype='text/plain')