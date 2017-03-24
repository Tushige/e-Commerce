'''
This file contains the model class that represents the 'entity' User
The class contains class methods that operate on the 'entity' object
'''
from google.appengine.ext import db
from blog_model import Blog
from cache import Cache
# create 'entity'
class User(db.Model):
        # create db columns
        # user credentials
        username = db.StringProperty(required = True) #sign in id
        password = db.StringProperty(required = True) # sign in pass
        email = db.StringProperty()
        created = db.DateTimeProperty(auto_now_add = True)
        # user profile information
        profile_name = db.StringProperty(required = True)
        occupation = db.StringProperty()
        employment = db.StringProperty()
        biography = db.TextProperty()

        @classmethod
        # method for creating a User object
        # @return: new User
        def createUser(cls, username, password, email):
            newUser = User(username=username,
                           password=password,
                           email=email,
                           # profile_name will be username by default
                           profile_name=username)
            return newUser

        @classmethod
        # used to for user registration
        # @return: True if username already exists in the database
        #          False otherwise
        def checkRegistration(cls, username):
            c = User.getUserByProperty('username', username)
            if c is None:
                return False
            return True

        @classmethod
        # used to check for the existence of a user profile
        # @return: True if profile exists
        #          False otherwise
        def profileExists(cls, username):
            c = User.getUserByProperty('username', username)
            if c is None:
                return False;
            return True

        @classmethod
        # @return: the user whose profile name is <profile_name>
        def getUserByProfileName(cls, profile_name):
            return User.getUserByProperty('profile_name', profile_name)

        @classmethod
        def getUserByUsername(cls, username):
            return User.getUserByProperty('username', username)

        @classmethod
        # @return: user with 'property: value'
        def getUserByProperty(cls, property, value):
            user = User.all().filter('%s ='%property, value)
            return user.get()

        @classmethod
        # @return: the user with the id 'user_id'
        def getUserById(cls, user_id):
            return User.get_by_id(int(user_id))
