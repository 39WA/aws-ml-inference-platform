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
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]

    image.save("temp.jpg")

    predictions = detector.predict("temp.jpg")

    return jsonify(predictions)