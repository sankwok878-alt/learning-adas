def calculate_deflection(q, L, E, I):
    # q may be zero, but must not be negative
    if q < 0:
        raise ValueError("uniform load q must not be negative")
    if L <= 0:
        raise ValueError("beam length L must be greater than 0")
    if E <= 0:
        raise ValueError("modulus of elasticity E must be greater than 0")
    if I <= 0:
        raise ValueError("moment of inertia I must be greater than 0")
    return (5 * q * L**4) / (384 * E * I)