import numpy as np

x = np.linspace(0, np.pi / 2, 11)
fx = []
for i in range(len(x)):
    fx.append(np.sin(x[i]))

number_of_subspaces = len(x) - 1


def sumfx():
    sum1 = 0
    for j in range(1, len(x) - 1):
        sum1 += fx[j]
    return 2 * sum1


def trapezoid():
    return (((np.pi / 2) - 0) / (2 * number_of_subspaces)) * (fx[0] + fx[10] + sumfx())
