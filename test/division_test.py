def test_synthetic_division():
    x = 5
    q, r = 2 * x**2 - 4 * x + 7, 1

    assert 2 * x**3 - 6 * x**2 + 11 * x - 6 == q * (x - 1) + r
    assert x ** (-0.2) == 1 / (x ** 0.2)
