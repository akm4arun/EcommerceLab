# from flask import Flask, app

# from config import Config
# from ecommerce.routes.home import home_bp


# def create_app():

#     app = Flask(__name__)

#     app.config.from_object(Config)

#     print("APP_NAME =", app.config.get("APP_NAME"))
#     print("SECRET_KEY =", app.config.get("SECRET_KEY"))

#     app.register_blueprint(home_bp)

#     return app

from flask import Flask

from config import Config

from ecommerce.extensions import db
from ecommerce.routes.home import home_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(home_bp)

    return app