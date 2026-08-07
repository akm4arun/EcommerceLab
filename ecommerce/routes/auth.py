from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

from ecommerce.extensions import db
from werkzeug.security import check_password_hash
from flask import session
from ecommerce.models import User

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already exists.", "danger")
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)

        user = User(
            name=name,
            email=email,
            password_hash=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")

        return redirect(url_for("home.home"))

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):

            session["user_id"] = user.id
            session["user_name"] = user.name
            session["role"] = user.role

            flash("Logged in successfully.", "success")

            return redirect(url_for("home.home"))

        flash("Invalid email or password.", "danger")

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():

        session.clear()

        flash("Logged out successfully.", "success")

        return redirect(url_for("home.home"))