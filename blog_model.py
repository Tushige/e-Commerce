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
        username = db.StringProperty(required = True)

        @classmethod
        def getAll(cls):
            # @blogs: cursor to the results
            blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC limit 10")
            return blogs
        @classmethod
        def getById(cls, id):
            # returns a blog instance
            blog = Blog.get_by_id(int(id))
            return blog
