from base import BaseHandler
class Error404Handler(BaseHandler):
    def get(self, param):
        if self.user:
            print '*******************'
            print self.user.profile_name
            print param
            print '*******************'
        self.render('error404.html', user=self.user)
