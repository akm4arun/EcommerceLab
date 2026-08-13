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


CATEGORY_PRODUCTS = {
    "Electronics": ELECTRONICS,
    "Books": BOOKS,
    "Fashion": FASHION,
    "Home & Kitchen": HOME_KITCHEN,
    "Sports": SPORTS,
    "Toys": TOYS,
    "Beauty": BEAUTY,
    "Automotive": AUTOMOTIVE,
}

def seed_category(products):
    inserted = 0
    updated = 0

    for item in products:

        product = Product.query.filter_by(
            name=item["name"],
            category=item["category"]
        ).first()

        if product:

            # Update existing product
            for key, value in item.items():
                setattr(product, key, value)

            updated += 1

        else:
            db.session.add(Product(**item))
            inserted += 1

    return inserted, updated

app = create_app()

with app.app_context():

    total_inserted = 0
    total_updated = 0

    try:

        for category, products in CATEGORY_PRODUCTS.items():

            inserted, updated = seed_category(products)

            total_inserted += inserted
            total_updated += updated

            print(
                f"{category}: "
                f"Inserted={inserted}, Updated={updated}"
            )

        db.session.commit()

        print("\n========== SUMMARY ==========")
        print(f"Inserted : {total_inserted}")
        print(f"Updated  : {total_updated}")
        print("=============================")
        print("\n✅ Seed completed successfully.")

    except Exception as ex:

        db.session.rollback()

        print("Seeding failed!")

        raise ex