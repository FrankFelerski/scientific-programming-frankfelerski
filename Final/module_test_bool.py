import numpy as np

from two_column_text_read import two_column_text_read
from bivariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
import matplotlib.pyplot as plt
from lowest_eigenvectors import lowest_eigenvectors

if __name__ == '__main__':
    filename = 'volumes_energies.dat'
    data = two_column_text_read(filename)
    print(data[0])
    statistics = bivariate_statistics(data)
    print(statistics)
    coefficients = quadratic_fit(data)
    print(coefficients)
    fit = fit_curve_array(coefficients, statistics[2], statistics[3])
    plot = plot_data_with_fit(data, fit)
    plt.show()
    matrix = np.array([[4, 0, 0, 0], [0, 3, 0, 0], [0, 0, 2, 0], [0, 0, 0, 1]])
    values, vectors = lowest_eigenvectors(matrix, number_of_eigenvectors=2)
    print(values)
    print(vectors)