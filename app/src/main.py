import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import flask
import json
from flask import request, jsonify
from controller.get_account_info import getAccountInfo
from view.index import homepage

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(getAccountInfo , url_prefix='/api/v1/resources/account', methods=['GET'])
app.register_blueprint(homepage , url_prefix='/', methods=['GET'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)