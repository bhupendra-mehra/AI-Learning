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
from app.utils.admin_auth import admin_required

category_bp = Blueprint(
    "admin_categories",
    __name__,
    url_prefix="/admin/categories",
)

category_bp.before_request(admin_required)


@category_bp.route("/")
def list_categories():
    with SessionLocal() as session:
        category_repository = CategoryRepository(session)
        page = request.args.get("page", 1, type=int)
        
        pagination = category_repository.get_all(page=page, per_page=5)

        return render_template(
            "admin/categories/list.html",
            pagination=pagination,
        )


def save_category(category=None):
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip() or None

    if not name:
        flash("Category name is required.", "error")
        return render_template(
            "admin/categories/category_form.html",
            category=category,
        )

    with SessionLocal() as session:
        repository = CategoryRepository(session)

        existing = repository.get_by_name(name)

        if existing and (
            category is None or existing.id != category.id
        ):
            flash("A category with this name already exists.", "error")
            return render_template(
                "admin/categories/category_form.html",
                category=category,
            )

        try:
            if category is None:
                repository.create(name, description)
                action = "created"
            else:
                # Reload the model in this session before updating.
                current_category = repository.get_by_id(category.id)

                if current_category is None:
                    abort(404)

                repository.update(
                    current_category,
                    name,
                    description,
                )
                action = "updated"

            session.commit()
            flash(f"Category {name} {action} successfully.", "success")

        except IntegrityError:
            session.rollback()
            flash("Unable to save category. Check for duplicate values.", "error")
            return render_template(
                "admin/categories/category_form.html",
                category=category,
            )

    return redirect(url_for("admin_categories.list_categories"))


@category_bp.route("/create", methods=["GET", "POST"])
def create_category():
    if request.method == "POST":
        return save_category()

    return render_template(
        "admin/categories/category_form.html",
        category=None,
    )


@category_bp.route("/<int:category_id>/edit", methods=["GET", "POST"])
def edit_category(category_id):
    with SessionLocal() as session:
        repository = CategoryRepository(session)
        category = repository.get_by_id(category_id)

        if category is None:
            abort(404)

        if request.method == "GET":
            return render_template(
                "admin/categories/category_form.html",
                category=category,
            )

        # Pass the ID, then reload the model in the save session.
        category_id_for_save = category.id

    class CategoryReference:
        id = category_id_for_save

    return save_category(category=CategoryReference())


@category_bp.route("/<int:category_id>/delete", methods=["POST"])
def delete_category(category_id):
    with SessionLocal() as session:
        repository = CategoryRepository(session)
        category = repository.get_by_id(category_id)

        if category is None:
            abort(404)

        if category.products:
            flash(
                "This category has products. Reassign or remove them before deleting it.",
                "error",
            )
            return redirect(url_for("admin_categories.list_categories"))

        try:
            repository.delete(category)
            session.commit()
            flash("Category deleted successfully.", "success")
        except IntegrityError:
            session.rollback()
            flash("Unable to delete this category because it is in use.", "error")

    return redirect(url_for("admin_categories.list_categories"))