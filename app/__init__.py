from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    """Creates a Flask instance of the app."""
    app = Flask(__name__)
    jwt = JWTManager(app)
    return app