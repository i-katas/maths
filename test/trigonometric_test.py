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



