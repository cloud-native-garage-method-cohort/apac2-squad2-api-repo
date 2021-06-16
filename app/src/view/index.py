import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Blueprint

homepage = Blueprint('HomePage', __name__)

@homepage.route('/')
def index():
    return '''<h1>Credit Approval Officer</h1>
    <p>A prototype API for the Credit approval officer.</p>'''
