import os
import tempfile

from flask import Blueprint, jsonify, request
from app.services.detector import ObjectDetector

api = Blueprint("api", __name__)

detector = ObjectDetector()


@api.route("/")
def home():
    return jsonify(
        {
            "application": "AWS ML Inference Platform",
            "status": "running",
        }
    )


@api.route("/health")
def health():
    return jsonify(
        {
            "service": "backend",
            "status": "ok",
            "version": "1.0.0",
        }
    )


@api.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({
            "success": False,
            "error": "No image uploaded"
        }), 400

    image = request.files["image"]

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            temp_path = temp_file.name
            image.save(temp_path)

        predictions = detector.predict(temp_path)
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

    return jsonify({
        "success": True,
        "count": len(predictions),
        "predictions": predictions
    }), 200