from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def detect_survivors(image_path):

    results = model(image_path)

    survivors = []

    for result in results:

        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])

            if cls == 0:

                confidence = float(box.conf[0])

                survivors.append(
                    {
                        "confidence": round(confidence, 2)
                    }
                )

    return {
        "survivors_found": len(survivors),
        "detections": survivors
    }
