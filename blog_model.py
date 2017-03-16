'''
This file contains the model class that represents the 'entity' Blog
'''
from google.appengine.ext import db
# create 'entity'
class Blog(db.Model):
        # create column 'title' of type 'String'
        # set the constraint that this field has to be filled before ->into db
        subject = db.StringProperty(required = True)
        content = db.TextProperty(required = True)
        created = db.DateTimeProperty(auto_now_add = True)
        blog_id = db.StringProperty(required = True)
        username = db.StringProperty(required = True)

        @classmethod
        def getAll(cls):
            # @blogs: cursor to the results
            blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC limit 10")
            return blogs
        @classmethod
        def getById(cls, id):
            blog = Blog.all().filter('blog_id =', str(id))
            return blog.get()
