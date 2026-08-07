from ecommerce import create_app
from ecommerce.extensions import db
from ecommerce.models import User

app = create_app()

with app.app_context():

    user = User.query.filter_by(
        email="arun2@test.com"      # Change if your email is different
    ).first()

    if user:

        user.role = "admin"

        db.session.commit()

        print(f"{user.email} is now an ADMIN.")

    else:

        print("User not found.")