def kmh_to_ms(speed):
    # Convert km/h to m/s
    return speed / 3.6

speeds = [36, 72, 0, 108, 54, 90, 0, 120]

valid_speeds = []

for speed in speeds:
    # Filter out zero speeds
    if speed > 0:
        valid_speeds.append(speed)

converted_speeds = []

for speed in valid_speeds:
    # Convert speed
    converted_speeds.append(kmh_to_ms(speed))


# Sort speeds in descending order
converted_speeds.sort(reverse=True)

# Print ranking using enumerate()
for i, speed in enumerate(converted_speeds, start=1):
    print(f"Rank {i}: {speed:.2f} m/s")

# Calculate average speed
average_speed = sum(converted_speeds) / len(converted_speeds) if converted_speeds else 0
print(f"Average speed: {average_speed:.2f} m/s")