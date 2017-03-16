'''
This file contains the class that handles logged in user welcome page logic
'''
from base import BaseHandler
from user_model import User
from blog_model import Blog

# handler class for route '/welcome'
class WelcomeHandler(BaseHandler):

    def get(self, param_username):
        # if active user is present and its username matches username in url
        if self.user and self.user.username == param_username:
            blogs = self.user.getBlogs()
            for blog in blogs:
                print blog.subject
            self.render('welcome.html', username=self.user.username, blogs=blogs)
        # if user not found or username mismatch, go to homepage
        else:
            self.redirect('/')
