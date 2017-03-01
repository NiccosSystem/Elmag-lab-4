import numpy as np
import math

def linear_regression(x, y):
    #Hjelpestørrelser
    N = len(x)
    Sx = np.sum(x)
    Sy = np.sum(y)
    Sxx = np.sum(np.square(x))
    Sxy = np.sum(np.multiply(x, y))
    delta = N*Sxx-Sx**2

    #Regne ut a0 og a1 og printe verdiene til skjerm
    a0 = (Sy*Sxx-Sx*Sxy)/delta
    a1 = (N*Sxy-Sx*Sy)/delta
    print("a0 = {0}".format(a0))
    print("a1 = {0}".format(a1))

    regfunksjon = a0 + a1 * x
    Dy = np.subtract(y, regfunksjon)
    S = np.sum(np.square(Dy))
    Da0 = math.sqrt((S*Sxx)/((N-2)*delta))
    Da1 = math.sqrt((N*S)/((N-2)*delta))
    print("Da0 = {0}".format(Da0))
    print("Da1 = {0}".format(Da1))

    return a0,a1