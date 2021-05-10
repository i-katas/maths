from pytest import approx
from functools import reduce

def test_involution_definition():
    base, exponent = 2, 3

    power = base ** exponent

    assert power == 8


def test_zero_exponent():
    assert 1 ** 0 == 1
    assert 2 ** 0 == 1
    assert 0 ** 0 == 1


def test_square_roots():
    a = 3
    assert a ** -2 == 1 / a ** 2


def test_fraction():
    a, m, n = 3, 4, 5
    assert (m / n) ** a == approx((m ** a) / (n ** a))


def test_roots_of_operator():
    assert 4 ** (1 / 2) == 2
    assert 8 ** (1 / 3) == 2


def test_same_base_multiplication():
    a = 2
    assert (a ** 3) * (a ** 4) == reduce(int.__mul__, [a] * 7)== a ** (3 + 4)


def test_same_base_division():
    a = 2
    assert (a ** 4) / (a ** 2) == a ** (4 - 2) == 4
    assert (a ** 2) / (a ** 4) == a ** (2 - 4) == 1 / 4
    assert int((a ** (1/3)) ** 6) == a ** (1/3 * 6) == a ** 2 


def test_exponentiation():
    a = 2

    assert (a ** 2) ** 3 == reduce(int.__mul__, [a**2] * 3) == a ** (2 * 3) 


def test_same_exponent_multiplication():
    a, b = 2, 3

    assert (a * b) ** 4 == (a ** 4) * (b ** 4)


def test_reciprocal():
    a, n = 3, -2
    assert a**0 == 1
    assert a**n == a**(0 + n) == (a**0) / (a**-n) == 1 / (a**-n)

    

def test_exponentiation_multiplication():
    a = 2
    n, m = 5, 7

    assert a ** (n ** m) \
            == a ** (n * n ** (m - 1)) \
            == (a ** n) ** (n ** (m - 1))

