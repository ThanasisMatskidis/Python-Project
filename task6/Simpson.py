import numpy as np

x = np.linspace(0, np.pi / 2, 11)
fx = []
for i in range(len(x)):
    fx.append(np.sin(x[i]))

number_of_subspaces = len(x) - 1


def sum_1_fx():
    sum1 = 0
    for j in range(1, int(number_of_subspaces / 2)):
        sum1 += fx[2 * j]
    return 2 * sum1


def sum_2_fx():
    sum2 = 0
    for j in range(1, int(number_of_subspaces / 2) + 1):
        sum2 += fx[2 * j - 1]
    return 4 * sum2


def simpson():
    return (((np.pi / 2) - 0) / (3 * number_of_subspaces)) * (fx[0] + fx[10] + sum_1_fx() + sum_2_fx())
