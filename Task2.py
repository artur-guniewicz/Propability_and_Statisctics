#############################################################################
#                                                                           #
#                       Artur Guniewicz - Zadanie 2                         #
#                                                                           #
#############################################################################


import matplotlib.pyplot as plt  # do tworzenia wykresów
import numpy as np
import math
import random

x = [-1, 0, 1, 2, 3]
y = [0, 1 / 3, 1 / 3, 1 / 3, 0]


def shot(n):
    for i in range(1, n):
        x = random.random()

        # odwrotność dystrybuanty (z wykładu)
        if x < 1 / 6:
            x = math.sqrt(6 * x) - 1
        elif 1 / 6 <= x < 5 / 6:
            x = 3 * x - 1 / 2
        else:
            x = 3 - math.sqrt(6 - 6 * x)

        tab.append(x)  # dodaje x do tablicy tab


tab = []
shot(100000)

fig, axs = plt.subplots(2)
axs[0].plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle('PORÓWNANIE')
axs[1].hist(tab, density=1, facecolor='g', bins=60)
plt.show()
