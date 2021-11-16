from flask import Flask
# from celery import Celery

import config
from apps.base import router as home_router


# celery = Celery(__name__)


def create_app():

    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY

    # celery.conf.update(app.config)

    home_router.install(app)

    return app
