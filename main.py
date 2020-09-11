# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import argparse

from lagrange import get_lagrange_poly_func
from newton import get_newton_poly_func


def get_data(data_path):
    with open(data_path, "r", encoding="utf-8") as f:
        data = np.array([[eval(t) for t in line.split()] for line in f.read().strip().split("\n")])
    return data[:, 0], data[:, 1]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', type=str, default='lagrange', choices=["lagrange", "newton"],
                        help='Interpolation method.')
    parser.add_argument('--data_path', type=str, default='', required=True,
                        help='Path to the data.')
    parser.add_argument('--output_path', type=str, default='',
                        help='Path to the output.')
    parser.add_argument('--not_show', action='store_true', default=False,
                        help="Whether not to show predictions.")
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    x_data, y_data = get_data(args.data_path)
    plt.plot(x_data, y_data, "r*")
    if args.method == 'lagrange':
        poly_func = get_lagrange_poly_func(x_data, y_data)
    elif args.method == 'newton':
        poly_func = get_newton_poly_func(x_data, y_data)
    else:
        poly_func = get_lagrange_poly_func(x_data, y_data)
    Xs = np.arange(-10, 10, 0.1)
    Ys = poly_func(Xs)
    plt.plot(Xs, Ys, "b")
    plt.show()
