import os

from flask import Flask, render_template

from app.routes.admin_auth_routes import admin_auth_bp
from app.routes.admin_category_routes import category_bp
from app.routes.admin_customer_routes import customer_bp
from app.routes.admin_order_routes import admin_order_bp
from app.routes.admin_product_routes import product_bp
from app.routes.admin_routes import admin_bp
from app.routes.auth_routes import auth_bp
from app.routes.cart_routes import cart_bp
from app.routes.checkout_routes import checkout_bp
from app.routes.order_routes import order_bp
from app.routes.storefront_routes import storefront_bp


def create_app():
    app = Flask(__name__)

    app.secret_key = os.getenv("SECRET_KEY", "dev-only-change-this-secret")

    # ---------------------------------
    # Customer / Storefront
    # ---------------------------------

    app.register_blueprint(storefront_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(order_bp)

    # ---------------------------------
    # Admin Authentication
    # ---------------------------------

    app.register_blueprint(admin_auth_bp)

    # ---------------------------------
    # Admin Dashboard
    # ---------------------------------

    app.register_blueprint(admin_bp)

    # ---------------------------------
    # Admin CRUD
    # ---------------------------------

    app.register_blueprint(customer_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(admin_order_bp)

    # ---------------------------------
    # Existing Root
    # ---------------------------------

    @app.route("/")
    def home():
        return render_template("index.html")

    return app
