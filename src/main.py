import numpy as np
from matplotlib import pyplot as plt
import math

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

#Debug-kode
#print(type(x_values), x_values)
#print(type(y_values), y_values)

#Plott målepunktene
plt.figure(1)
plt.plot(x_values, y_values, '.', label="Målepunkter", color='black')

#Hjelpestørrelser
N = len(x_values)
Sx = np.sum(x_values)
Sy = np.sum(y_values)
Sxx = np.sum(np.square(x_values))
Sxy = np.sum(np.multiply(x_values, y_values))
delta = N*Sxx-Sx**2

#Regne ut a0 og a1 og printe verdiene til skjerm
a0 = (Sy*Sxx-Sx*Sxy)/delta
a1 = (N*Sxy-Sx*Sy)/delta
print("a0 = {0}".format(a0))
print("a1 = {0}".format(a1))

#Plotte regresjonsverdiene
regfunksjon = a0 + a1*x_values
plt.plot(x_values, regfunksjon, '-', color='0.6', label="Regresjonsverdier")

plt.ylabel(r"$y$")
plt.xlabel(r"$x$")
plt.title("Kurvetilpasning")
plt.legend(loc="upper left")


Dy = np.subtract(y_values, regfunksjon)
S = np.sum(np.square(Dy))
Da0 = math.sqrt((S*Sxx)/((N-2)*delta))
Da1 = math.sqrt((N*S)/((N-2)*delta))
print("Da0 = {0}".format(Da0))
print("Da1 = {0}".format(Da1))

#Plotte avvik
plt.figure(2)
plt.plot(x_values, Dy, '.', color='0', label=r"$D_y$")
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend()
plt.show()


