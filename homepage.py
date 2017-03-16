'''
This file contains the controller class for the homepage
'''
from base import BaseHandler
from google.appengine.ext import db
from blog_model import Blog
import json
import webapp2

# handler class for route '/' - homepage, displays all blog entries
class HomePageHandler(BaseHandler):
    def render_front(self, user=None, error=""):
        blogs = Blog.getAll()
        self.render('front.html', user=user, blogs = blogs)

    # user visits page, serve front.html
    def get(self, param):
        # if user wants json format of the page
        if param == '.json':
            return self.serveJson()
        # otherwise, serve normal html file
        self.render_front(user=self.user)

    # sends JSON formatted page of the homepage
    def serveJson(self):
        # create a json representation of blogs
        blogs = Blog.getAll()
        json_file = []
        for blog in blogs:
            d = {'subject': str(blog.subject), 'content': str(blog.content)}
            json_file.append(d)
        json_out = json.dumps(json_file)
        self.write(json_out)
