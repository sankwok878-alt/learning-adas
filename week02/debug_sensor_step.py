def calculate_average_confidence(detections):
    total = 0

    for object_type, confidence in detections:
        total += confidence

    average = total / len(detections)

    return average


detections = [
    ("car", 0.95),
    ("pedestrian", 0.88),
    ("truck", 0.72)
]

result = calculate_average_confidence(detections)

print(f"Average confidence: {result:.2f}")