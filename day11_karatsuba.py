def karatsuba(x, y):
    if len(x) == 1 and len(y) == 1:
        return str(int(x) * int(y))
    max_len = max(len(x), len(y))
    part_size = (max_len + 1)  >> 1
    x1, x2 = partition(x, part_size)
    y1, y2 = partition(y, part_size)
    a = karatsuba(x1, y1)
    b = karatsuba(x2, y2)
    c = karatsuba(add(x1, x2), add(y1, y2))
    c = sub(c, add(a, b))
    res = add((a + "0" * (part_size << 1)), (c + "0" * part_size))
    res = add(res, b)
    return res

def partition(x, part_size):
    if len(x) <= part_size:
        x1 = "0"
        x2 = x
    else:
        x1 = x[:-part_size]
        x2 = x[-part_size:]
    return x1, x2

def add(x, y):
    # quick hack to add two strings as numbers
    return str(int(x) + int(y))

def sub(x, y):
    return str(int(x) - int(y))

def test_karatsuba():
    assert karatsuba("12", "12") == "144"
    assert karatsuba("1575923514", "53") == "83523946242"
    assert karatsuba("42", "0") == "0"
    assert karatsuba("1", "1") == "1"
    assert karatsuba("5780321345", "1575923514") == "9109344326061606330"
