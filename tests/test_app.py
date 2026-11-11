import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_returns_200(client):
    response = client.get("/")

    assert response.status_code == 200


def test_home_returns_expected_message(client):
    response = client.get("/")

    assert b"Cloud & Middleware Lab: aplicaci\xc3\xb3n funcionando" in response.data
