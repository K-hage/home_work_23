from flask import Flask

from app.views import main_bp


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(main_bp)

    return app
