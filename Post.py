'''
This file contains the controller class for a new post permalink page
'''
from base import BaseHandler
from blog_model import Blog
import json
# handler class for '/<postId>' - the permalink page of the new post
class PostHandler(BaseHandler):
    def get(self, postId, param):
        if param == '.json':
            return self.serveJson(postId)
        blog = Blog.getById(str(postId))
        if not blog:
            self.error(404)
            return
        self.render('permalink.html', blog = blog, user=self.user)

    def serveJson(self, postId):
        blog = Blog.getById(str(postId))
        json_file = {'subject': blog.subject, 'content': blog.content}
        json_out = json.dumps(json_file)
        return self.write(json_out)
