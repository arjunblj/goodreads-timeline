
import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

from bookviz.urls import *
from bookviz.ingest import *

if __name__ == '__main__':
    app.run()
