from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "Cloud & Middleware Lab: aplicación funcionando"

@main.route("/health")
def health():
    return jsonify({"status": "ok"}), 200
