from flask import url_for
from flask_testing import TestCase
from application import app

class TestGen(TestCase):
    def create_app(self):
        #return app
        pass

class TestingResponse(TestGen):
    def test_home(self):
        pass

    def test_generator(self):
        pass