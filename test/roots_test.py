from pytest import approx 
from math import sqrt

def test_multiplciation():
    a, b = 2, 3
    n = 1/2

    assert (a * b) ** n == approx((a ** n) * (b ** n))


def test_exponentiation():
    a = 2
    n, m = 1/2, 4

    assert (a ** n) ** m == approx((a ** m) ** n)


def test_roots_algo():
    assert roots(4, 2) == approx(2)
    assert roots(7, 8) == approx(7 ** (1 / 8))
    assert roots(.1, 8) == approx(.1 ** (1 / 8))
    assert roots(-8, 3) == approx(-8 ** (1 / 3))



def roots(a, n):
    x, e, m = 1, 1e-8, n - 1

    while abs(x - (x :=(m * x + a / x ** m) / n)) > e:
        pass

    return x
        

def test_identities_formula():
    a, b = 2, 3

    assert sqrt(a) - sqrt(b)  \
            == approx((sqrt(a) - sqrt(b)) * (sqrt(a) + sqrt(b)) / (sqrt(a) + sqrt(b))) \
            == approx((a - b) / (sqrt(a) + sqrt(b)))
    assert (sqrt(a) - sqrt(b)) ** -1 \
            == approx(1 / (sqrt(a) - sqrt(b))) \
            == approx((sqrt(a) + sqrt(b)) / (a -b)) 
