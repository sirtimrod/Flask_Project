from flask import Flask

from apps.base import router as home_router


def install_app():

    app = Flask(__name__)

    home_router.install(app)

    return app
