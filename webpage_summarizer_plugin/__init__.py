import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from flask import Flask

app = Flask(__name__)

from webpage_summarizer_plugin import routes
