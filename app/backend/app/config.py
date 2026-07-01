import os


class Config:
    """Application configuration."""

    MODEL_PATH = os.getenv(
        "MODEL_PATH",
        "app/models/yolov8n.pt",
    )

    HOST = os.getenv("HOST", "0.0.0.0")

    PORT = int(os.getenv("PORT", "5000"))

    DEBUG = (
        os.getenv("FLASK_DEBUG", "False").lower()
        == "true"
    )