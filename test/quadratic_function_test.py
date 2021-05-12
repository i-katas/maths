from functools import reduce
from pytest import approx
from math import sqrt
from random import randint

a, c = randint(1, 20), randint(1, 20)
a2, a4, ac4, b = 2 * a, 4 * a, 4 * a * c, sqrt(4 * a * c) + 1 
delta = b**2 - ac4
assert delta > 0

def f(x):
    return a * (x ** 2) + b * x + c


def test_vertex_formula():
    x = randint(1, 20)
    h, k = -b / a2, -delta / a4

    assert f(-b / a2) == approx(-delta / a4)
    assert approx(f(x)) == a * (x - h) ** 2 + k


def test_intersection_formula():
    x1, x2, x = (-b + sqrt(delta))/a2, (-b - sqrt(delta))/a2, randint(1, 20)

    assert approx(f(x1)) == approx(f(x2)) == 0
    assert f(x) == approx(a * (x1 - x) * (x2 - x))


