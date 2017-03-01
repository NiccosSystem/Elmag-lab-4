import numpy as np
from matplotlib import pyplot as plt
from regression import linear_regression

#Åpne og lese verdiene inn i matrise
datafile = open('../data/data.dat', 'r')
datamatrise = [[], []]
for line in datafile:
    xandy = line.strip().split(" "*7)
    datamatrise[0].append(float(xandy[0]))
    datamatrise[1].append(float(xandy[1]))

#Legge verdiene inn i numpy-arrays
x_values = np.array(datamatrise[0])
y_values = np.array(datamatrise[1])

#Plott målepunktene
plt.figure(1)
plt.plot(x_values, y_values, '.', label="Målepunkter", color='black')


a0,a1 = linear_regression(x_values, y_values)

#Plotte regresjonsverdiene
regfunksjon = a0 + a1*x_values
plt.plot(x_values, regfunksjon, '-', color='0.6', label="Regresjonsverdier")
plt.ylabel(r"$y$")
plt.xlabel(r"$x$")
plt.title("Kurvetilpasning")
plt.legend(loc="upper left")

#Regn ut avviket
Dy = np.subtract(y_values, regfunksjon)

#Plotte avvik
plt.figure(2)
plt.plot([0,2*max(x_values)], [0, 0], '-', color='0')
plt.plot(x_values, Dy, '.', color='0', label=r"$D_y$")
plt.xlim([min(x_values), max(x_values)+1])
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend()

#Vis figurene
plt.show()


