from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return render_template("index.html")

# from flask import Blueprint, current_app, render_template

# home_bp = Blueprint("home", __name__)

# @home_bp.route("/")
# def home():

#     print("APP_NAME =", current_app.config["APP_NAME"])

#     return render_template(
#         "index.html",
#         app_name=current_app.config["APP_NAME"],
#     )