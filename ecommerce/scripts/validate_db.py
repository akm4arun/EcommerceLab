from pathlib import Path

from ecommerce import create_app
from ecommerce.models import Product

app = create_app()


VALID_CATEGORIES = {
    "electronics",
    "books",
    "fashion",
    "home-kitchen",
    "sports",
    "toys",
    "beauty",
    "automotive"
}


with app.app_context():

    products = Product.query.all()

    seen = set()
duplicates = []

for product in products:

    key = (
        product.category,
        product.name.lower().strip()
    )

    if key in seen:
        duplicates.append(product)

    else:
        seen.add(key)

    print("=" * 45)
    print("DATABASE VALIDATION")
    print("=" * 45)
    print(f"\nDuplicate Products : {len(duplicates)}")

    for p in duplicates:
        print(f"  [{p.category}] {p.name}")

    print(f"Products Found : {len(products)}")

    invalid_categories = []

    for product in products:

        if product.category not in VALID_CATEGORIES:
            invalid_categories.append(product)

    print(f"\nInvalid Categories : {len(invalid_categories)}")

    for p in invalid_categories:
        print(f"{p.name} --> {p.category}")

    negative_price = [
        p
        for p in products
        if p.price < 0
    ]

    print(f"Negative Prices : {len(negative_price)}")

    negative_stock = [
        p
        for p in products
        if p.stock < 0
    ]

    print(f"Negative Stock : {len(negative_stock)}")

    missing_brand = [
        p
        for p in products
        if not p.brand
    ]

    print(f"Missing Brand : {len(missing_brand)}")

    missing_images = []

base_path = (
    Path(__file__).resolve().parents[1]
    / "static"
    / "assets"
    / "products"
)

for product in products:

    image_path = base_path / product.image_url

    if not image_path.exists():
        missing_images.append(product)

print(f"\nMissing Images : {len(missing_images)}")

for p in missing_images:
    print(f"  [{p.category}] {p.name}")
    print(f"      image_url : {p.image_url}")

errors = (
    len(duplicates)
    + len(invalid_categories)
    + len(negative_price)
    + len(negative_stock)
    + len(missing_brand)
    + len(missing_images)
)

print("=" * 45)

if errors == 0:
    print("✅ Validation PASSED")
else:
    print(f"❌ Validation FAILED ({errors} issues)")

print("=" * 45)