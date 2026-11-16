# Vehicle kinematics

speeds_kmh = [36, 90, 108]
times_s = [20, 15, 30]

# Convert km/h to m/s, Calculate distance

speed_ms = [speed / 3.6 for speed in speeds_kmh]
for i, (speed, time) in enumerate(zip(speed_ms, times_s), start=1):
    distance = speed * time
    print(f"Vehicle {i}: Speed = {speed:.2f} m/s, Time = {time} s, Distance = {distance:.2f} m")
