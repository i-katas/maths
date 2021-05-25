from pytest import approx
from math import *


def test_expression():
    assert f(0) == 6
    assert f(3) == 0
    assert fy(0) == 7
    assert fy(3) == 1
    assert fx(-2) == 6
    assert fx(1) == 0


def test_slope():
    a = atan(k := -2)
    x1, y1, x2, y2 = 1, f(1), 3, f(3)

    assert (y1 - y2) / (x1 - x2) == approx(tan(a)) == k


def test_monotonicity():
    assert f(-1) - f(1) > 0


# y = k(x + n) + b
def fx(x):
    return f(x) - 2 * 2


# y = kx + b + n
def fy(x):
    return f(x) + 1


# y = kx + b
def f(x):
    return -2 * x + 6
