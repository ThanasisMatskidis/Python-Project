import numpy as np

# Πίνακας με τις τιμές του x (ημερομηνίες)
Xi = np.array([15, 16, 17, 18, 21, 22, 23, 24, 25, 29])


# Επιλογή κατάλληλου πίνακα με τις τιμές κλεισίματος με βάση την εταιρία
def selection(i):
    if i == 1:
        fxi = np.array([18.24, 18.00, 18.24, 18.52, 18.60, 18.80, 18.80, 18.60, 18.78, 18.84])
    elif i == 2:
        fxi = np.array([0.6500, 0.6400, 0.6380, 0.6330, 0.6400, 0.6350, 0.6400, 0.6320, 0.6350, 0.6850])
    return fxi


# Συνάρτηση που δημηουργεί πίνακα με τους συντελεστές των αγνώστων
def A():
    a = np.ones((10, 4))
    for i in range(0, 10):
        a[i, 1] = Xi[i]
        a[i, 2] = Xi[i] ** 2
        a[i, 3] = Xi[i] ** 3
    return a


# Συνάρτηση που υπολογίζει τον πίνακα ΑΤ
def AT():
    a = A()
    A_T = np.ones((4, 10))
    for i in range(0, 10):
        for j in range(1, 4):
            A_T[j, i] = a[i, j]
    return A_T


# Συνάρτηση που υπολογίζει τον πίνακα ΑΤ*Τ
def ATA():
    return np.dot(AT(), A())


# Συνάρτηση που υπολογίζει τον πίνακα ΑΤ*fx (όπου fx ο πίνακας με τις τιμές της f(x))
def C(i):
    fx = selection(i)
    return np.dot(AT(), fx)


# Συνάρτηση που υπολογίζει το πολυώνυμο 3ου βαθμού με τη μέθοδο ελαχίστων τετραγώνων
def Third_Degree_Polynomial(i, x):
    sol = np.linalg.solve(ATA(), C(i))
    y = float(sol[0] + sol[1] * x + sol[2] * x ** 2 + sol[3] * x ** 3)
    return y
