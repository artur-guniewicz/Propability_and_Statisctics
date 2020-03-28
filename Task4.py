#############################################################################
#                                                                           #
#                       Artur Guniewicz - Zadanie 4                         #
#                                                                           #
#############################################################################


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import random


def BoxMullerTranform():  # transforamcja Box-Muller'a
    u1 = random.random()
    u2 = random.random()
    return np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)


def generator(n):
    out = np.empty(n)
    for i in range(n):
        out[i] = BoxMullerTranform()
    return out


def randomPoints(n, size):
    tab = np.empty(size)
    for i in range(size):
        t = generator(n)
        tab[i] = np.dot(t, t)
    return tab


N = 10000
n = 3
tab = randomPoints(n, N)

space = np.linspace(0, 20, 100)  # 100 próbek między 0 a 20
plt.figure(dpi=150, clear=True)
plt.hist(tab, 150, density=1, facecolor='g')
plt.plot(space, chi2.pdf(space, df=n))  # pdf = probability density function (funkcja gęstości prawdopodobieństwa)
plt.show()
