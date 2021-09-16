import Lagrange as Lg
import Splines as Sp
import LeastSquares as LS
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 200)
fx = []
for i in range(len(x)):
    fx.append(abs(Lg.polynomial(x[i]) - np.sin(x[i])))
plt.plot(x, fx)
plt.grid()
plt.axhline()
plt.axvline()
plt.show()

x = np.linspace(-np.pi, np.pi, 200)
f = []
for i in range(len(x)):
    f.append(abs(Sp.splines(x[i]) - np.sin(x[i])))
plt.plot(x, f)
plt.grid()
plt.axhline()
plt.axvline()
plt.show()

x = np.linspace(-np.pi, np.pi, 200)
fy = []
for i in range(len(x)):
    fy.append(abs(LS.L_Squares(x[i]) - np.sin(x[i])))
plt.plot(x, fy)
plt.grid()
plt.axhline()
plt.axvline()
plt.show()
