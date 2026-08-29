from ecommerce.models import Product
from flask import abort


def get_all_products(search=None, sort="name_asc", page=1, per_page=12, category=None):

    query = Product.query.filter_by(is_active=True)

    # Filter by category if provided
    if category:
        query = query.filter(Product.category == category)

    # Search by product name
    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))

    # Sorting
    if sort == "name_desc":
        query = query.order_by(Product.name.desc())
    elif sort == "price_asc":
        query = query.order_by(Product.price.asc())
    elif sort == "price_desc":
        query = query.order_by(Product.price.desc())
    else:
        query = query.order_by(Product.name.asc())

    # Return paginated results
    return query.paginate(page=page, per_page=per_page, error_out=False)


def get_product(product_id):

    product = Product.query.filter_by(
        id=product_id,
        is_active=True
    ).first()

    if not product:
        abort(404)

    return product