from ecommerce.extensions import db
from ecommerce.models import Cart, Order, OrderItem


def checkout(user_id):

    cart_items = Cart.query.filter_by(user_id=user_id).all()

    if not cart_items:
        return False

    # Validate stock
    for item in cart_items:

        if item.quantity > item.product.stock:
            return False

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    order = Order(
        user_id=user_id,
        total_amount=total,
        status="Pending"
    )

    db.session.add(order)

    # Flush generates order.id before commit
    db.session.flush()

    for item in cart_items:

        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product.id,
            quantity=item.quantity,
            unit_price=item.product.price
        )

        db.session.add(order_item)

        item.product.stock -= item.quantity

        db.session.delete(item)

    db.session.commit()

    return order

def get_all_orders():

    return (
        Order.query
        .order_by(Order.created_at.desc())
        .all()
    )