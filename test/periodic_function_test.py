def test_period():
    assert f(0) == 0
    assert f(6) == 6
    assert f(7) == 0

    assert f(0, start = 1) == 1
    assert f(6, 1) == 7
    assert f(7, 1) == 1


def f(x, start=0):
    return x % 7 + start
