import pytest


@pytest.fixture
def client(app):
    return app.test_client()


def test_base():
    a = 4*5
    assert a == 20


def test_get(client):
    res = client.get('/')
    assert res.status_code == 200
