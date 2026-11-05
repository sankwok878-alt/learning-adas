def check_vehicle_speed(speed):
    if speed > 100:
        return "Fast"
    elif speed >= 60:
        return "Cruising"
    else:
        return "Slow"
    
speed = float(input("Enter vehicle speed (km/h):"))
status = check_vehicle_speed(speed)
print("Vehicle status:", status)