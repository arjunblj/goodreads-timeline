
from flask import Flask, flash, request, redirect, render_template, url_for
from rauth.service import OAuth1Service

from bookviz import app


base_url='http://www.goodreads.com/oauth/'

goodreads = OAuth1Service(
    name='goodreads',
    consumer_key=app.config['GOODREADS_CONSUMER_KEY'],
    consumer_secret=app.config['GOODREADS_CONSUMER_SECRET'],
    request_token_url=base_url+'request_token',
    authorize_url=base_url+'authorize',
    access_token_url=base_url+'access_token',
    )


@app.route('/')
def index():

    # head_auth=True is important here; this doesn't work with oauth2 for some reason
    request_token, request_token_secret = goodreads.get_request_token(header_auth=True)
    authorize_url = goodreads.get_authorize_url(request_token)

    return render_template('index.html', authorize_url=authorize_url)
