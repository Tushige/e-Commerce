'''
This file contains the class that handles user login logic
'''
from base import BaseHandler
from user_model import User
from credential import Credential

class LogoutHandler(BaseHandler):
    def get(self):
        self.logout()
        self.redirect('/')
