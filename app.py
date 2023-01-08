#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "hi"

@app.route('/hi')
def index():
    return render_template('hello.html')