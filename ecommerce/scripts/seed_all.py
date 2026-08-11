from ecommerce import create_app
from ecommerce.extensions import db
from ecommerce.models import Product

from ecommerce.scripts.seed_electronics import PRODUCTS as ELECTRONICS
from ecommerce.scripts.seed_books import PRODUCTS as BOOKS
from ecommerce.scripts.seed_fashion import PRODUCTS as FASHION
from ecommerce.scripts.seed_home_kitchen import PRODUCTS as HOME_KITCHEN
from ecommerce.scripts.seed_sports import PRODUCTS as SPORTS
from ecommerce.scripts.seed_toys import PRODUCTS as TOYS
from ecommerce.scripts.seed_beauty import PRODUCTS as BEAUTY
from ecommerce.scripts.seed_automotive import PRODUCTS as AUTOMOTIVE

# from seed_electronics import PRODUCTS as ELECTRONICS
# from seed_books import PRODUCTS as BOOKS
# from seed_fashion import PRODUCTS as FASHION
# from seed_home_kitchen import PRODUCTS as HOME_KITCHEN
# from seed_sports import PRODUCTS as SPORTS
# from seed_toys import PRODUCTS as TOYS
# from seed_beauty import PRODUCTS as BEAUTY
# from seed_automotive import PRODUCTS as AUTOMOTIVE


ALL_PRODUCTS = (
    ELECTRONICS
    + BOOKS
    + FASHION
    + HOME_KITCHEN
    + SPORTS
    + TOYS
    + BEAUTY
    + AUTOMOTIVE
)

app = create_app()

with app.app_context():
    added = 0

    for p in ALL_PRODUCTS:
        exists = Product.query.filter_by(name=p['name']).first()
        if not exists:
            db.session.add(Product(**p))
            added += 1

    db.session.commit()
    print(f'Seed completed. Added {added} products.')