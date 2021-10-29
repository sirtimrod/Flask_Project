import pytest

from apps.base.models import Page
from db import session


@pytest.fixture
def client(app):
    return app.test_client()


def test_base():
    a = 4*5*2
    assert a == 40


def add_data():
    page = Page()
    page.internal_ip = '192.168.92.129'
    page.external_ip = '62.152.35.117'
    session.add(page)
    session.commit()


def test_get(client):
    res = client.get('/')
    assert res.status_code == 200
