from flask import Flask, session,request
from flask_babel import Babel
from config import Config

from app.routes.main_routes import main
from app.routes.prediction_routes import prediction
from app.routes.auth_routes import auth
from app.routes.language_routes import language
from app.routes.chatbot_routes import chatbot
from app.routes.expert_routes import experts_bp


babel = Babel()


def get_locale():

    if "language" in session:
        return session["language"]

    return request.accept_languages.best_match(["en", "hi", "es", "fr"])

def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object(Config)

    app.config["BABEL_DEFAULT_LOCALE"] = "en"
    import os

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    app.config["BABEL_TRANSLATION_DIRECTORIES"] = os.path.join(BASE_DIR, "translations")
    # app.config["BABEL_TRANSLATION_DIRECTORIES"] = "translations"

    babel.init_app(app, locale_selector=get_locale)

    app.register_blueprint(main)
    app.register_blueprint(prediction)
    app.register_blueprint(auth)
    app.register_blueprint(language)
    app.register_blueprint(chatbot)
    app.register_blueprint(experts_bp)

    return app