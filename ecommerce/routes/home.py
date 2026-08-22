from flask import Blueprint, render_template
from flask import session

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    print(session)
    return render_template("index.html")

@home_bp.route("/health")
def health():
    return {"status": "ok"}, 200


# from flask import Blueprint, current_app, render_template

# home_bp = Blueprint("home", __name__)

# @home_bp.route("/")
# def home():

#     print("APP_NAME =", current_app.config["APP_NAME"])

#     return render_template(
#         "index.html",
#         app_name=current_app.config["APP_NAME"],
#     )