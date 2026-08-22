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

# Temporary endpoint for Phase 5 monitoring validation.
# Remove after alert testing is complete.
@home_bp.route("/monitoring-test-error")
def monitoring_test_error():
    return "Controlled monitoring test failure", 500

# from flask import Blueprint, current_app, render_template

# home_bp = Blueprint("home", __name__)

# @home_bp.route("/")
# def home():

#     print("APP_NAME =", current_app.config["APP_NAME"])

#     return render_template(
#         "index.html",
#         app_name=current_app.config["APP_NAME"],
#     )