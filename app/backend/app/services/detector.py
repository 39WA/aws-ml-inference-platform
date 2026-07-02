from pathlib import Path

from ultralytics import YOLO


class ObjectDetector:
    """YOLOv8 object detector."""

    def __init__(self):
        model_path = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "models"
            / "yolov8n.pt"
        )

        self.model = YOLO(str(model_path))

    def predict(self, image_path):
        results = self.model(image_path)

        predictions = []

        for result in results:
            for box in result.boxes:
                predictions.append(
                    {
                        "class": result.names[int(box.cls)],
                        "confidence": round(float(box.conf), 3),
                        "bbox": box.xyxy.tolist()[0],
                    }
                )

        return predictions