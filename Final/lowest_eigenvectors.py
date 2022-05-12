__author__ = 'Frank Felerski'
import numpy as np


def lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    """
    :param square_matrix: ndarray, shape(M, M)
    Matrix to be characterized. Must be a square matrix of M rows and M columns where M is >=1.
    :param number_of_eigenvectors: int, optional
    Number of eigenvectors K with eigenvalues to return.  Default is 3.
    :return:
    """
    m, n = square_matrix.shape
    if m != n:
        raise IndexError('not square')
    values, vectors = np.linalg.eig(square_matrix)
    values_sorted = np.sort(values)
    vector_sorted = vectors[:, values.argsort()]
    return values_sorted[:number_of_eigenvectors], vector_sorted.transpose()[:number_of_eigenvectors]