# coding: utf-8

import numpy as np


def get_newton_poly_func(x_data, y_data):
    n = len(x_data)
    assert n == len(y_data)
    A = y_data.copy()
    for i in range(1, n):
        A[i:] = (A[i:] - A[i - 1]) / (x_data[i:] - x_data[i - 1])
    print(A)

    def poly(x):
        x = np.array(x, dtype=float)
        res = np.full(x.shape, A[-1])
        for i in range(n - 2, -1, -1):
            res *= (x - x_data[i])
            res += A[i]
        return res

    return poly
