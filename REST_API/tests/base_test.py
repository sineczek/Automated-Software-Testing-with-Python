"""

BaseTest

This should be a parent class to each non-unit tests.
It allows for installation of the database dynamically
and makes sure that it is a new, blank database each time.

"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):  # befor'ek
        # make sure db exist
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():  # wgrywa wszystko z app, "udaje" że appka pracuje
            db.init_app(app)
            db.create_all()
        # gest a test client
        self.app = app.test_client()
        self.app_context = app.app_context


    def tearDown(self):  # after'ek
        # db is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
