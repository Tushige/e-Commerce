'''
This file contains the model class that represents the 'entity' User
The class contains class methods that operate on the 'entity' object
'''
from google.appengine.ext import db
from blog_model import Blog
# create 'entity'
class User(db.Model):
        # create column 'title' of type 'String'
        # set the constraint that this field has to be filled before ->into db
        username = db.StringProperty(required = True)
        password = db.StringProperty(required = True)
        occupation = db.StringProperty()
        employment = db.StringProperty()
        email = db.StringProperty()
        created = db.DateTimeProperty(auto_now_add = True)

        # @return: all the blogs submitted by this user
        def getBlogs(self):
            blogs = Blog.all().filter('username =', str(self.username))
            return list(blogs)

        @classmethod
        # method for creating a User object
        # @return: new User
        def createUser(cls, username, password, email):
            newUser = User(username=username, password=password, email=email)
            return newUser

        @classmethod
        # @return: True if username already exists in the database
        #          False otherwise
        def checkRegistration(cls, username):
            c = User.getUserByName(username)
            if c is None:
                return False
            return True

        @classmethod
        # @return: user whose username is the specified username
        #          None otherwise
        def getUserByName(cls, username):
            user = db.GqlQuery("SELECT * FROM User WHERE username= :username", username=username)
            return user.get()

        @classmethod
        def getUserById(cls, user_id):
            return User.get_by_id(int(user_id))

        @classmethod
        # @return: list of blogs submitted by <username>
        def getBlogsByUsername(cls, username):
            blogs = Blog.all().filter('username =', str(username))
            return list(blogs)
