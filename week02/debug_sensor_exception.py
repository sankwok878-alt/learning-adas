def calculate_average_confidence(detections):

    total = 0

    for object_type, confidence in detections:
        total += confidence

    try:
        average = total / len(detections)
    except ZeroDivisionError:
        print("No detections available.")
        return None

    else:
        return average


detections = []
result = calculate_average_confidence(detections)
if result is not None:
    print(f"Average confidence: {result:.2f}")
