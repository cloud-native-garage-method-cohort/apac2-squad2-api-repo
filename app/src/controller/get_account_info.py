import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import request, Blueprint, jsonify
from model.account_info import accountDataInfo

getAccountInfo = Blueprint('GetAccountInfo', __name__)

@getAccountInfo.route('/all')
def index():
    return jsonify(accountDataInfo())

@getAccountInfo.route('/')
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []
    account_list = accountDataInfo()
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for account in account_list:
        if account['id'] == id:
            results.append(account)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)