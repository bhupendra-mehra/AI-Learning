from flask import (
    Blueprint,
    abort,
    render_template,
)

from app.database import SessionLocal
from app.repositories.category_repository import CategoryRepository
from app.repositories.product_repository import ProductRepository

storefront_bp = Blueprint(
    "storefront",
    __name__,
    url_prefix="/store",
)


@storefront_bp.route("/")
def home():
    with SessionLocal() as session:
        category_repository = CategoryRepository(session)
        product_repository = ProductRepository(session)

        categories = category_repository.get_categories()
        products = product_repository.get_products()

        return render_template(
            "storefront/home.html",
            categories=categories,
            products=products,
        )


@storefront_bp.route("/category/<int:category_id>")
def category_products(category_id):
    with SessionLocal() as session:
        category_repository = CategoryRepository(session)
        product_repository = ProductRepository(session)

        category = category_repository.get_by_id(category_id)

        if category is None:
            abort(404)

        products = product_repository.get_by_category(category_id)

        return render_template(
            "storefront/category.html",
            categories=category_repository.get_categories(),
            category=category,
            products=products,
        )


@storefront_bp.route("/product/<int:product_id>")
def product_detail(product_id):
    with SessionLocal() as session:
        category_repository = CategoryRepository(session)
        product_repository = ProductRepository(session)

        product = product_repository.get_by_id(product_id)

        if product is None:
            abort(404)

        return render_template(
            "storefront/product_detail.html",
            categories=category_repository.get_categories(),
            product=product,
        )