import logging
import sys

import pytest
from flask import Flask
from flask.logging import default_handler

from app import create_app, configure_logging, JSONFormatter
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


def test_ready_returns_ready(client):
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ready"}


def test_ready_returns_json_content_type(client):
    response = client.get("/ready")

    assert response.content_type == "application/json"


def test_response_contains_request_id(client):
    response = client.get("/health")

    assert "X-Request-ID" in response.headers
    assert response.headers["X-Request-ID"]


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

def test_configure_logging_uses_json_stdout(monkeypatch):
    monkeypatch.setenv("LOG_TO_STDOUT", "1")

    app = Flask("test_logging_stdout")
    logger = app.logger

    # Simular la presencia del manejador predeterminado de Flask.
    logger.addHandler(default_handler)

    assert default_handler in logger.handlers

    try:
        configure_logging(app)

        # El manejador predeterminado debe desaparecer.
        assert default_handler not in logger.handlers

        # Debe existir exactamente un manejador propio.
        handlers = [
            handler
            for handler in logger.handlers
            if getattr(handler, "_cloudlab_handler", False)
        ]

        assert len(handlers) == 1

        handler = handlers[0]

        # Debe escribir en stdout.
        assert isinstance(handler, logging.StreamHandler)
        assert handler.stream is sys.stdout

        # Debe utilizar nuestro formateador JSON.
        assert isinstance(handler.formatter, JSONFormatter)

    finally:
        # Limpiar los manejadores después de la prueba.
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

            if handler is not default_handler:
                handler.close()

def test_configure_logging_uses_rotating_file(monkeypatch, tmp_path):
    monkeypatch.delenv("LOG_TO_STDOUT", raising=False)

    app = Flask("test_logging_file")
    app.root_path = str(tmp_path / "app")

    logger = app.logger

    # Simular el manejador predeterminado de Flask.
    logger.addHandler(default_handler)

    try:
        configure_logging(app)

        # El manejador predeterminado debe desaparecer.
        assert default_handler not in logger.handlers

        # Debe existir un manejador de archivo.
        handlers = [
            handler
            for handler in logger.handlers
            if getattr(handler, "_cloudlab_handler", False)
        ]

        assert len(handlers) == 1

        handler = handlers[0]

        # Debe utilizar RotatingFileHandler.
        assert isinstance(handler, logging.handlers.RotatingFileHandler)

        # Debe utilizar nuestro formateador JSON.
        assert isinstance(handler.formatter, JSONFormatter)

        # Debe guardar los registros en la ruta esperada.
        expected_path = tmp_path / "logs" / "app.log"

        assert handler.baseFilename == str(expected_path)
        assert expected_path.exists()

    finally:
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

            if handler is not default_handler:
                handler.close()
