from pytest import approx, fixture
from functools import reduce
from math import *

@fixture
def funs():
    return [
            lambda x: 5 * x**2 + 3 * x + 10, # y = ax^2 + bx +c
            lambda x: 5 * x + 11, # y = kx + b
            lambda x: 2^x, # y = 2^x
            sin, # y = sin(x)
            log, # y = ln(x)
            lambda x: 1 / x, # y = 1/x
            lambda x: log(100, x) # y = log(100)/log(x)
    ]


def test_functions(funs):
    a, n = 2, 79
    test, k = range(a, n), 7
    skips = set(x for x in test if x % k == 0)

    for f in funs:
        p = [(x, f(x)) for x in test if x % k != 0]

        f1 = df(p)
        errs = []

        for x in range(a, n):
            if f(x) != approx(f1(x), 0.1):
                errs.append(x)

        assert len(errs) and all(e in skips for e in errs)


def df(p):
    return lambda x: reduce(float.__add__, terms(p, x))


def terms(p, x):
    s = [x[1] for x in p]
    for k in range(0, len(p)):
        for i in range(0, len(p)):
            if k != i:
                xi = p[i][0]
                s[k] *= (x - xi) / (p[k][0] - xi)
    return s

