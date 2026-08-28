from flask import Flask

from config import Config
from ecommerce.extensions import db, migrate

# Import models so Flask-Migrate can detect them
from ecommerce.models import Product

from ecommerce.routes.home import home_bp
from ecommerce.routes.products import products_bp
from ecommerce.routes.auth import auth_bp
from ecommerce.routes.cart import cart_bp
from ecommerce.routes.orders import orders_bp
from ecommerce.routes.admin import admin_bp
from ecommerce.routes.icm import icm_bp


def create_app(config_class=Config):
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config_class)


    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # IMPORTANT:
    # Do NOT call db.create_all() when using Flask-Migrate.
    # Schema changes will be applied through:
    #     flask db upgrade

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(icm_bp)

    return app
