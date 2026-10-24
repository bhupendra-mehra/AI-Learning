from flask import (
    Blueprint,
    render_template,
)

from app.utils.admin_auth import admin_required

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin",
)

admin_bp.before_request(admin_required)

@admin_bp.route("/")
def home():
    return render_template("admin/index.html")