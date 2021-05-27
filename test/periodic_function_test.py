def test_period():
    assert f(1) == 0
    assert f(7) == 6
    assert f(8) == 0

    assert f(1, 1) == 1
    assert f(7, 1) == 7
    assert f(8, 1) == 1


def f(x, start=0):
    return (x - 1) % 7 + start
