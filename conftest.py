from app import install_app

import pytest


@pytest.fixture
def app():
    app = install_app(++)
    return app
