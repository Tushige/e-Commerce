'''
This file contains the controller class for blog submit page
'''
from base import BaseHandler
from blog_model import Blog

# handler class for '/newpost' - page for submitting a new post
class NewpostHandler(BaseHandler):
    def render_newpost(self, subject='', content='', error=''):
        self.render('newpost.html', subject=subject, content=content, user=self.user,error=error)

    def get(self, param_username):
        # welcome user if active user matches user in url
        if self.user is not None and self.user.username==param_username:
            self.render_newpost()
        # blog submission is only allowed if user is logged in
        else:
            return self.redirect('/')

    # user submits form
    def post(self, param_username):
        # retrieve submission fields
        subject = self.request.get('subject')
        content = self.request.get('content')
        username = self.user.username
        # check that all required fields are filled in
        if subject and content:
            newBlog = Blog(subject=subject, content=content, username=username)
            newBlog.content = newBlog.content.replace('\\n', '<br>')
            key = newBlog.put()
            self.redirect("/entry/%s" % str(key.id()))
        else:
            error = 'Please submit both subject and content'
            self.render_newpost(subject=subject, content=content, error=error)
