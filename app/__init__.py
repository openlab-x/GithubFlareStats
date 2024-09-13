from flask import Flask

app = Flask(__name__)

from app.views import *  # Importing the views to register routes

def create_app():
    return app
