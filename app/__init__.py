import asyncio
import logging
import os
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from app import config
from app.middleware import jwt, jwt_blacklist

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s]: {} %(levelname)s %(message)s".format(os.getpid()),
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    global blacklist
    app = Flask(__name__)
    with app.app_context():

        app.config.from_object(config.settings.BaseConfig)
        app.secret_key = app.config["JWT_SECRET_KEY"]
        jwt.init_app(app)

        # Token blacklist
        @jwt.token_in_blacklist_loader
        def check_if_token_in_blacklist(decrypted_token):
            jti = decrypted_token["jti"]
            return jti in jwt_blacklist

        # initialize SQLAlchemy
        db.init_app(app)

        login_manager.init_app(app)
        login_manager.login_message = "You must be logged in to access this page."
        login_manager.login_view = "auth.login"

        # Workaround to use migration
        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "mysql+pymysql://root:root@127.0.0.1/iflask"

        # initialize migrations
        migrate.init_app(app, db)
        from app import model
        from app import api
        from app.tasks import CeleryQueueMessages
        from app.test import (
            test_1_1,
            test_1_2,
            test_1_3,
            test_2_1,
            test_2_2,
            test_2_3,
            test_3_1,
            test_3_2,
            test_3_3,
            test_4_1,
            test_4_2,
            test_5_1,
            test_5_2,
            test_5_3,
        )

        api.api_restful.init_app(app)
        api.CeleryProcessing(CeleryQueueMessages)

        # define hello world page
        @app.route("/")
        def test():
            test_1_1()
            test_1_2()
            test_1_3()

            test_2_1()
            test_2_2()
            test_2_3()

            test_3_1()
            test_3_2()
            test_3_3()

            test_4_1()
            test_4_2()

            test_5_1()
            test_5_2()
            test_5_3()
            return "Running test"

    return app
