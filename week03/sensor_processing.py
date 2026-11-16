sensor_data = {
    "camera": [
        ("car", 0.95),
        ("pedestrian", 0.88),
        ("truck", 0.72)
    ],
    "lidar": [
        ("car", 0.91),
        ("bicycle", 0.85),
        ("pedestrian", 0.93)
    ],
    "radar": [
        ("car", 0.89),
        ("truck", 0.81)
    ]
}

for sensor, detections in sensor_data.items():
    for detection in detections:
        object_type, confidence = detection
        print(f"Sensor: {sensor}, Object: {object_type}, Confidence: {confidence}")

object_type = [
    object_type for sensor, detections in sensor_data.items()
      for object_type, confidence in detections
]
unique_objects = set(object_type)

high_confidence_detections = [
    (sensor, object_type, confidence)
    for sensor, detections in sensor_data.items()
    for object_type, confidence in detections
    if confidence >= 0.9
]

sensor_counts = {sensor: len(detections) for sensor, detections in sensor_data.items()}

object_camera = [
    object_type for object_type, confidence in sensor_data["camera"]
]
object_lidar = [
    object_type for object_type, confidence in sensor_data["lidar"] 
]
common_objects = set(object_camera) & set(object_lidar)
all_objects = set(object_camera) | set(object_lidar)
camera_only = set(object_camera) - set(object_lidar)
symmetric_difference = set(object_camera) ^ set(object_lidar)