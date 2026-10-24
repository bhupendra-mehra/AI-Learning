import hmac
import os

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

admin_auth_bp = Blueprint(
    "admin_auth",
    __name__,
    url_prefix="/admin",
)


@admin_auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if session.get("admin_authenticated"):
        return redirect(url_for("admin.home"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        admin_username = os.getenv("ADMIN_USERNAME")
        admin_password = os.getenv("ADMIN_PASSWORD")

        if not admin_username or not admin_password:
            flash(
                "Admin credentials are not configured.",
                "error",
            )
            return render_template("admin_auth/login.html")

        username_valid = hmac.compare_digest(
            username,
            admin_username,
        )

        password_valid = hmac.compare_digest(
            password,
            admin_password,
        )

        if username_valid and password_valid:
            session.clear()

            session["admin_authenticated"] = True
            session["admin_username"] = admin_username

            flash(
                "Admin login successful.",
                "success",
            )

            return redirect(url_for("admin.home"))

        flash(
            "Invalid administrator credentials.",
            "error",
        )

    return render_template("admin_auth/login.html")


@admin_auth_bp.route("/logout", methods=["POST"])
def logout():

    session.clear()

    flash(
        "Administrator logged out.",
        "success",
    )

    return redirect(url_for("admin_auth.login"))