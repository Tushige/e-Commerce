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
            print '2222222222222'
            print blog.subject
            print '2222222222222'
            self.error(404)
            return
        print '1111111111111'
        print blog.subject
        print '1111111111111'
        self.render('permalink.html', blog = blog)

    def serveJson(self, postId):
        blog = Blog.get_by_id(int(postId))
        json_file = {'subject': blog.subject, 'content': blog.content}
        json_out = json.dumps(json_file)
        return self.write(json_out)
