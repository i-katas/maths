from pytest import approx

def test_square_roots():
    a = 3
    assert a ** -2 == 1 / a ** 2


def test_fraction():
    a, m, n = 3, 4, 5
    assert (m / n) ** a == approx((m ** a) / (n ** a))


def test_roots_of_operator():
    assert 4 ** (1 / 2) == 2
    assert 8 ** (1 / 3) == 2


def test_index_multiplication():
    a = 2
    assert (a ** 3) * (a ** 4) == a ** (3 + 4)
    assert approx(2, 3)


def test_division():
    a = 2
    assert (a ** 4) / (a ** 2) == a ** (4 - 2) == 4
    assert (a ** 2) / (a ** 4) == a ** (2 - 4) == 1 / 4
    assert int((a ** (1/3)) ** 6) == a ** (1/3 * 6) == a ** 2 


def test_exponentiation():
    a = 2

    assert (a ** 2) ** 3 == a ** (2 * 3) 


def test_base_multiplication():
    a, b = 2, 3

    assert (a * b) ** 4 == (a ** 4) * (b ** 4)


def test_identities_formula():
    a, b = 2, 3
    n = 1/2

    assert a ** n - b ** n == approx((a - b) / (a ** n + b ** n))
    assert (a ** n - b ** n) ** -1 == approx(1 / (a ** n - b ** n)) == approx((a ** n + b ** n) / (a - b))
    


