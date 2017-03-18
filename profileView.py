'''
This file contains the class that handles profile view page
'''
from base import BaseHandler
from user_model import User
from blog_model import Blog
class ProfileViewHandler(BaseHandler):
    def get(self, param_username):
        # if active user is present and its username matches username in url
        if self.user.username == param_username:
            blogs = self.user.getBlogs()
            self.render('welcome.html',user=self.user, blogs=blogs)

        # if user not found or username mismatch, go to homepage
        else:
            # if username exists, visit profile page
            self.redirect('/author/%s' % param_username)
            # else, do nothing
