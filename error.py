from base import BaseHandler
class Error404Handler(BaseHandler):
    def get(self):
        self.render('error404.html', user=self.user)
