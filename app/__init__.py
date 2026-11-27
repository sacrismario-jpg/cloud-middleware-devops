import json
import logging
import uuid
import os 
import sys

from flask.logging import default_handler
from datetime import datetime, timezone
from pathlib import Path
from logging.handlers import RotatingFileHandler

from flask import Flask, request, g, has_request_context
from werkzeug.exceptions import HTTPException

from app.config import Config
from app.routes import main


class JSONFormatter(logging.Formatter):

    def format(self, record):
        log_entry = {
            "timestamp": datetime.fromtimestamp(
                record.created,
                timezone.utc
            ).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        if has_request_context():
            log_entry.update({
                "request_id": getattr(g, "request_id", None),
                "method": request.method,
                "path": request.path,
            })

        status_code = getattr(record, "status_code", None)

        if status_code is not None:
            log_entry["status_code"] = status_code

        if record.exc_info:
            log_entry["exception"] = self.formatException(
                record.exc_info
            )

        return json.dumps(log_entry, ensure_ascii=False)


def configure_logging(app):
    if app.testing:
        return

    # Eliminar el manejador predeterminado de Flask.
    if default_handler in app.logger.handlers:
        app.logger.removeHandler(default_handler)

    # Evitar duplicar nuestros propios manejadores.
    for handler in app.logger.handlers[:]:
        if getattr(handler, "_cloudlab_handler", False):
            app.logger.removeHandler(handler)
            handler.close()

    app.logger.setLevel(logging.INFO)

    # Docker: enviar logs JSON a stdout.
    if os.getenv("LOG_TO_STDOUT") == "1":
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JSONFormatter())
        handler._cloudlab_handler = True
        app.logger.addHandler(handler)

    # Ejecución tradicional: guardar logs en archivo.
    else:
        log_dir = Path(app.root_path).parent / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)

        handler = RotatingFileHandler(
            log_dir / "app.log",
            maxBytes=10240,
            backupCount=5,
            encoding="utf-8"
        )

        handler.setFormatter(JSONFormatter())
        handler._cloudlab_handler = True
        app.logger.addHandler(handler)

def create_app(config=None):

    app = Flask(__name__)

    app.config.from_object(Config)

    if isinstance(config, dict):
        app.config.update(config)

    elif config is not None:
        app.config.from_object(config)

    configure_logging(app)

    app.register_blueprint(main)

    @app.before_request
    def assign_request_id():
        g.request_id = str(uuid.uuid4())

    @app.after_request
    def log_request(response):

        response.headers["X-Request-ID"] = g.request_id

        app.logger.info(
            "HTTP request completed",
            extra={
                "status_code": response.status_code
            }
        )

        return response

    @app.errorhandler(Exception)
    def handle_exception(error):

        if isinstance(error, HTTPException):
            return error

        app.logger.exception(
            "Internal application error"
        )

        return {
            "error": "Error interno del servidor"
        }, 500

    app.logger.info(
        "Flask application initialized"
    )

    return app
