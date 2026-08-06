from ecommerce.extensions import db

class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(
        db.Integer, 
        db.ForeignKey('products.id'), 
        nullable=False
    )

    quantity = db.Column(
        db.Integer, 
        nullable=False, 
        default=1
    )

    product = db.relationship(
        "Product",
        backref="cart_items"
    )

    def __repr__(self):
        return f"<Cart {self.product_id}>"