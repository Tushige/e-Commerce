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
        profile_name = db.StringProperty(required = True)

        @classmethod
        # @return: A Blog object with the provided fields
        def createBlog(cls, subject, content, username, profile_name):
            newBlog = Blog(subject = subject,
                           content = content,
                           username= username,
                           profile_name = profile_name)
            return newBlog

        @classmethod
        # @return: a list of all blogs in the db
        def getAll(cls):
            # @blogs: cursor to the results
            blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC limit 10")
            return list(blogs)

        @classmethod
        # @return: A blog object whose id is provided
        def getById(cls, id):
            # returns a blog instance
            blog = Blog.get_by_id(int(id))
            return blog

        @classmethod
        # @return: list of blogs submitted by <username>
        def getBlogsByUsername(cls, username):
            blogs = Blog.all().filter('username =', str(username))
            return list(blogs)
