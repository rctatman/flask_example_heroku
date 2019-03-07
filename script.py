#importing libraries
import flask
from flask import Flask, jsonify, request
from serve import get_keywords_api
import json

app=Flask(__name__)

# update index
@app.route('/')
def index():
    return "Index API"

# page to accept inputs
@app.route('/api_input')
def client():
    return flask.render_template('simple_client.html')


# load the model
keywords_api = get_keywords_api()

# API route
@app.route('/api', methods=['POST'])
def api():
    """API function
    All model-specific logic to be defined in the get_model_api()
    function
    """
    input_data = request.json
    #app.logger.info("api_input: " + str(input_data))
    #output_data = keywords_api(input_data)
    #app.logger.info("api_output: " + str(output_data))
    #response = jsonify(output_data)
    
    print(input_data)
    return json.dumps(input_data)
