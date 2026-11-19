import pytest
from pytest import approx
from beam import calculate_deflection


def test_example_values():
    # q=1000 N/m, L=4 m, E=2.1e11 Pa, I=8e-6 m^4
    result = calculate_deflection(1000, 4, 2.1e11, 8e-6)
    assert result == approx(0.001984127, rel=1e-6)
def test_zero_load():
    # A zero uniform load should produce zero deflection
    result = calculate_deflection(0, 4, 2.1e11, 8e-6)
    assert result == 0
def test_double_load_doubles_deflection():
    # Deflection is proportional to q, so doubling q should double delta
    d1 = calculate_deflection(1000, 4, 2.1e11, 8e-6)
    d2 = calculate_deflection(2000, 4, 2.1e11, 8e-6)
    assert d2 == approx(2 * d1)

def test_negative_load_raises():
    with pytest.raises(ValueError):
        calculate_deflection(-1000, 4, 2.1e11, 8e-6)


def test_zero_length_raises():
    with pytest.raises(ValueError):
        calculate_deflection(1000, 0, 2.1e11, 8e-6)


def test_zero_modulus_raises():
    with pytest.raises(ValueError):
        calculate_deflection(1000, 4, 0, 8e-6)