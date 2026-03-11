from flask import Flask

from config import Config

from app.routes.main_routes import main
from app.routes.prediction_routes import prediction


def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    app.config.from_object(Config)
    app.register_blueprint(main)
    app.register_blueprint(prediction)

    return app
