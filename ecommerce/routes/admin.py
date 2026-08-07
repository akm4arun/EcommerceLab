from flask import Blueprint, render_template, request, redirect, url_for, flash
from ecommerce.services.admin_service import get_all_products, add_product, get_product, update_product
from ecommerce.decorators.admin import admin_required
from ecommerce.decorators.auth import login_required

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

        add_product(

            name=request.form["name"],
            description=request.form["description"],
            price=float(request.form["price"]),
            stock=int(request.form["stock"]),
            image_url=request.form["image_url"]

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