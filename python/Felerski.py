# Goal is to take in data, find a line of best fit from up to 3 models, and plot it
# Import required packages
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
# Begin by establishing empty lists for the points
x = []
y = []
n = 0
# Get critical value for number of points to be used in calculation
numberofpoints = int((input('How many data points? ')))
# Append previously empty lists with data points to be used
while n < numberofpoints:
    x.append(float(input('Input point x value: ')))
    y.append(float(input('Input point y value: ')))
    n = n + 1
# Reset n just in case after loop for point input concludes
n = 0
# Print values to show process functions as intended
print('X values: ')
print(x)
print('Y values: ')
print(y)
# Plot, hopefully
plt.scatter(x, y)
# With custom user specified labels
xlabel = input('X label? ')
plt.xlabel = xlabel
ylabel = input('Y label? ')
plt.ylabel = ylabel
title = input('Graph title? ')
plt.title = title
plt.show()
# Graph should show up w points plotted on it
# Next step is the hard bit:
# getting the program to figure out the rate of change of the data and use it to create a line of best fit
# Starting by defining simple variables
deltax = 0
deltay = 0
slopes = []
pointsminusone = numberofpoints - 1
slopeindex = []
# for list purposes
while n < pointsminusone:
    deltax = x[n+1]-x[n]
    deltay = y[n+1]-y[n]
    tempslope = deltay/deltax
    slopes.append(tempslope)
    slopeindex.append(n)
    n += 1
# Once again, to please the machine spirit
n = 0
print('Slopes:')
print(slopes)
m, b = np.polyfit(slopeindex, slopes, 1)
g = sp.Symbol('X')
print(m)
print(b)
lineofbestfit = sp.integrate(m*g+b, g)
lineofbestfit = str(lineofbestfit)
print(lineofbestfit)
print(type(lineofbestfit))
plotfit = []
# Calculate points from projected line of best fit
for n in x:
    midpoint = lineofbestfit.replace('X', str(n))
    print(midpoint)
    midpoint = eval(midpoint)
    print(midpoint)
    plotfit.append(midpoint)
print('Projected points.')
print(plotfit)
plt.plot(plotfit, x, linestyle='solid')
plt.xlabel = xlabel
plt.ylabel = ylabel
plt.title = title
plt.show()
