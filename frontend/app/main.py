from app.blueprints.health_check import bp as health_check_bp
from app.blueprints.webui import bp as webui_bp

from flask import Flask


def create_app():
    app = Flask(__name__)

    # app.config.from_envvar('APP_SETTINGS')

    app.register_blueprint(health_check_bp)
    app.register_blueprint(webui_bp)

    return app
