'''
class Cache is the interface between the application and in-memory cache
All DB reads go through Cache.
    -   If data is in Cache, Cache serves it
    -   If data is not in Cache, Cache asks it from either
            1.  Blog data model class
            2.  User model class
            -  Blog and User model classes interact directly with DB
'''
from google.appengine.api import memcache
from google.appengine.ext import db
from blog_model import Blog
import private

# helper function to create a list of blogs for specified username
def blogsFilter(blogs, username):
    blogs = [x for x in blogs if x.username==username]
    return blogs

class Cache:
    @staticmethod
    # @return:  'all blogs' from cache if applicable
    #           else 'all blogs' from db
    def getBlogs():
        blogs = memcache.get(private.CACHE_BLOGS_KEY)
        if blogs:
            return blogs
        # if not in cache, read DB
        blogs = Blog.getAll()
        # save it in the cache for future reference
        memcache.set(private.CACHE_BLOGS_KEY, blogs)
        return blogs

    @staticmethod
    # clears the cache on write to db
    def flush():
        memcache.flush_all()

    @staticmethod
    # @return: list of blogs that match the filter
    def getBlogsForUser(username):
        blogs = memcache.get(private.CACHE_BLOGS_KEY)
        # serve from cache
        if blogs:
            return blogsFilter(blogs, username)
        # if not found in cache, read DB
        blogs = Blog.getBlogsByUsername(username)
        return blogs

    @staticmethod
    # @return: blog with specified id
    #          read from DB for now
    def getBlogById(id):
        return Blog.getById(id)
