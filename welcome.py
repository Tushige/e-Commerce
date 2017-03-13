'''
This file contains the class that handles logged in user welcome page logic
'''
from base import BaseHandler
from entity import User

# handler class for route '/welcome'
class WelcomeHandler(BaseHandler):
    def get(self):
        # if user found, welcome user
        if self.user:
            self.render('welcome.html', username=self.user.username)
        # if user not found, go to homepage
        else:
            self.redirect('/')
