'''
This file contains the class that handles homepage logic
'''
from base import BaseHandler

# handler class for route '/'
class HomepageHandler(BaseHandler):
    def get(self):
        self.redirect('/signup')
