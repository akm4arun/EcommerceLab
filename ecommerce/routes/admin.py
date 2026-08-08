from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session
from ecommerce.services.admin_service import get_all_products, add_product, get_product, update_product
from ecommerce.decorators.admin import admin_required
from ecommerce.decorators.auth import login_required
from werkzeug.utils import secure_filename
from ecommerce.models import Product, User, Order
import os
from ecommerce.extensions import db
from ecommerce.services.order_service import get_all_orders

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


@admin_bp.route("/")
@admin_required
def dashboard():

    return render_template(
        "admin/dashboard.html"
    )

@admin_bp.route("/products")
@login_required
@admin_required
def products():

    products = get_all_products()

    return render_template(
        "admin/products.html",
        products=products
    )

@admin_bp.route("/products/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_product_page():

    if request.method == "POST":

        image = request.files["image"]

        filename = ""

        if image and image.filename:

            filename = secure_filename(image.filename)

            image.save(

                os.path.join(

                    current_app.config["UPLOAD_FOLDER"],
                    filename

                )

            )

        add_product(

            name=request.form["name"],
            description=request.form["description"],
            price=float(request.form["price"]),
            stock=int(request.form["stock"]),
            image_url=filename

        )

        flash(
            "Product added successfully.",
            "success"
        )

        return redirect(
            url_for("admin.products")
        )

    return render_template(
        "admin/product_form.html"
    )

@admin_bp.route("/products/<int:product_id>/edit",
                methods=["GET", "POST"])
@login_required
@admin_required
def edit_product(product_id):

    product = get_product(product_id)

    if request.method == "POST":

        update_product(

            product,

            request.form["name"],
            request.form["description"],
            float(request.form["price"]),
            int(request.form["stock"]),
            request.form["image_url"]

        )

        flash(
            "Product updated successfully.",
            "success"
        )

        return redirect(
            url_for("admin.products")
        )

    return render_template(
        "admin/product_form.html",
        product=product,
        edit=True
    )

@admin_bp.route("/products/edit/<int:product_id>", 
                methods=["GET", "POST"])
@login_required
@admin_required
def edit_product_page(product_id):

    product = Product.query.get_or_404(product_id)

    if request.method == "POST":

        product.name = request.form["name"]
        product.description = request.form["description"]
        product.price = float(request.form["price"])
        product.stock = int(request.form["stock"])

        image = request.files.get("image")

        if image and image.filename:

            filename = secure_filename(image.filename)

            image.save(
                os.path.join(
                    current_app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

            product.image_url = filename

        db.session.commit()

        flash(
            "Product updated successfully.",
            "success"
        )

        return redirect(
            url_for("admin.products")
        )

    return render_template(
        "admin/product_form.html",
        product=product,
        edit=True
    )

# @admin_bp.route("/products/delete/<int:product_id>", methods=["POST"])
# @login_required
# @admin_required
# def delete_product(product_id):

#     product = Product.query.get_or_404(product_id)

#     product.is_active = False

#     db.session.commit()

#     flash(
#         "Product deleted successfully.",
#         "success"
#     )

#     return redirect(
#         url_for("admin.products")
#     )

@admin_bp.route("/products/delete/<int:product_id>", methods=["POST"])
@login_required
@admin_required
def delete_product(product_id):

    product = Product.query.get_or_404(product_id)

    product.is_active = False

    db.session.commit()

    flash(
        "Product deleted successfully.",
        "success"
    )

    return redirect(
        url_for("admin.products")
    )

@admin_bp.route("/products/restore/<int:product_id>", methods=["POST"])
@login_required
@admin_required
def restore_product(product_id):

    product = Product.query.get_or_404(product_id)

    product.is_active = True

    db.session.commit()

    flash(
        "Product restored successfully.",
        "success"
    )

    return redirect(
        url_for("admin.products")
    )

@admin_bp.route("/users")
@login_required
@admin_required
def users():

    users = User.query.order_by(User.id).all()

    return render_template(
        "admin/users.html",
        users=users
    )

# Promote User to Admin
@admin_bp.route("/users/<int:user_id>/promote", methods=["POST"])
@login_required
@admin_required
def promote_user(user_id):

    user = User.query.get_or_404(user_id)

    user.role = "admin"

    db.session.commit()

    flash(
        f"{user.name} promoted to Admin.",
        "success"
    )

    return redirect(
        url_for("admin.users")
    )

# Demote Admin to User
@admin_bp.route("/users/<int:user_id>/demote", methods=["POST"])
@login_required
@admin_required
def demote_user(user_id):

    user = User.query.get_or_404(user_id)

    if user.id == session["user_id"]:
        flash(
            "You cannot demote yourself.",
            "danger"
        )
        return redirect(url_for("admin.users"))

    user.role = "customer"

    db.session.commit()

    flash(
        f"{user.name} is now a Customer.",
        "success"
    )

    return redirect(
        url_for("admin.users")
    )

@admin_bp.route("/orders")
@login_required
@admin_required
def orders():

    orders = get_all_orders()

    return render_template(
        "admin/orders.html",
        orders=orders
    )

# print("Before order_detail")

@admin_bp.route("/orders/<int:order_id>")
@login_required
@admin_required
def order_detail(order_id):

    # print("Inside order_detail definition")

    order = Order.query.get_or_404(order_id)

    return render_template(
        "admin/order_detail.html",
        order=order
    )

# print(">>> admin.py loaded completely")

@admin_bp.route("/orders/<int:order_id>/status", methods=["POST"])
@login_required
@admin_required
def update_order_status(order_id):

    order = Order.query.get_or_404(order_id)

    new_status = request.form["status"]

    allowed_statuses = [
        "Pending",
        "Processing",
        "Shipped",
        "Delivered",
        "Cancelled"
    ]

    if new_status not in allowed_statuses:
        flash("Invalid order status.", "danger")
        return redirect(url_for("admin.order_detail", order_id=order.id))

    order.status = new_status
    db.session.commit()

    flash("Order status updated successfully.", "success")

    return redirect(url_for("admin.order_detail", order_id=order.id))