frames = [
    ["car", "truck"],
    ["pedestrian", "bicycle"],
    ["car", "motorcycle", "bus"]
]
all_objects = []
for frame in frames:
    for obj in frame:
        all_objects.append(obj)

all_objects_comprehension = [obj for frame in frames for obj in frame]

unique_objects = set(all_objects)