from flask import Blueprint, render_template

from ecommerce.decorators.auth import login_required

cart_bp = Blueprint(
    "cart",
    __name__,
    url_prefix="/cart"
)


@cart_bp.route("/")
@login_required
def cart():

    return render_template("cart.html")