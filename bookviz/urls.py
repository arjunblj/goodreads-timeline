
from flask import Flask, flash, request, redirect, render_template, url_for
from rauth.service import OAuth1Service

from bookviz import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome')