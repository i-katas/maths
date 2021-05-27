def test_period():
    assert f(0) == 0
    assert f(6) == 6
    assert f(7) == 0


def f(x):
    return x % 7
