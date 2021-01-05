import os
import sys
from dotenv import load_dotenv

dotenv_path = os.path.join("app/config/{env}".format(env=os.environ.get("FLASK_ENV")))
load_dotenv(dotenv_path)


class BaseConfig:
    SERVICE_NAME = "iflask"
    API_PREFIX = os.environ.get("API_PREFIX")
    TESTING = False
    DEBUG = False
    ENV = os.environ.get("FLASK_ENV")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    BASE_HOST = os.environ.get("BASE_HOST")
    BASE_PORT = os.environ.get("BASE_PORT")
    JWT_SECRET_KEY = os.environ.get("USER_SERVICE_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(
        os.environ.get("DB_USER"),
        os.environ.get("DB_PASSWORD"),
        os.environ.get("DB_HOST"),
        os.environ.get("DB_NAME"),
    )
    CELERY_BROKER = os.environ.get("CELERY_BROKER")
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")
