from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        #return app
        pass

class TestClass(TestBase):
    def test_Class(self):
        pass