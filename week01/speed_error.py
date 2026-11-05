def calculate_speed_error(target_speed, actual_speed):
    error = target_speed - actual_speed
    return error

target_speed = float(input("Enter target speed (km/h): "))
actual_speed = float(input("Enter actual speed (km/h): "))

error = calculate_speed_error(target_speed, actual_speed)
print("Speed error:", error, "km/h")
print("Absolute speed error:", abs(error), "km/h")
