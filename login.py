'''
This file contains the class that handles user login logic
'''
from base import BaseHandler
from entity import User
from credential import Credential

# handler class for route '/login'
class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        # validate user input
        userError = Credential.checkUsername(username)
        passError = Credential.checkPassword(password)

        # math username with password
        if userError=='' and passError=='':
            user = User.getUserByName(username)
            # username not found in db -> show error
            if user is None:
                self.render('login.html', userError='username not found!')
                return
            hashPass = user.password
            isPassValid = Credential.isCredValid(password, hashPass)

            # username matched with password -> login
            if isPassValid:
                self.setCookie('user_id', user.key().id())
                self.setCookie('username', user.username)
                self.redirect('/welcome')
            # username did not match with password -> show error
            else:
                self.render('login.html', passError='username or password wrong!')
