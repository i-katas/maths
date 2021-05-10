from pytest import approx 
from math import sqrt


x, y, z = 7, 11, 13
xy, xz, yz = x * y, x * z, y * z


# 取反法
def test_invert_polynomial():
    assert -x**2 + y == -(x**2 - y)

# 提公因式法
def test_extract_common_factor():
    assert x + x*y + y + 1 == \
            x * (y + 1) + (y + 1) == \
            (x + 1) * (y + 1) 


# 公式法
def test_formula():
    # 平方差
    assert x**2 - y**2 == (x + y) * (x - y)
    # 完全平方
    assert x**2 + 2*xy + y**2 == (x + y)**2
    assert x**2 - 2*xy + y**2 == (x - y)**2
    assert x**2 + 2*xy + 2*xz + 2*yz + y**2 + z**2 == (x + y + z)**2
    # 立方和
    assert x**3 + y**3 == (x + y) * (x**2 - xy + y**2)
    # 立方差
    assert x**3 - y**3 == (x - y) * (x**2 + xy + y**2)
    # 完全立方
    assert x**3 + 3 * x**2 * y + 3 * x * y**2 + y**3 == (x + y) ** 3 
    assert x**3 - 3 * x**2 * y + 3 * x * y**2 - y**3 == (x - y) ** 3 


# 求根公式法
def test_root_finding():
    a, b, c = 7, 3, -15
    b4ac = sqrt(b**2 - 4 * a * c)
    x1 = (-b + b4ac)/(2*a)
    x2 = (-b - b4ac)/(2*a)

    assert a*x**2 + b*x + c == approx(a * (x - x1) * (x - x2))


#十字相乘法
def test_cross_multiplication():
    a1, b1 = 5, 3
    a2, b2 = 7, 11
    a, b, c = a1 * a2, a1 * b2 + b1 * a2, b1 * b2
    delta = sqrt(b**2 - 4 * a * c)

    assert delta ** 2 == b**2 - 4 * a * c
    assert a * x**2 + b * x + c == (a1 * x + b1) * (a2 * x + b2)


#双十字相乘法
def test_cross_multiplication2():
    a1, a2, b1, b2, c1, c2 = 1, 5, 7, 11, 13, 17

    assert a1*a2*x**2 + b1*b2*y**2 + c1*c2 + \
            (a1*b2 + a2*b1)*xy + (a1*c2 + a2*c1)*x + (b1*c2 + b2*c1)*y == \
            (a1*x + b1*y + c1) * (a2*x + b2*y + c2)


# 分组分解法
def test_group_multiplication():
    a, b = 3, 5

    assert a * x + a * y + b * x + b * y == (a + b) * (x + y) # 2 + 2
    assert x**2 - y**2 + 2 * y - 1 == (x + y - 1) * (x - y + 1) # 3 + 1
