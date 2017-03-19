'''
This file contains the class that handles logged in user welcome page logic
'''
from base import BaseHandler
from user_model import User
from blog_model import Blog

# handler class for route '/welcome'
class WelcomeHandler(BaseHandler):
    def get(self, param_username):
        # if user is visiting his/her profile
        if self.user and self.user.username == param_username:
            blogs = self.user.getBlogs()
            print '------------------'
            print len(blogs)
            print '------------------'
            self.render('welcome.html',user=self.user, blogs=blogs)

        # if visiting someone else's profile
        elif User.profileExists(param_username):
            blogs = Blog.getBlogsByUsername(param_username)
            user = User.getUserByUsername(param_username)
            self.render('author.html', user=self.user, author=user, blogs=blogs)
        else:
            self.render('error404.html', user=self.user)
