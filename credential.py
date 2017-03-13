'''
This class 'Credential' contains methods that are used to validate user input
'''
from entity import User
import hashlib
import random
import string
import private

class Credential:
    @staticmethod
    # user input validation logic
    def checkUsername(name):
        error_msg = 'Please enter a valid username!'
        if len(name) < 1:
            return error_msg
        elif name.find(' ') > 0:
            return error_msg
        return ''

    @staticmethod
    def checkPassword(password):
        if len(password) < 1:
            return 'Please enter a valid password!'
        return ''

    @staticmethod
    def checkVPassword(password, vpassword):
        if password != vpassword:
            return 'Passwords do not match!'
        return ''

    @staticmethod
    # @return: sha256 hashed user password
    def hashCredential(cred):
        salt = Credential.getSalt()
        h = hashlib.sha256(cred + private.SECRET + salt).hexdigest()
        return '%s|%s' % (h, salt)

    @staticmethod
    def getSalt(salt=None):
        return ''.join(random.choice(string.letters) for x in xrange(5))

    @staticmethod
    # password correctness checking logic
    def isCredValid(cred, h):
        l = h.split('|')
        salt = l[1]
        return hashlib.sha256(cred + private.SECRET + salt).hexdigest() == l[0]
