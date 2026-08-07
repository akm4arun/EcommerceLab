from ecommerce.extensions import db
from ecommerce.models import Cart


def add_to_cart(user_id, product_id):

    cart_item = Cart.query.filter_by(
        user_id=user_id,
        product_id=product_id
    ).first()

    if cart_item:

        cart_item.quantity += 1

    else:

        cart_item = Cart(
            user_id=user_id,
            product_id=product_id,
            quantity=1
        )

        db.session.add(cart_item)

    db.session.commit()

def increase_quantity(cart_id):

    cart_item = Cart.query.get_or_404(cart_id)

    cart_item.quantity += 1

    db.session.commit()


def decrease_quantity(cart_id):

    cart_item = Cart.query.get_or_404(cart_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
    else:
        db.session.delete(cart_item)

    db.session.commit()
    
def get_cart_items(user_id):

    return Cart.query.filter_by(
        user_id=user_id
    ).all()