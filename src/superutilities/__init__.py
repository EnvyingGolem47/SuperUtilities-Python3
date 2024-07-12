import re
from flask import Flask, render_template

app = Flask(__name__)

from super_utilities import SuperUtilities

app.register_blueprint(SuperUtilities)