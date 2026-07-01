from flask import Blueprint
from flask import jsonify

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    return jsonify(
        {
            "application": "AWS ML Inference Platform",
            "status": "running",
        }
    )


@main.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "ok",
            "service": "backend",
            "version": "1.0.0",
        }
    )