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

from ecommerce.extensions import db, migrate
from ecommerce.routes.home import home_bp
from ecommerce.models import Product
from ecommerce.services.product_service import seed_products
from ecommerce.routes.products import products_bp
from ecommerce.routes.auth import auth_bp
from ecommerce.routes.cart import cart_bp
from ecommerce.routes.orders import orders_bp
from ecommerce.routes.admin import admin_bp

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    # existing extension initialization here
    # db.init_app(app)
    # migrate.init_app(app, db)
    # register blueprints, etc.

    print(app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()
        seed_products()

    app.register_blueprint(home_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(admin_bp)

    return app