from flask import Blueprint, render_template

from ecommerce.services.product_service import get_all_products

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)


@products_bp.route("/")
def product_list():

    products = get_all_products()

    return render_template(
        "products.html",
        products=products
    )