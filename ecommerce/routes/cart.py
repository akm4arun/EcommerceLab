from flask import Blueprint, render_template, session, redirect, url_for

from ecommerce.decorators.auth import login_required
from ecommerce.services.cart_service import add_to_cart, get_cart_items


cart_bp = Blueprint(
    "cart",
    __name__,
    url_prefix="/cart"
)


# @cart_bp.route("/")
# @login_required
# def cart():

#     return render_template("cart.html")

@cart_bp.route("/")
@login_required
def cart():

    items = get_cart_items(
        session["user_id"]
    )

    total = sum(
    item.product.price * item.quantity
    for item in items
)

    return render_template(
    "cart.html",
    items=items,
    total=total
)

@cart_bp.route("/add/<int:product_id>", methods=["POST"])
@login_required
def add_product(product_id):

    user_id = session["user_id"]

    add_to_cart(
        user_id=user_id,
        product_id=product_id
    )

    return redirect(url_for("cart.cart"))