#importing libraries
import flask
from flask import Flask, jsonify, request
import nerish_model

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

# page to accept inputs
@app.route('/api_input')
def client():
    return flask.render_template('simple_client.html')


# right now this just returns the data you give it
@app.route('/api', methods=['POST'])
def api():
    input_data = request.json
    output_data = get_keywords(input_data)
    response = jsonify(output_data)
    return response
