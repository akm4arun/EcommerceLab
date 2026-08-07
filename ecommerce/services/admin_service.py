from ecommerce.extensions import db
from ecommerce.models import Product


def get_all_products():

    return Product.query.order_by(Product.id).all()


def add_product(
    name,
    description,
    price,
    stock,
    image_url
):

    product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        image_url=image_url
    )

    db.session.add(product)
    db.session.commit()

def get_product(product_id):

    return Product.query.get_or_404(product_id)


def update_product(
    product,
    name,
    description,
    price,
    stock,
    image_url
):

    product.name = name
    product.description = description
    product.price = price
    product.stock = stock
    product.image_url = image_url

    db.session.commit()