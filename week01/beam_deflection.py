def calculate_deflection(q, L, E, I):
    # Only perform the calculation here
    maximum_deflection = (5 * q * L**4) / (384 * E * I)
    return maximum_deflection

q = float(input("Enter the uniform load (q) in N/m: "))
L = float(input("Enter the length of the beam (L) in m: "))
E = float(input("Enter the modulus of elasticity (E) in Pa: "))
I = float(input("Enter the moment of inertia (I) in m^4: "))

calculated_deflection = calculate_deflection(q, L, E, I)
calculate_deflection_mm = calculated_deflection * 1000  # Convert to millimeters

print(f"The maximum deflection of the simply supported beam is: {calculated_deflection:.6f} m")
print(f"The maximum deflection of the simply supported beam is: {calculate_deflection_mm:.6f} mm")