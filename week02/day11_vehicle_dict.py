vehicle = {
    "speed": 72,
    "steering_angle": 5.5,
    "battery": 85,
    "gear": "D"
}
print("Speed: " + str(vehicle["speed"]))

vehicle["speed"] = 90
vehicle["temperature"] = 36.5
del vehicle["gear"]

print("Updated vehicle data: ")

for key, value in vehicle.items():
    print(key + ": " + str(value))