import re
import webapp2

from homepage import HomePageHandler
from NewPost import NewpostHandler
from Post import PostHandler
from signup import SignupHandler
from signin import SigninHandler
from signout import SignoutHandler
from welcome import WelcomeHandler
import string
routes = [
    ('/(.json){0,1}', HomePageHandler),
    # /<post_id> -> page of a blog post
    ('/entry/([%s]{1,100})(.json){0,1}' % string.ascii_letters, PostHandler),
    # /signup -> page for registering new user
    ('/signup', SignupHandler),
    # /login -> page for logging in
    ('/signin', SigninHandler),
    # /logout -> logout user
    ('/signout', SignoutHandler),
    # /username -> user front page
    ('/([a-zA-Z0-9_-]{3,20})', WelcomeHandler),
    # /<username>/newpost -> to submit a new post
    ('/([a-zA-Z0-9_-]{3,20})/newpost', NewpostHandler)
]

app = webapp2.WSGIApplication(routes=routes, debug=True)
