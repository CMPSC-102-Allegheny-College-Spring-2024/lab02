"""Test suite to ensure that each function words correctly."""

from rootfinder import __version__

from pytest import approx

from rootfinder import rootfind


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"


def test_calculate_x_values_non_imaginary():
    """Check that the calculation of x values works if they are not imaginary."""
    a = 1
    b = 2
    c = 1
    x_one, x_two = rootfind.calculate_quadratic_equation_roots(a, b, c)
    assert x_one == -1.0
    assert x_two == -1.0


def test_calculate_x_values_imaginary():
    """Check that the calculation of x values works if they are imaginary."""
    a = 1
    b = 1
    c = 1
    x_one, x_two = rootfind.calculate_quadratic_equation_roots(a, b, c)
    assert x_one == approx(-0.499999 + 0.866025j, rel=1e-5)
    assert x_two == approx(-0.500000 - 0.866025j, rel=1e-5)
