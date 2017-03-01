import numpy as np
from matplotlib import pyplot as plt
from regression import linear_regression
import math

#Åpne og lese verdiene inn i matrise
datafile = open('../data/sinus.dat', 'r')
datamatrise = [[], []]
for line in datafile:
    xandy = line.strip().split("\t")
    datamatrise[0].append(float(xandy[0]))
    datamatrise[1].append(float(xandy[1]))

#Legge verdiene inn i numpy-arrays
theta = np.array(datamatrise[0])
y_values = np.array(datamatrise[1])
sintheta = np.sin(theta)


#Plott målepunktene både s.f.a. theta og sintheta
plt.figure(1)
plt.plot(theta, y_values, '.', label=r"Målinger s.f.a. $\theta$", color='0')
plt.ylabel(r"$y$")
plt.xlabel(r"$\theta$")
plt.title(r"Kurvetilpasning, som funksjon av $\theta$")

plt.figure(2)
plt.plot(sintheta, y_values, '.', label=r"Målinger s.f.a. $\sin \theta$", color='0')
plt.ylabel(r"$y$")
plt.xlabel(r"$\sin \theta$")

#Finn a0 og a1 ved hjelp av regression.py
a0,a1 = linear_regression(sintheta, y_values)

#Plotte regresjonsverdiene s.f.a. sin theta
plt.figure(2)
regfunksjon = a0 + a1 * sintheta
plt.plot(sintheta, regfunksjon, '-', color='0.6', label=r"$y(\sin \theta)$")
plt.title(r"Kurvetilpasning, som funksjon av $\sin \theta$")
plt.legend(loc=2)

#Plotte regresjonsverdiene s.f.a. theta
plt.figure(1)
x_smooth = np.linspace(min(theta), max(theta), 300)
verdier = np.multiply(x_smooth, a1)
verdier = np.sin(verdier)
verdier = np.add(verdier, a0)
plt.plot(x_smooth, verdier, '-', color='0', label=r"$y(\theta)$")
plt.legend(loc=2)

#Vis figurene
plt.show()


