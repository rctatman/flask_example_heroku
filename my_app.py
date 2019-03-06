#importing libraries
import os
import flask
import pickle

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
