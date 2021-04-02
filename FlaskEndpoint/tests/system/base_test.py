#inny wzór - nie test_

from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def setUp(self): # startuje przed każdym testem
        app.testing = True # na całe życie tej apki mówi Flask'owi, że jesteśmy w trybie testowym
        self.app = app.test_client