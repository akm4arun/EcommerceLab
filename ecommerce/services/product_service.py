from ecommerce.extensions import db
from ecommerce.models import Product
from flask import abort


def seed_products():

    if Product.query.count() > 0:
        return

    products = [

        Product(
            name="Gaming Laptop",
            description="Intel i7, 16GB RAM, 1TB SSD",
            price=99999,
            image_url="laptop.jpg",
            stock=5
        ),

        Product(
            name="Wireless Mouse",
            description="Bluetooth Mouse",
            price=1499,
            image_url="mouse.jpg",
            stock=30
        ),

        Product(
            name="Mechanical Keyboard",
            description="RGB Keyboard",
            price=3999,
            image_url="keyboard.jpg",
            stock=12
        )

    ]

    db.session.add_all(products)
    db.session.commit()

def get_all_products(search=None):

    query = Product.query.filter_by(is_active=True)

    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))

    return query.order_by(Product.id).all()


def get_product(product_id):

    product = Product.query.filter_by(
        id=product_id,
        is_active=True
    ).first()

    if not product:
        abort(404)

    return product