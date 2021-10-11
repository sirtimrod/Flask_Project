from flask import Flask

import router as home_router


def install_app():

    app = Flask(__name__)

    home_router.install(app)

    return app
