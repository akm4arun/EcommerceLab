from flask import Blueprint, redirect, url_for, flash, session

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

    success = checkout(session["user_id"])

    if success:

        flash(
            "Order placed successfully!",
            "success"
        )

    else:

        flash(
            "Your cart is empty.",
            "warning"
        )

    return redirect(url_for("cart.cart"))