
def kmh_to_ms(speed_kmh):
    return speed_kmh / 3.6


def calculate_distance(speed_ms, time_s):
    return speed_ms * time_s


speed_kmh = float(input("Enter vehicle speed in km/h: "))
time_s = float(input("Enter travel time in seconds: "))

speed_ms = kmh_to_ms(speed_kmh)
distance_m = calculate_distance(speed_ms, time_s)

print(f"Speed: {speed_ms:.2f} m/s")
print(f"Distance: {distance_m:.2f} m")
