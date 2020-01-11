import numpy as np

arr = np.array(
    [-np.pi, -np.pi / 2, -np.pi / 3, -np.pi / 4, -np.pi / 6, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2, np.pi])


def A():
    a = np.ones((10, 2))
    for i in range(0, 10):
        a[i, 0] = arr[i]
    return a


def B():
    b = np.zeros((10, 1))
    for i in range(0, 10):
        b[i] = np.sin(arr[i])
    return b


def AT():
    a = A()
    A_T = np.ones((2, 10))
    for i in range(0, 10):
        A_T[0, i] = a[i, 0]
    return A_T


def ATA():
    return np.dot(AT(), A())


def C():
    return np.dot(AT(), B())


def L_Squares(x):
    sol = np.linalg.solve(ATA(), C())
    y = float(sol[0] * x + sol[1])
    return y
