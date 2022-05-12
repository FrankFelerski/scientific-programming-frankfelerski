from two_column_text_read import two_column_text_read
from bivariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
from convert_units import convert_units
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from numpy import linspace
import matplotlib.pyplot as plt

display_graph = True


def parse_file_name(file_name):
    x = file_name.split(".")
    chemical_symbol = x[0]
    crystal_symmetry = x[1]
    density_functional_exchange = x[2]
    return chemical_symbol, crystal_symmetry, density_functional_exchange


file_name = "Al.Fm-3m.GGA-PBE.volumes_energies.dat"
chemical_symbol, crystal_symmetry, density_functional_exchange = parse_file_name(file_name)
array = two_column_text_read("Al.Fm-3m.GGA-PBE.volumes_energies.dat")
statistics = bivariate_statistics(array)
quadratic_coefficients = quadratic_fit(array)

min_x = statistics[2]
max_x = statistics[3]

undo_array = zip(*array)
array_2 = list(undo_array)

fit_eos_curve, fit_parameters = fit_eos(array[0], array[1], quadratic_coefficients, eos='Murnaghan',
                                        number_of_points=50)
bulk_modulus = fit_parameters[1]
equilibrium_volume = fit_parameters[3]


def annotate_graph(chemical_symbol, crystal_symmetry):
    ax.annotate(chemical_symbol, xy=(0, 0))

    ax.annotate(r'$ {}\overline{{{}}} {}$'.format(crystal_symmetry[0:2],
                                                  crystal_symmetry[3],
                                                  crystal_symmetry[1]),
                xy=(0, -200))

    ax.annotate('K_0={:.6f}GPa'.format(bulk_modulus_gpa),
                xy=(0, -400))

    ax.annotate('V_0={:.3f}A^3/atom'.format(eq_vol),
                xy=(0, -300))
    plt.axvline(eq_vol - array_2[0][array_2[1].index(min(array_2[1]))] * 0.01, color="black",
                linestyle='--')

    plt.text(0, -100, "created by Frank Felerski 2022/05/12")
    plt.title("{} Equation of State for {} in DFT {}".format('Murnaghan', chemical_symbol, density_functional_exchange))
    return ax, plt


fig = plt.figure()
ax = fig.add_subplot(111)

volumes = linspace(min(array_2[0]), max(array_2[0]), len(fit_eos_curve))
line1, = ax.plot(array_2[0], array_2[1], 'o')
line2, = ax.plot(volumes, fit_eos_curve, color="black")

x_min = 10
x_max = 20
y_min = -537
y_max = 540

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel(r'$V$ (Å$^3$/atom)')
plt.ylabel(r'$E$ (eV/atom)')
bulk_modulus_gpa = convert_units(bulk_modulus, "rb/cb")
eq_vol = array_2[0][array_2[1].index(min(array_2[1]))]
annotate_graph(chemical_symbol, crystal_symmetry)

fit_curve = fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100)
scatter_plot, curve_plot = plot_data_with_fit(array, fit_curve, data_format="bo", fit_format="k")

if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("Felerski.Al.Fm-3m.GGA-PBE.MurnaghanEquationOfState.png")

from generate_matrix import generate_matrix
from lowest_eigenvectors import lowest_eigenvectors
from numpy import linspace
import matplotlib.pyplot as plt

display_graph = False
potential_name = 'harmonic'
N_dim = 120
potential_parameter = 100

matrix = generate_matrix(-10, 10, N_dim, potential_name, potential_parameter)

eigenvalues, eigenvectors = lowest_eigenvectors(matrix, 3)

x = linspace(-10, 10, N_dim)
line1, = plt.plot(x, eigenvectors[0][0:N_dim])
line2, = plt.plot(x, eigenvectors[1][0:N_dim])
line3, = plt.plot(x, eigenvectors[2][0:N_dim])

plt.xlabel("x [a.u.]")
plt.ylabel("ψ n ( x ) [a.u.]")
plt.legend((line1, line2, line3), ('ψ1, Ε1 = 0.62414396 a.u.', 'ψ2, Ε2 = 0.87335307 a.u.', 'ψ3, Ε3 = 1.12229893 a.u.'))
plt.axis([-10, 10, max(eigenvectors[0]) - 2, max(eigenvectors[0]) + 2])
plt.axhline(color="black")
plt.text(-9.5, -1.75, "Created by Frank Felerski 2022/05/12")
plt.title("Select Wavefunctions for a Harmonic Potential on a Spatial Grid of 0, 1, 2 Points")

if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("Felerski.harmonic.Eigenvector0, 1, 2.png")
