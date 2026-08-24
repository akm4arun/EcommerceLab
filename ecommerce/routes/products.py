from flask import Blueprint, render_template, request
from ecommerce.services.product_service import get_all_products, get_product

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)

VALID_CATEGORIES = [
    "electronics",
    "fashion",
    "books",
    "home-kitchen",
    "sports",
    "toys",
    "beauty",
    "automotive"
]


@products_bp.route("/")
def product_list():
    raise RuntimeError("SIMULATED_PRODUCTION_INCIDENT: products endpoint failure")

    search = request.args.get("q", "").strip()
    sort = request.args.get("sort", "name_asc")
    page = request.args.get("page", 1, type=int)

    pagination = get_all_products(
        search=search,
        sort=sort,
        page=page,
        per_page=12
    )

    return render_template(
        "products.html",
        products=pagination.items,
        pagination=pagination,
        search=search,
        sort=sort,
        current_category=None,
        page_title="All Products"
    )


@products_bp.route('/category/<category>')
def products_by_category(category):

    category = category.lower()

    # support both home_kitchen and home-kitchen URLs
    category = category.replace('_' , '-')

    if category not in VALID_CATEGORIES:
        return render_template('404.html'), 404

    search = request.args.get('q', '').strip()
    sort = request.args.get('sort', 'name_asc')
    page = request.args.get('page', 1, type=int)

    pagination = get_all_products(
        search=search,
        sort=sort,
        page=page,
        per_page=12,
        category=category
    )

    DISPLAY_NAMES = {
        'electronics': 'Electronics',
        'fashion': 'Fashion',
        'books': 'Books',
        'home-kitchen': 'Home & Kitchen',
        'sports': 'Sports & Fitness',
        'toys': 'Toys',
        'beauty': 'Beauty',
        'automotive': 'Automotive'
    }

    return render_template(
        'products.html',
        products=pagination.items,
        pagination=pagination,
        search=search,
        sort=sort,
        current_category=category,
        page_title=f"{DISPLAY_NAMES.get(category, category.title())} Products"
    )


@products_bp.route("/<int:product_id>")
def product_detail(product_id):

    product = get_product(product_id)

    return render_template(
        "product_detail.html",
        product=product
    )