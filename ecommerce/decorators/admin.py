from functools import wraps

from flask import (
    flash,
    redirect,
    session,
    url_for,
)

from ecommerce.models import User


def admin_required(view):

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        user_id = session.get("user_id")

        if not user_id:

            flash(
                "Please login first.",
                "warning"
            )

            return redirect(
                url_for("auth.login")
            )

        user = User.query.get(user_id)

        if not user or user.role != "admin":

            flash(
                "You are not authorized to access this page.",
                "danger"
            )

            return redirect(
                url_for("home.home")
            )

        return view(*args, **kwargs)

    return wrapped_view