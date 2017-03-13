'''
This file contains the class that handles user login logic
'''
from base import BaseHandler
from entity import User
from credential import Credential

class LogOut(BaseHandler):
    def get():
        self.logout()
        self.redirect('/')
