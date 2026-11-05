
# Vehicle Speed and Distance Calculator

speed_kmh = float(input("Enter vehicle speed in km/h: "))
time_s = float(input("Enter travel time in seconds: "))

speed_ms = speed_kmh / 3.6
distance_m = speed_ms * time_s

print("Speed:", speed_ms, "m/s")
print("Distance:", distance_m, "m")
