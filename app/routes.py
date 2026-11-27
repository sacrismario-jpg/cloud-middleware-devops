from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "Cloud & Middleware Lab: aplicación funcionando"

@main.route("/health")
def health():
    """Comprueba que la aplicacion está viva."""
    return jsonify({"status": "ok"}), 200

@main.route("/ready")
def ready():
    """Comprueba que la aplicacion está preparada."""
    return jsonify({"status": "ready"}), 200
