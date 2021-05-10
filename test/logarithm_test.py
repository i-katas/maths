from math import log, log2
from pytest import approx
from random import randint


def test_definition():
    base, power = 10, 100

    assert log(power, base) == 2
    assert base ** log(power, base) == power
    assert log(base, base) == 1
    assert log(1, base) == 0


def test_fraction_natural():
    m = rand()

    assert 2 ** m == approx(1 / 2 ** -m)
    assert 2 ** log2(1 / m) == approx(1 / m)
    assert 2 ** -log2(m) == approx(1 / 2 ** log2(m)) == approx(1 / m)
    assert log2(1/m) == approx(-log2(m))


def test_natural_multiplication():
    m, n, b = rand(), rand(), 10

    assert 2 ** log2(n * m) \
            == approx(2 ** log2(n) * 2 ** log2(m)) \
            == approx(2 ** (log2(n) + log2(m)))
    assert log2(n * m) == approx(log2(n) + log2(m))


def test_interchange():
    a, b = rand(), rand()

    assert log(b, a) \
            == approx(log(b, b) / log(a, b)) \
            == approx(1 / log(a, b))
    assert log(b, a) * log(a, b) == approx(1)


def test_change_base():
    a, b, c = rand(), rand(), rand()

    assert log(b, a) \
        == approx(log(b, a) * log(a, c) / log(a, c)) \
        == approx(log(a ** log(b, a), c) / log(a, c)) \
        == approx(log(b, c) / log(a, c))


def test_exponent():
    a, m, n = rand(), rand(), rand()

    assert a ** log(m ** n, a) \
            == approx((a ** log(m, a)) ** n) \
            == approx(a ** (n * log(m, a)))
    assert log(m ** n, a) == approx(n * log(m, a))


def test_fraction_natural():
    a, b = rand(), rand()

    assert 2 ** log2(1/b) \
            == approx(2 ** log2(b ** -1)) \
            == approx(2 ** -log2(b)) 
    assert log(1/b, a) == approx(log(b ** -1, a)) == approx(-log(b, a))


def test_scale():
    a, b, n = rand(), rand(), rand()


    assert log(b ** n , a ** n) == approx(log(b, a))


def rand():
    return randint(5, 10)
