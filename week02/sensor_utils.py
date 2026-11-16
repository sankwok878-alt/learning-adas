def get_all_objects(sensor_data):
    all_objects = [
        object_type
        for sensor, detections in sensor_data.items()
        for object_type, confidence in detections
    ]

    return all_objects
