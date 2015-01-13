
from flask import Flask, redirect, render_template, request, Response, url_for

from bookviz import app, ingest


oauth = ingest.GoodreadsOAuth()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return redirect(oauth.get_auth_url())


@app.route('/authorized')
def authorized():

    authorized = request.args.get('authorize', '')
    if authorized != '1':
        return dict(status='error', msg='Not authorized.')

    print oauth.connect()

    return render_template('index.html')
