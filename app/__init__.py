from flask import Flask

from app import pages
from .endpoints import api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    app.register_blueprint(api, url_prefix='/api')

    return app
