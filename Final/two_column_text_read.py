__author__ = 'Frank Felerski'
import numpy as np


def two_column_text_read(filename):
    """
    :param filename:str
    ,Name of file to be read in.
    :return:data: ndarray, shape (2, M)
    x-y data read in from file. M is the number of data points.
    """
    try:
        data = np.loadtxt(filename)
    except OSError:
        print(f'{filename} cannot be found!!')

    return data.transpose()


if __name__ == '__main__':
    data_file = 'volumes_energies.dat'
    volumes_energies = two_column_text_read(data_file)
    print(volumes_energies)