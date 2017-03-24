'''
This file contains the class that handles profile view page
'''
from base import BaseHandler
from user_model import User
from blog_model import Blog
from cache import Cache

class ProfileHandler(BaseHandler):
    def get(self, param_username):
        # signed in user is visiting his/her profile
        if self.user and self.user.username == param_username:
            self.render('profile.html', user=self.user)
        # otherwise, show 404 page
        else:
            self.render('error404.html', user=self.user)

    def post(self, param_username):
        profile_name = self.request.get('profile_name')
        occupation = self.request.get('occupation')
        employment = self.request.get('employment')
        biography = self.request.get('biography')
        self.updateUser(profile_name, occupation, employment, biography)
        # go back to profile page
        self.redirect('/author/%s' %self.user.username)

    # helper function to update the 'user' fields in the db
    def updateUser(self, profile_name, occupation, employment, biography):
        # save profile name
        if profile_name:
            blogs = Cache.getBlogsForUser(self.user.username)
            # flush the cache since we're writing to db
            Cache.flush()
            # update blog username to reflect the changes
            for blog in blogs:
                blog.profile_name = profile_name
                blog.put()
            self.user.profile_name = profile_name;

        if occupation:
            self.user.occupation = occupation
        if employment:
            self.user.employment = employment
        if biography:
            self.user.biography = biography
        # save changes
        self.user.put()
