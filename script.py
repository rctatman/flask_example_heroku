#importing libraries
import flask
from flask import Flask, jsonify, request
from serve import get_keywords_api
import json
from flask_httpauth import HTTPBasicAuth

app=Flask(__name__)
auth = HTTPBasicAuth()

# plain text user data
# DO NOT DO THIS IN PRODUCTION
USER_DATA = {
    "user1": "password"
}

# fucntion to varify password passed through API
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

# this will print some text at our app's URL
@app.route('/')
def index():
    return "Up and running!"

# load the model
keywords_api = get_keywords_api()

# API route
@app.route('/api', methods=['POST'])
@auth.login_required
def api():
    """API function
    All model-specific logic to be defined in the get_model_api()
    function
    """
    input_data = request.json
    
    # use our API function to get the keywords
    output_data = keywords_api(input_data)

    # convert our dictionary into a .json file
    response = json.dumps(output_data)
    
    # return our json file
    return response
