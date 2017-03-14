'''
This file contains the class that represents the google datastore 'entity'.
The class contains class methods that operate on the 'entity' object
'''
from google.appengine.ext import db
# create 'entity'
class User(db.Model):
        # create column 'title' of type 'String'
        # set the constraint that this field has to be filled before ->into db
        username = db.StringProperty(required = True)
        password = db.StringProperty(required = True)
        email = db.StringProperty()
        created = db.DateTimeProperty(auto_now_add = True)

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
