from math import factorial # for tests

class BinomialCoefficients:
    def __init__(self, n=10):
        self.coefficients = []
        self.initialize(n)

    def initialize(self, n):
        start = len(self.coefficients)
        for i in range(start, n + 1):
            cur_row = [1 for j in range(i + 1)]
            for j in range(1, i):
                cur_row[j] = self.coefficients[i - 1][j - 1] + self.coefficients[i - 1][j]
            self.coefficients.append(cur_row)

    def choose_n_k(self, n, k):
        if len(self.coefficients) < n + 1:
            self.initialize(n)
        return self.coefficients[n][k]

def choose_n_k_factorial(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)

def test_binomial_coefficients():
    myBinomialCoefficients = BinomialCoefficients()
    assert myBinomialCoefficients.choose_n_k(20, 6) == choose_n_k_factorial(20, 6)
    assert myBinomialCoefficients.choose_n_k(90, 42) == choose_n_k_factorial(90, 42)
    assert myBinomialCoefficients.choose_n_k(500, 189) == choose_n_k_factorial(500, 189)

if __name__ == "__main__":
    test_binomial_coefficients()
