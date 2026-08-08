from flask import Blueprint, redirect, url_for, flash, session, render_template

from ecommerce.decorators.auth import login_required
from ecommerce.services.order_service import checkout

orders_bp = Blueprint(
    "orders",
    __name__,
    url_prefix="/orders"
)


@orders_bp.route("/checkout")
@login_required
def place_order():

    order = checkout(session["user_id"])

    if order:

        flash(
            f"Order #{order.id} placed successfully!",
            "success"
        )

        return redirect(
            url_for("orders.order_success", order_id=order.id)
        )

    flash(
        "Unable to place order. Your cart may be empty or stock is insufficient.",
        "warning"
    )

    return redirect(
        url_for("cart.cart")
    )
@orders_bp.route("/success/<int:order_id>")
@login_required
def order_success(order_id):

    return render_template(
        "order_success.html",
        order_id=order_id
    )