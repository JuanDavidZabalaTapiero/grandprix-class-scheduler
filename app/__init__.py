from flask import Flask

from .blueprints import register_blueprints


def create_app():
    app = Flask(__name__)

    # == REGISTRAR BLUEPRINTS ==
    register_blueprints(app)

    return app
