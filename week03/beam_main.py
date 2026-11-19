import csv
from pathlib import Path

from beam import calculate_deflection

CSV_PATH = Path("beam_results.csv")

q = float(input("Enter the uniform load (q) in N/m: "))
L = float(input("Enter the length of the beam (L) in m: "))
E = float(input("Enter the modulus of elasticity (E) in Pa: "))
I = float(input("Enter the moment of inertia (I) in m^4: "))

delta_m = calculate_deflection(q, L, E, I)
delta_mm = delta_m * 1000  # Convert to millimeters

print(f"The maximum deflection of the simply supported beam is: {delta_m:.6f} m")
print(f"The maximum deflection of the simply supported beam is: {delta_mm:.6f} mm")

# Save this run, then print all saved records
write_header = not CSV_PATH.exists()
with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if write_header:
        writer.writerow(["q_N_per_m", "L_m", "E_Pa", "I_m4", "deflection_m", "deflection_mm"])
    writer.writerow([q, L, E, I, f"{delta_m:.6f}", f"{delta_mm:.6f}"])

print("\nSaved records:")
with open(CSV_PATH, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(
            f"q={row['q_N_per_m']} N/m, "
            f"L={row['L_m']} m -> "
            f"{row['deflection_m']} m ({row['deflection_mm']} mm)"
        )