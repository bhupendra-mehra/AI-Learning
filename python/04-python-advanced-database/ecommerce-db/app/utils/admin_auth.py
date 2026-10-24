from flask import (
    flash,
    redirect,
    session,
    url_for,
)


def admin_required():
    if not session.get("admin_authenticated"):
        flash("Please log in as administrator.", "error")
        return redirect(url_for("admin_auth.login"))