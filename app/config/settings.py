import os
import sys
from dotenv import load_dotenv

dotenv_path = os.path.join('app/config/.env')
load_dotenv(dotenv_path)

class BaseConfig():
    API_PREFIX = os.environ.get('API_PREFIX')
    TESTING = False
    DEBUG = False
    ENV = os.environ.get('FLASK_ENV')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    BASE_HOST = os.environ.get('DEVELOPMENT_BASE_HOST')
    BASE_PORT = os.environ.get('DEVELOPMENT_BASE_PORT')
    # SQLALCHEMY_DATABASE_URI = os.environ.get(
    #     'DEVELOPMENT_SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.environ.get('DEVELOPMENT_DB_USER'),
        os.environ.get('DEVELOPMENT_DB_PASSWORD'),
        os.environ.get('DEVELOPMENT_DB_HOST'),
        os.environ.get('DEVELOPMENT_DB_NAME')
    )
    CELERY_BROKER = os.environ.get('DEVELOPMENT_CELERY_BROKER')
    CELERY_RESULT_BACKEND = os.environ.get('DEVELOPMENT_CELERY_RESULT_BACKEND')


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    BASE_HOST = os.environ.get('PRODUCTION_BASE_HOST')
    BASE_PORT = os.environ.get('PRODUCTION_BASE_PORT')
    # SQLALCHEMY_DATABASE_URI = os.environ.get(
    #     'PRODUCTION_SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.environ.get('PRODUCTION_DB_USER'),
        os.environ.get('PRODUCTION_DB_PASSWORD'),
        os.environ.get('PRODUCTION_DB_HOST'),
        os.environ.get('PRODUCTION_DB_NAME')
    )
    CELERY_BROKER = os.environ.get('PRODUCTION_CELERY_BROKER')
    CELERY_RESULT_BACKEND = os.environ.get('PRODUCTION_CELERY_RESULT_BACKEND')


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    # make celery execute tasks synchronously in the same process
    CELERY_ALWAYS_EAGER = True
