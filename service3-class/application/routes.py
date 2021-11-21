from application import app
from flask import Flask, request, Response
import random

def class_func():
    class_list = ['Fighter', 'Wizard', 'Rogue']
    class_ = random.choice(class_list)
    return Response(class_, mimetype='text/plain')