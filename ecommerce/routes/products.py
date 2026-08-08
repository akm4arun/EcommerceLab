from flask import Blueprint, render_template, request

# from ecommerce.services.product_service import get_all_products
from ecommerce.services.product_service import (
    get_all_products,
    get_product,
)

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)


@products_bp.route("/")
def product_list():

    search = request.args.get("q", "").strip()

    products = get_all_products(search=search)

    return render_template(
        "products.html",
        products=products,
        search=search
    )

@products_bp.route("/<int:product_id>")
def product_detail(product_id):

    product = get_product(product_id)

    return render_template(
        "product_detail.html",
        product=product
    )