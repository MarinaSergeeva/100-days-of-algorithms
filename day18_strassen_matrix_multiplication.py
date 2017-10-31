import numpy as np
import math

def strassen_multiply_wrapper(x, y):
    if x.shape[1] != y.shape[0]:
        raise ValueError("martices sshapes do not match")
    shapes = x.shape + y.shape
    max_dim = max(shapes)
    if max_dim == min(shapes) and is_power_of_2(max_dim):
        # square matrices of the right size => no need for padding
        return strassen_multiply(x, y)
    else:
        # do padding to make matrices square and of the right size
        next_power = int(get_next_power_of_2(max_dim))
        padding_size = [next_power - el for el in shapes]
        x = np.pad(x, ((0, padding_size[0]), (0, padding_size[1])), "constant", constant_values=(0))
        y = np.pad(y, ((0, padding_size[2]), (0, padding_size[3])), "constant", constant_values=(0))
        result = strassen_multiply(x, y)
        # trimming extra zeros
        return result[:shapes[0], :shapes[3]]

def is_power_of_2(x):
    return x > 0 and x & (x - 1) == 0

def get_next_power_of_2(x):
    return math.pow(2, math.ceil(math.log2(x)))

def strassen_multiply(x, y):
    # x, y - square numpy 2d arrays
    if x.shape == (1, 1):
        return np.array(x[0, 0] * y[0, 0])
    else:
        med = (x.shape[0] + 1) // 2
        a, b, c, d = partition_matrix(x, med)
        e, f, g, h = partition_matrix(y, med)
        p1 = strassen_multiply(a, f - h)
        p2 = strassen_multiply(a + b, h)
        p3 = strassen_multiply(c + d, e)
        p4 = strassen_multiply(d, g - e)
        p5 = strassen_multiply(a + d, e + h)
        p6 = strassen_multiply(b - d, g + h)
        p7 = strassen_multiply(a - c, e + f)
        z11 = p5 + p4  - p2 + p6
        z12 = p1 + p2
        z21 = p3 + p4
        z22 = p1 + p5 - p3 - p7
        z1 = np.hstack((z11, z12))
        z2 = np.hstack((z21, z22))
        return np.vstack((z1, z2))

def partition_matrix(x, med):
    a = x[:med, :med]
    b = x[:med, med:]
    c = x[med:, :med]
    d = x[med:, med:]
    return a, b, c, d

def test_is_power_of_2():
    assert is_power_of_2(2) == True
    assert is_power_of_2(256) == True
    assert is_power_of_2(9) == False

def test_get_next_power_of_2():
    assert get_next_power_of_2(2) == 2
    assert get_next_power_of_2(9) == 16

def test_strassen_multiply():
    a = np.ones((4, 4))
    b = np.ones((4, 4))
    assert np.array_equal(strassen_multiply_wrapper(a, b), np.matmul(a, b))
    a1 = np.array([[1, 2], [3, 4]])
    b1 = np.array([[5, 4], [1, 2]])
    assert np.allclose(strassen_multiply_wrapper(a1, b1), np.matmul(a1, b1))
    a2 = np.random.rand(4, 4)
    b2 = np.random.rand(4, 4)
    assert np.allclose(strassen_multiply_wrapper(a2, b2), np.matmul(a2, b2))
    a3 = np.random.rand(32, 32)
    b3 = np.random.rand(32, 32)
    assert np.allclose(strassen_multiply_wrapper(a3, b3), np.matmul(a3, b3))
    a4 = np.random.rand(7, 7)
    b4 = np.random.rand(7, 7)
    assert np.allclose(strassen_multiply_wrapper(a4, b4), np.matmul(a4, b4))
    a5 = np.random.rand(17, 21)
    b5 = np.random.rand(21, 7)
    assert np.allclose(strassen_multiply_wrapper(a5, b5), np.matmul(a5, b5))

if __name__ == "__main__":
    test_strassen_multiply()
