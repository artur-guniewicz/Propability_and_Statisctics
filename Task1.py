#############################################################################
#                                                                           #
#                       Artur Guniewicz - Zadanie 1                         #
#                                                                           #
#############################################################################


import math
import random

moj_N = 10.0


def shot(n):
    hits = 0
    for i in range(1, n): # przedział (1,n) przechodzony po kolei
        # dwie liczby pseudoloswe, które opisują miejsce trafienia w tarczę
        x = random.random()
        y = random.random()
        distance = math.sqrt((x * x) + (y * y))
        if (distance < 1):  # czy odległość trafienia od rogu tarczy jest < 1; hit - ilość trafień w ćwiartkę koła
            hits = hits + 1
    pi = 4 * (hits / n)
    return pi


print("Liczba pi dla N = 10   : {}".format(shot(10)))
print("Liczba pi dla N = 10^2 : {}".format(shot(100)))
print("Liczba pi dla N = 10^3 : {}".format(shot(1000)))
print("Liczba pi dla N = 10^5 : {}".format(shot(100000)))
print("Liczba pi dla N = 10^6 : {}".format(shot(1000000)))
