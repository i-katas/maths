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

