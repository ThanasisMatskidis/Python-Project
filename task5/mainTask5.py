import Lagrange as Lg
import Splines as Sp
import LeastSquares as LS
import show
import numpy as np

a = -1.5
print("Lagrange Method: ")
print(Lg.polynomial(a))
print("\n")
print("Splines Method: ")
print(Sp.splines(a))
print("\n")
print("Least Squares Method: ")
print(LS.L_Squares(a))