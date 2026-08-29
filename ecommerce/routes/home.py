from flask import Blueprint, render_template
from flask import session
from flask import jsonify
from sqlalchemy import text
from ecommerce.extensions import db
from ecommerce.models.product import Product

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    print(session)
    return render_template("index.html")

@home_bp.route("/health")
def health():
    return {"status": "ok"}, 200

# Add this route next to the existing /health route.
@home_bp.route("/health/functional")
def functional_health():
    """
    Read-only application/data validation endpoint used by the deployment gate.
    It deliberately performs no writes, checkout, cart mutation, or order creation.
    """
    checks = {}
    healthy = True

    try:
        db.session.execute(text("SELECT 1"))
        checks["database"] = {"status": "passed"}
    except Exception as exc:
        checks["database"] = {
            "status": "failed",
            "error": type(exc).__name__,
        }
        healthy = False

    try:
        product_count = Product.query.count()
        checks["products"] = {
            "status": "passed" if product_count > 0 else "failed",
            "count": product_count,
        }
        if product_count == 0:
            healthy = False
    except Exception as exc:
        checks["products"] = {
            "status": "failed",
            "error": type(exc).__name__,
        }
        healthy = False

    # Expected application categories.
    # The key is the logical/display name used by the validator.
    # The value is the actual category value stored in the database.
    EXPECTED_CATEGORIES = {
        "electronics": "electronics",
        "fashion": "fashion",
        "books": "books",
        "home_kitchen": "home-kitchen",
        "sports": "sports",
        "toys": "toys",
        "beauty": "beauty",
        "automotive": "automotive",
    }

    # Functional requirement:
    # Every supported category must contain at least one product.
    MIN_PRODUCTS_PER_CATEGORY = 1

    category_counts = {}

    try:
        for category_name, db_category in EXPECTED_CATEGORIES.items():
            count = Product.query.filter_by(category=db_category).count()
            category_counts[category_name] = count

        failed_categories = {
            name: count
            for name, count in category_counts.items()
            if count < MIN_PRODUCTS_PER_CATEGORY
        }

        if failed_categories:
            healthy = False

        checks["categories"] = {
            "status": "passed" if not failed_categories else "failed",
            "counts": category_counts,
            "failed_categories": failed_categories,
            "minimum_required": MIN_PRODUCTS_PER_CATEGORY,
        }

    except Exception as exc:
        checks["categories"] = {
            "status": "failed",
            "error": type(exc).__name__,
        }
        healthy = False

    # Verify that at least one real product record has the fields required by
    # the product-detail/business flow.
    try:
        sample = Product.query.order_by(Product.id.asc()).first()
        required_fields = [sample.name, sample.category, sample.price, sample.image_url] if sample else []
        detail_ok = sample is not None and all(value is not None for value in required_fields)
        checks["product_detail_data"] = {
            "status": "passed" if detail_ok else "failed",
        }
        if not detail_ok:
            healthy = False
    except Exception as exc:
        checks["product_detail_data"] = {
            "status": "failed",
            "error": type(exc).__name__,
        }
        healthy = False

    return jsonify({
        "status": "healthy" if healthy else "unhealthy",
        "checks": checks,
    }), (200 if healthy else 503)
# from flask import Blueprint, current_app, render_template

# home_bp = Blueprint("home", __name__)

# @home_bp.route("/")
# def home():

#     print("APP_NAME =", current_app.config["APP_NAME"])

#     return render_template(
#         "index.html",
#         app_name=current_app.config["APP_NAME"],
#     )