from ecommerce.extensions import db
from ecommerce.models import Product


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

def get_all_products():
    return Product.query.order_by(Product.id).all()

def get_product(product_id):
    return Product.query.get_or_404(product_id)