from sensor_utils import get_all_objects
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
all_objects = get_all_objects(sensor_data)
print(all_objects)