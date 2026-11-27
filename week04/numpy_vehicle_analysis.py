import numpy as np

speed_kmh = np.array([36, 54, 72, 90, 108])

# TODO: Convert km/h to m/s

speed_mps = speed_kmh / 3.6
# TODO: Print the converted speed
print("Speed in m/s:", speed_mps)

# TODO: Calculate the difference between adjacent speeds
diff_speed = np.diff(speed_kmh)

# TODO: Print the result
print("Difference in speed (km/h):", diff_speed)

# TODO: Calculate the square of every element
square_speed = np.square(speed_kmh)
# TODO: Print the result
print("Square of speed (km/h):", square_speed)

# TODO: Select speeds below 80 km/h
selected_speeds = speed_kmh[speed_kmh < 80]
# TODO: Print the result
print("Speeds below 80 km/h:", selected_speeds)

# TODO 1: Calculate the average speed
average_speed = np.mean(speed_kmh)
# TODO 2: Calculate the maximum speed
max_speed = np.max(speed_kmh)
# TODO 3: Print both results
print("Average speed (km/h):", average_speed)
print("Maximum speed (km/h):", max_speed)

# TODO 1: Add 3 to every element
adjusted_speeds = speed_kmh + 3
# TODO 2: Print the adjusted speeds
print("Adjusted speeds (km/h):", adjusted_speeds)