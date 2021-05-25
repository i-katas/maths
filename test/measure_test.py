def test_offset():
    assert offset(5, 1) == -4
    assert offset(5, -3) == -8
    assert offset(-3, 5) == 8


def test_distance():
    assert distance(5, 1) == 4
    assert distance(5, -3) == 8
    assert distance(-3, 5) == 8


def test_mid():
    assert mid(1, 3)  == 2
    assert mid(3, 1)  == 2
    assert mid(-1, -3)  == -2
    assert mid(-3, -1)  == -2


def distance(x1, x2):
    return abs(x2 - x1) #abs(offset(x1, x2))


def offset(x1, x2):
    return x2 - x1


def mid(x1, x2):
    return (x1 + x2) >> 1  #x1 + offset(x1, x2) / 2


