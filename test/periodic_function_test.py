def test_period():
    assert f(1) == 1
    assert f(7) == 7
    assert f(8) == 1


def f(x):
    return (x - 1) % 7 + 1
