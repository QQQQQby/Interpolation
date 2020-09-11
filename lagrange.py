# coding: utf-8

import numpy as np


def get_lagrange_poly_func(x_data, y_data):
    n = len(x_data)
    assert n == len(y_data)

    def poly(x):
        x = np.array(x, dtype=float)
        res = np.zeros_like(x)
        for i in range(n):
            res += y_data[i] * get_cardinal_func(x_data, i)(x)
        return res

    return poly


def get_cardinal_func(x_data, i):
    def cardinal(x):
        res = np.ones_like(x)
        for j in range(i):
            res *= (x - x_data[j]) / (x_data[i] - x_data[j])
        for j in range(i + 1, len(x_data)):
            res *= (x - x_data[j]) / (x_data[i] - x_data[j])
        return res

    return cardinal
