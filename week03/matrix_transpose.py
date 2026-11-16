vehicle_data = [
    [30, 40, 50],
    [10, 20, 30],
    [5,  6,  7]
]
transposed = list(zip(*vehicle_data))
print(transposed)  # Output: [(30, 10, 5), (40, 20, 6), (50, 30, 7)]
a=zip(vehicle_data)
print(list(a))
print(list(zip(*vehicle_data)))