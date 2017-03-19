import re
import webapp2

from homepage import HomePageHandler
from NewPost import NewpostHandler
from Post import PostHandler
from signup import SignupHandler
from signin import SigninHandler
from signout import SignoutHandler
from welcome import WelcomeHandler
from profile import ProfileHandler
from error import Error404Handler
import string
routes = [
    ('/(.json){0,1}', HomePageHandler),
    # /entry/<post_id> -> page of a blog post
    ('/entry/([0-9]{1,100})(.json){0,1}', PostHandler),
    # /signup -> page for registering new user
    ('/signup', SignupHandler),
    # /login -> page for logging in
    ('/signin', SigninHandler),
    # /logout -> logout user
    ('/signout', SignoutHandler),
    # /username -> user front page
    ('/author/([a-zA-Z0-9_-]{3,20})', WelcomeHandler),
    ('/author/([a-zA-Z0-9_-]{3,20})/profile', ProfileHandler),
    # /<username>/newpost -> to submit a new post
    ('/([a-zA-Z0-9_-]{3,20})/newpost', NewpostHandler),
    ('/(.*)', Error404Handler)
]

app = webapp2.WSGIApplication(routes=routes, debug=True)
