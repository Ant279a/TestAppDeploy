import os
from flask import Flask
from .views import register_blueprints
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    #Set flask key
    app.secret_key = 'test'


    # Register blueprints for views
    register_blueprints(app)

    return app
