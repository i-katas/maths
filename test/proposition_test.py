def test_xor():
    assert True ^ True == xor(True, True) == False
    assert True ^ False == xor(True, False) == True
    assert False ^ True == xor(False, True) == True
    assert False ^ False == xor(False, False) == False


def xor(p, q):
    return (p and not q) or (not p and q)
