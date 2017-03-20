'''
This file contains the base controller class for all controllers in this project
'''
import os
import webapp2
import jinja2
from user_model import User
#------------Setup jinja2 template------
# path to our directory containing template files
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = False)

# Base handler class of all handler classes
class BaseHandler(webapp2.RequestHandler):
    # this function runs on every request before anything else
    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        user_id = self.getCookie('user_id')
        self.user = None
        if user_id:
            self.user = User.getUserById(user_id)

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_template(self, template, **kw):
        temp = jinja_env.get_template(template)
        return temp.render(kw)

    def render(self, template, **kw):
        self.write(self.render_template(template, **kw))

    def setCookie(self, name, val):
        self.response.headers.add_header('set-cookie', '%s=%s; Path=/' %(str(name), str(val)))

    def getCookie(self, name):
        return self.request.cookies.get(name)

    def login(self, user):
        self.setCookie('user_id', user.key().id())
        self.setCookie('username', user.username)
        
    def logout(self):
        self.setCookie('user_id', '')
        self.setCookie('username', '')
