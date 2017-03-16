'''
This file contains the class that handles user signup logic
'''
from base import BaseHandler
from user_model import User
from credential import Credential
# handler class for route '/signup'
class SignupHandler(BaseHandler):
    def get(self):
        self.render('signup.html', user=self.user)

    def post(self):
        # retrieve user input
        username = self.request.get('username')
        password = self.request.get('password')
        vpassword = self.request.get('vpassword')
        email = self.request.get('email')

        # validate inputs
        usernameError = Credential.checkUsername(username)
        passError = Credential.checkPassword(password)
        vpassError = Credential.checkVPassword(password, vpassword)
        isUserRegistered = User.checkRegistration(username)

        # proceed if no error
        if usernameError=='' and passError=='' and vpassError=='' and isUserRegistered is False:
            user = self.saveUser(username, password, email)
            self.login(user)
            self.redirect('/%s' % username)

        # if error found, display them
        else:
            if isUserRegistered is True:
                usernameError = 'user is already registered!'
            self.render('signup.html', user=self.user,
                                       username=username,
                                       email=email,
                                       usernameError=usernameError,
                                       passError=passError,
                                       vpassError=vpassError)
    # database user registration logic
    def saveUser(self, username, password, email):
        hashedPass = Credential.hashCredential(password)
        newUser = User.createUser(username=username, password=hashedPass,email=email)
        newUser.put()
        return newUser

    def login(self, user):
        self.setCookie('user_id', user.key().id())
        self.setCookie('username', user.username)
