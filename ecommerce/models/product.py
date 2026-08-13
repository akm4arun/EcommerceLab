from ecommerce.extensions import db

class Product(db.Model):
    __tablename__ = "products"

    __table_args__ = (
    db.UniqueConstraint('name', 'category', name='uq_product_name_category'),
)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    stock = db.Column(db.Integer, nullable=False, default=0)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    featured = db.Column(db.Boolean, default=False)

    # New fields
    category = db.Column(db.String(50), nullable=False, default="electronics")
    brand = db.Column(db.String(100), nullable=True)
    model = db.Column(db.String(100), nullable=True)
    specifications = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, nullable=False, default=4.0)
    warranty = db.Column(db.String(50), nullable=True)

    order_items = db.relationship("OrderItem", back_populates="product")

    def __repr__(self):
        return f"<Product {self.name}>"