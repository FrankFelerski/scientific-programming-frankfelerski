__author__ = 'Frank Felerski'

import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format="", fit_format=""):
    """
    :param data:ndarray, shape(2, M)
    x-y data that was fit. M is the number of data points.
    :param fit_curve: ndarray, shape(2, N)
    x-y data created by the coeffecients of the fit function. N is the number of function evaluation points (usually much greater than M).
    :param data_format: str, optional
    Optional formatting specification for the style of the scatter plot data points.
    :param fit_format:str, optional
    Optional formatting specification for the curve of the fit function.
    :return:combined_plot
    A list of Line2D objects representing the plotted data.
    """
    scatter_plot = plt.plot(data[0, :], data[1, :], data_format)
    curve_plot = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)
    plt.title(r'Fm-3m Equation of State for Al in DFT GGA-PBE', y=1.05)
    plt.xlabel(r'$V$ $A^3/atom$')
    plt.ylabel(r'$E$ $eV/atom$')

    plt.xlim([90, 137])

    plt.show()

    return scatter_plot, curve_plot