'''
This file contains the controller class for blog submit page
'''
from base import BaseHandler
from blog_model import Blog

# handler class for '/newpost' - page for submitting a new post
class NewpostHandler(BaseHandler):
    def render_newpost(self, subject='', content='', error=''):
        self.render('newpost.html', subject=subject, content=content, error=error)
    def get(self):
        self.render_newpost()
    # user submits form
    def post(self):
        # retrieve submission fields
        subject = self.request.get('subject')
        content = self.request.get('content')
        # check that all required fields are filled in
        if subject and content:
            newBlog = Blog(subject=subject, content=content)
            newBlog.content = newBlog.content.replace('\\n', '<br>')
            key = newBlog.put()
            self.redirect("/%s" % str(key.id()))
        else:
            error = 'Please submit both subject and content'
            self.render_newpost(subject, content, error=error)
