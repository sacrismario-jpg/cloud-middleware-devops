import logging
from werkzeug.exceptions import HTTPException
from logging.handlers import RotatingFileHandler
from pathlib import Path
from flask import Flask, request

from app.config import Config
from app.routes import main


def configure_logging(app):
    if app.testing:
        return

    log_dir = Path(app.root_path).parent / "logs"
    log_dir.mkdir(exist_ok=True)

    if not any(
        isinstance(handler, RotatingFileHandler)
        for handler in app.logger.handlers
    ):
        file_handler = RotatingFileHandler(
            log_dir / "app.log",
            maxBytes=10240,
            backupCount=5,
            encoding="utf-8"
        )

        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s "
            "[in %(module)s:%(lineno)d]"
        ))

        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)

def create_app(config=None):
    app = Flask(__name__)


    app.config.from_object(Config)

    if isinstance(config, dict):
        app.config.update(config)
    elif config is not None:
        app.config.from_object(config)

    configure_logging(app)

    app.register_blueprint(main)

    @app.after_request
    def log_request(response):
        app.logger.info(
            "%s %s %s",
            request.method,
            request.path,
            response.status_code
        )
        return response

    @app.errorhandler(Exception)
    def handle_exception(error):
        if isinstance(error, HTTPException):
            return error

        app.logger.exception(
            "Error interno de la aplicacion: %s",
             error
        )

        return {"error": "Error interno del servidor"}, 500

    app.logger.info("Aplicacion Flask inicializada correctamente")

    return app
