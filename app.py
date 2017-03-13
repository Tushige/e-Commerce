import os
import webapp2

from welcome import WelcomeHandler
from homepage import HomepageHandler
from login import LoginHandler
from signup import SignupHandler

# maps all routes to their corresponding handler classes
routes = [
    ('/', HomepageHandler),
    ('/login', LoginHandler),
    ('/signup', SignupHandler),
    ('/welcome', WelcomeHandler)
]
app = webapp2.WSGIApplication(routes=routes, debug=True)
