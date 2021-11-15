import pytest

from apps.base.models import Page
from db import session


@pytest.fixture
def client(app):
    return app.test_client()


def test_base():
    a = 4*5*2
    assert a == 40


def test_get(client):
    res = client.get('/')
    assert res.status_code == 200
