from .routes import bp

from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_envvar('APP_SETTINGS')
    app.register_blueprint(bp)
    return app
