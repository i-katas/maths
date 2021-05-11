from pytest import approx
from math import *

def test_absolute():
    assert abs(inf) == inf
    assert abs(-inf) == inf
    assert -inf < 0 < inf


def test_arithmetic():
    assert inf * inf == inf
    assert 1 * inf == inf
    assert 1 + inf == inf
    assert -inf * inf == -inf
    assert -inf * -inf == inf
    assert 1 / inf == 0
    assert 1 / -inf == 0


def test_infinitismal_of_high_order():
    for n in range(2, 1000):
        x, e = 1/n, 1e10
        assert x ** 2 < x < 6 * x


def test_eqvuivalent_infinitismal():
    for n in range(2, 1000):
        x, e = 1/n, 1e10
        assert sin(x) == approx(x, e)
        assert tan(x) == approx(x, e)
