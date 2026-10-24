from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from sqlalchemy.exc import IntegrityError

from app.database import SessionLocal
from app.repositories.category_repository import CategoryRepository
from app.repositories.product_repository import ProductRepository
from app.utils.admin_auth import admin_required

product_bp = Blueprint(
    "admin_products",
    __name__,
    url_prefix="/admin/products",
)

product_bp.before_request(admin_required)


@product_bp.route("/")
def list_products():
    with SessionLocal() as session:
        product_repository = ProductRepository(session)
        page = request.args.get("page", 1, type=int)
               
        pagination = product_repository.get_all(page=page, per_page=5)

        return render_template(
            "admin/products/list.html",
            pagination=pagination,
        )


def save_product(product=None):
    name = request.form.get("name", "").strip()
    sku = request.form.get("sku", "").strip() or None
    price = float(request.form.get("price", "").strip())
    quantity = int(request.form.get("quantity", "").strip())
    category_id = int(request.form.get("category_id", ""))

    if not name:
        flash("Product name is required.", "error")
        return render_template(
            "admin/products/product_form.html",
            product=product,
        )

    if not sku:
        flash("Product sku is required.", "error")
        return render_template(
            "admin/products/product_form.html",
            product=product,
        )

    if not price:
        flash("Product price is required.", "error")
        return render_template(
            "admin/products/product_form.html",
            product=product,
        )
    
    if price and type(price) is str:
            flash("Product price is invalid.", "error")
            return render_template(
                "products/product_form.html",
                product=product,
            )

    if not quantity:
        flash("Product quantity is required.", "error")
        return render_template(
            "admin/products/product_form.html",
            product=product,
        )

    if quantity and type(quantity) is str:
            flash("Product quantity is invalid.", "error")
            return render_template(
                "admin/products/product_form.html",
                product=product,
            )

    if not category_id:
            flash("Select category.", "error")
            return render_template(
                "admin/products/product_form.html",
                product=product,
            )

    with SessionLocal() as session:
        repository = ProductRepository(session)

        # existing = repository.get_by_name(name)

        # if existing and (
        #     product is None or existing.id != product.id
        # ):
        #     flash("A product with this name already exists.", "error")
        #     return render_template(
        #         "products/product_form.html",
        #         product=product,
        #     )

        try:
            if product is None:
                repository.create(name, sku, price, quantity, category_id)
                action = "created"
            else:
                # Reload the model in this session before updating.
                current_product = repository.get_by_id(product.id)

                if current_product is None:
                    abort(404)

                repository.update(
                    current_product,
                    name=name,
                    sku=sku,
                    price=price,
                    quantity=quantity,
                    category_id=category_id
                )
                action = "updated"

            session.commit()
            flash(f"Product {name} {action} successfully.", "success")

        except IntegrityError:
            session.rollback()
            flash("Unable to save category. Check for duplicate values.", "error")
            return render_template(
                "admin/products/product_form.html",
                category_id=category_id,
            )

    return redirect(url_for("admin_products.list_products"))


@product_bp.route("/create", methods=["GET", "POST"])
def create_product():
    if request.method == "POST":
        return save_product()

    with SessionLocal() as session:
        categroy_repository = CategoryRepository(session)
        categories = categroy_repository.get_categories()
        return render_template(
            "admin/products/product_form.html", product=None, categories=categories
        )


@product_bp.route("/<int:product_id>/edit", methods=["GET", "POST"])
def edit_product(product_id):
    with SessionLocal() as session:
        repository = ProductRepository(session)
        product = repository.get_by_id(product_id)
        categroy_repository = CategoryRepository(session)
        categories = categroy_repository.get_categories()

        if product is None:
            abort(404)

        if request.method == "GET":
            return render_template(
                "admin/products/product_form.html", product=product, categories=categories
            )

        # Pass the ID, then reload the model in the save session.
        product_id_for_save = product.id

    class ProductReference:
        id = product_id_for_save

    return save_product(product=ProductReference())


@product_bp.route("/<int:product_id>/delete", methods=["POST"])
def delete_product(product_id):
    with SessionLocal() as session:
        repository = ProductRepository(session)
        product = repository.get_by_id(product_id)

        if product is None:
            abort(404)

        try:
            repository.delete(product)
            session.commit()
            flash(f"Product {product.name} deleted successfully.", "success")
        except IntegrityError:
            session.rollback()
            flash("Unable to delete this product because it is in use.", "error")

    return redirect(url_for("admin_products.list_products"))
