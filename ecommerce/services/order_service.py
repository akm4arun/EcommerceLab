from ecommerce.extensions import db
from ecommerce.models import Cart, Order


def checkout(user_id):

    cart_items = Cart.query.filter_by(user_id=user_id).all()

    if not cart_items:
        return False

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    order = Order(
        user_id=user_id,
        total_amount=total
    )

    db.session.add(order)

    for item in cart_items:

        item.product.stock -= item.quantity

        db.session.delete(item)

    db.session.commit()

    return True