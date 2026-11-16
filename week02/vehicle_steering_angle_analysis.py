steering_angles = [0, 2, 5, 13, 15, 4]


def calculate_angle_changes(angles):
    angle_changes = []

    for i in range(1, len(angles)):
        change = angles[i] - angles[i - 1]
        angle_changes.append(change)

    return angle_changes


def detect_steering_events(angles, threshold):
    event_count = 0
    event_indices = []

    for i in range(len(angles)):
        if abs(angles[i]) > threshold:
            event_count += 1
            event_indices.append(i + 1)

    return event_count, event_indices


def generate_steering_report(angles, threshold):
    report = {}

    angle_changes = calculate_angle_changes(angles)

    event_count, event_indices = detect_steering_events(
        angle_changes, threshold
    )

    report["angle_changes"] = angle_changes
    report["event_count"] = event_count
    report["event_indices"] = event_indices

    return report


report = generate_steering_report(steering_angles, 7)
print("Steering Report:", report)

test_angles = [10, 15, 20, 35, 30, 10]

report = generate_steering_report(test_angles, 10)

print(report)