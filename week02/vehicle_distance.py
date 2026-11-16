import sys

def calculate_distance(speed_mps, time_seconds):
    return speed_mps * time_seconds

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vehicle_distance.py <speed> <time>")
        sys.exit(1)

    try:
        speed_mps = float(sys.argv[1])/3.6
        time_seconds = float(sys.argv[2])
    except ValueError:
        print("Please provide valid numbers for speed and time.")
        sys.exit(1)

    distance = calculate_distance(speed_mps, time_seconds)
    print(f"The distance traveled is: {distance:.2f} meters.")