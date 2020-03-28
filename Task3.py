#############################################################################
#                                                                           #
#                       Artur Guniewicz - Zadanie 3                         #
#                                                                           #
#############################################################################


import matplotlib.pyplot as plt
import numpy as np
import math
import random

tab = []
k = 16
lamb = 4


def poisson(i):
    return (math.pow(lamb, i) * math.exp(-lamb)) / math.factorial(i)


def expected_distribution(k):
    for i in range(0, k):
        tab.append(poisson(i))


# http://www.math.uni.wroc.pl/~dbura/teaching/rozwiazania/z6/symulacje.pdf
def generator():
    U = random.random()
    i = 0
    p = math.exp(-lamb)
    F = p

    while U >= F:
        p = (lamb * p) / (i + 1)
        F = F + p
        i = i + 1

    return i


expected_distribution(k)  # wyliczany ze wzoru

tab2 = []
N = 1000000

for i in range(0, N):
    tab2.append(generator())

fig, axs = plt.subplots(2)
axs[0].plot(tab, 'ro')
axs[1].hist(tab2, density=1, bins=18)
plt.axis([0, 15, 0, 0.2])
plt.suptitle("PORÓWNANIE")
plt.show()
