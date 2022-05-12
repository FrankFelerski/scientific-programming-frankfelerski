__author__ = 'Frank Felerski'
import numpy as np


def quadratic_fit(data):
    """
    :param data:ndarray, shape (2, M)
    x-y data to be fit. M is the number of data points.
    :return:quadratic_coefficients: ndarray, shape (3,)
    Quadratic polynomial coefficients, ordered quadratic term first, then linear term, and constant term last.
    """
    x = data[0]
    y = data[1]
    quadratic_coefficients = np.polyfit(x, y, 2)

    return quadratic_coefficients


if __name__ == '__main__':
    data = np.array([[2, 7], [0, 1], [-1, 1]]).transpose()
    coefficients = quadratic_fit(data)
    print(coefficients)