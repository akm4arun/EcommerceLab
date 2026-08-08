import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    FLASK_ENV = os.getenv("FLASK_ENV")

    # SQLALCHEMY_DATABASE_URI = "sqlite:///database/ecommerce.db"
    SQLALCHEMY_DATABASE_URI = (f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'ecommerce.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "ecommerce", "static", "uploads")