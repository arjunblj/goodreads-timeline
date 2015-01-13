
import os

class Config(object):

    DEBUG = False
    USE_RELOADER = False
    SECRET_KEY = 'S00p3rS3cr3T'

    # Snag your own and set your ENVs.
    GOODREADS_CONSUMER_KEY = os.environ['GOODREADS_CONSUMER_KEY']
    GOODREADS_CONSUMER_SECRET = os.environ['GOODREADS_CONSUMER_SECRET']


class DevelopmentConfig(Config):
    """Local development config settings.
    """

    DEBUG = True
    USE_RELOADER = True

    MONGODB_SETTINGS = {'DB': 'bookviz'}