import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory

from bookviz import app


@app.route('/')
def index():
    return render_template('index.html')
