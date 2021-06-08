from random import randint
from pytest import approx
from math import *


def test_deg_transformation():
    deg = 90

    assert radians(deg) == pi / 2 == pi / 180 * deg
    assert degrees(pi / 2) == 90 == pi / 2 * 180 / pi



def test_sin():
    deg = pi / 2

    assert degrees(deg) == 90
    assert sin(0) == 0
    assert sin(deg) == 1
    assert sin(-deg) == -sin(deg)
    assert sin(deg + 2 * pi) == sin(deg)

    a, b, c = 3, 4, 5
    assert degrees(asin(a / c)) + degrees(asin(b / c)) + degrees(asin(c / c))  == 180
    assert degrees(asin(a / c) + asin(b / c) + asin(c / c))  == 180



def test_cofunction():
    a = 30 * pi / 180
    b = 90 * pi / 180 - a

    assert degrees(a + b) == degrees(a) + degrees(b) == 90

    assert sin(a) == approx(cos(b)) == approx(1 / 2)
    assert sin(pi / 2 + a) == approx(sin(pi / 2 - a)) == approx(cos(a))
    assert cos(pi / 2 + a) == approx(-cos(pi / 2 - a)) == approx(-sin(a))
    assert tan(a) == approx(cot(b)) == approx(sqrt(3) / 3)
    assert sec(a) == approx(csc(b)) == approx(2 / sqrt(3))


def test_regular_formula():
    a, b = radians(1), radians(3)

    assert sin(a) ** 2 + cos(a) ** 2 == 1
    assert sec(a) ** 2 - tan(a) ** 2 == 1
    assert csc(a) ** 2 - cot(a) ** 2 == 1

    assert tan(a) * cot(a) == 1
    assert sin(a) * csc(a) == 1
    assert cos(a) * sec(a) == 1

    assert sin(a) == approx(tan(a) * cos(a))
    assert cos(a) == approx(cot(a) * sin(a))
    assert tan(a) == approx(sin(a) * sec(a))
    assert cot(a) == approx(cos(a) * csc(a))
    assert sec(a) == approx(tan(a) * csc(a))
    assert csc(a) == approx(cot(a) * sec(a))
    assert cos(a + b) == approx(cos(a) * cos(b) - sin(a) * sin(b))
    assert cos(a - b) == approx(cos(a) * cos(b) + sin(a) * sin(b))
    assert sin(a + b) == approx(cos(a) * sin(b) + sin(a) * cos(b))
    assert sin(a + b) == approx(sin(a) * cos(b) + cos(a) * sin(b))
    assert sin(a - b) == approx(sin(a) * cos(b) - cos(a) * sin(b))
    assert sin(2 * a) == approx(2 * sin(a) * cos(a)) == approx(2 / (tan(a) + cot(a)))
    assert cos(2 * a) == approx(cos(a) ** 2 - sin(a) ** 2) == approx(2 * cos(a) ** 2 - 1) == approx(1 - 2 * sin(a) ** 2)



def sec(x):
    return 1 / cos(x)

def csc(x):
    return 1 / sin(x)

def cot(x):
    return 1 / tan(x)


