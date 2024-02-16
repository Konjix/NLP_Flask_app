from flask import Flask

from .pages import bp
from .endpoints import api

# Stworzenie aplikacji
def create_app():
    app = Flask(__name__)

    app.register_blueprint(bp)
    app.register_blueprint(api, url_prefix='/api')

    return app
