import pytest

from app import create_app
from app.config import TestingConfig, DevelopmentConfig


@pytest.fixture
def client():
    app = create_app({"TESTING": True})

    with app.test_client() as client:
        yield client


def test_home_returns_200(client):
    response = client.get("/")

    assert response.status_code == 200


def test_home_returns_expected_message(client):
    response = client.get("/")

    assert b"Cloud & Middleware Lab: aplicaci\xc3\xb3n funcionando" in response.data

def test_home_returns_405_for_post(client):
    response = client.post("/")

    assert response.status_code == 405
    assert "GET" in response.headers["Allow"]


def test_unknown_route_returns_404(client):
    response = client.get("/ruta-inexistente")

    assert response.status_code == 404

def test_app_is_created_in_testing_mode(client):
    assert client.application.config["TESTING"] is True

def test_home_returns_html_content_type(client):
    response = client.get("/")

    assert response.content_type == "text/html; charset=utf-8"

def test_home_returns_200_for_head(client):
    response = client.head("/")

    assert response.status_code == 200
    assert response.data == b""

def test_health_returns_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_health_returns_json_content_type(client):
    response = client.get("/health")

    assert response.content_type == "application/json"

def test_app_uses_custom_config():
    app = create_app({"TESTING": True, "CUSTOM_SETTING": "test-value"})

    assert app.config["TESTING"] is True
    assert app.config["CUSTOM_SETTING"] == "test-value"

def test_app_uses_base_config():
    app = create_app()

    assert app.config["TESTING"] is False
    assert app.config["DEBUG"] is False

def test_app_uses_testing_config():
    app = create_app(TestingConfig)

    assert app.config["TESTING"] is True
    assert app.config["DEBUG"] is False

def test_app_uses_development_config():
    app = create_app(DevelopmentConfig)

    assert app.config["TESTING"] is False
    assert app.config["DEBUG"] is True

def test_unexpected_exception_returns_500():
    app = create_app({"TESTING": True})

    @app.route("/test-error")
    def trigger_error():
        raise RuntimeError("Error de prueba")

    client = app.test_client()
    response = client.get("/test-error")

    assert response.status_code == 500
    assert response.get_json() == {
        "error": "Error interno del servidor"
    }
