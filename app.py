import re
import webapp2

from homepage import HomePageHandler
from NewPost import NewpostHandler
from Post import PostHandler
from signup import SignupHandler
from login import LoginHandler
from welcome import WelcomeHandler

routes = [
    ('/(.json){0,1}', HomePageHandler),
    ('/([0-9]+)(.json){0,1}', PostHandler),
    ('/signup', SignupHandler),
    ('/login', LoginHandler),
    ('/welcome', WelcomeHandler),
    ('/newpost', NewpostHandler)
]

app = webapp2.WSGIApplication(routes=routes, debug=True)
