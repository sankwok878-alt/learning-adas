speeds_kmh = [30, 45, 60, 80, 100, 120, 150]
fast_speeds_kmh = [speed for speed in speeds_kmh if speed >= 80]
speeds_mps = [speed / 3.6 for speed in speeds_kmh]
fast_speeds_mps = [speed/3.6 for speed in speeds_kmh if speed >= 80]