detections = [
    ("car", 0.95),
    ("pedestrian", 0.88),
    ("car", 0.91),
    ("bicycle", 0.82),
    ("pedestrian", 0.90),
    ("truck", 0.87)
]
for detection in detections:
    label, confidence = detection
    print(f"{label}: {confidence}")

labels = set(label for label, _ in detections)
print("Unique labels:", labels)

if "car" in labels:
    print("Car detected!")

camera_objects = {"car", "pedestrian", "bicycle"}
lidar_objects = {"car", "truck", "pedestrian"}

# Find objects detected by both sensors
common_objects = camera_objects & lidar_objects
print("Objects detected by both sensors:", common_objects)

# Find objects detected by either sensor
all_objects = camera_objects | lidar_objects
print("All detected objects:", all_objects)

# Find objects detected by camera but not by lidar
camera_only_objects = camera_objects - lidar_objects
print("Objects detected by camera but not by lidar:", camera_only_objects)