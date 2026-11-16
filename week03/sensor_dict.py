sensors = {
    "camera": {
        "status": "active",
        "fps": 30
    },
    "lidar": {
        "status": "active",
        "points": 120000
    },
    "radar": {
        "status": "inactive",
        "range": 200
    }
}
print("Camera status: " + sensors["camera"]["status"])

sensors["radar"]["status"] = "active"
sensors["camera"]["fps"] = 60
sensors["GPS"] = {"status": "active"}  # This will add the "GPS" key to the dictionary
sensors["GPS"]["frequency"] = 10  # This will add the "frequency" key to the "GPS" dictionary

for sensor, data in sensors.items():
    for key, value in data.items():
        print(sensor + " " + key + ": " + str(value))