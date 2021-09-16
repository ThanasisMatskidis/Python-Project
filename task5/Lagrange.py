import numpy as np

arr = np.array(
    [-np.pi, -np.pi / 2, -np.pi / 3, -np.pi / 4, -np.pi / 6, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2, np.pi])


def Li(i, x):
    par = 1
    ar = 1
    for j in range(0, 10):
        if j != i:
            par *= (arr[i] - arr[j])
            ar *= (x - arr[j])
    return ar / par


def polynomial(x):
    snx = 0

    for i in range(0, 10):
        snx += np.sin(x) * Li(i, x)
    return snx
