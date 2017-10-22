def get_greatest_common_divisor(a, b):
    # for simplicity make a > b
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    remainder = a % b
    return get_greatest_common_divisor(b, remainder)

def get_least_common_multiple(a, b):
    # gdc(a, b) * lcm(a, b) = a, b
    gcd = get_greatest_common_divisor(a, b)
    return a * b // gcd

def test_greatest_common_divisor():
    assert get_greatest_common_divisor(0, 5) == 5
    assert get_greatest_common_divisor(34, 55) == 1
    assert get_greatest_common_divisor(144, 60) == 12

def test_least_common_multiple():
    assert get_least_common_multiple(5, 0) == 0
    assert get_least_common_multiple(30, 16) == 240
    assert get_least_common_multiple(34, 55) == 1870
