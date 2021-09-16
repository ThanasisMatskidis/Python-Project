import numpy as np

arr = np.array(
    [-np.pi, -np.pi / 2, -np.pi / 3, -np.pi / 4, -np.pi / 6, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2, np.pi])


def space(x):
    for i in range(0, 10):
        if arr[i] <= x <= arr[i + 1]:
            break
    return i


def splines(x):
    i = space(x)
    y = np.sin(arr[i]) + ((np.sin(arr[i + 1]) - np.sin(arr[i])) / (arr[i + 1] - arr[i])) * (x - arr[i])
    return y
