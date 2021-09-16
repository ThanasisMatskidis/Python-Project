import SecondDegree as SD
import ThirdDegree as TD
import FourthDegree as FD
import numpy as np

# ΑΣΚΗΣΗ 7
print("\n")
print("TASK 7")

# Πίνακας με τις τιμές του x (ημερομηνίες)
X = np.array([15, 16, 17, 18, 21, 22, 23, 24, 25, 29])

x = 31

# Ημέρα γενεθλίων
print("\n")
print("BIRTHDAY: 30 / 10")

# Πρόβλεψη για την ημέρα μετά τα γενέθλια
# Πολυώνυμο 2ου βαθμού
print("\n")
print("DATE: 31 / 10")
print("SECOND DEGREE POLYNOMIAL (a + b * x + c * x^2 = y): ")

print("First company: ")
print(SD.Second_Degree_Polynomial(1, x))

print("Second company: ")
print(SD.Second_Degree_Polynomial(2, x))

# Πολυώνυμο 3ου βαθμού
print("\n")
print("THIRD DEGREE POLYNOMIAL (a + b * x + c * x^2 + d * x^3 = y): ")

print("First company: ")
print(TD.Third_Degree_Polynomial(1, x))

print("Second company: ")
print(TD.Third_Degree_Polynomial(2, x))

# Πολυώνυμο 4ου βαθμού
print("\n")
print("FOURTH DEGREE POLYNOMIAL (a + b * x + c * x^2 + d * x^3 + e * x^4 = y): ")

print("First company: ")
print(FD.Fourth_Degree_Polynomial(1, x))

print("Second company: ")
print(FD.Fourth_Degree_Polynomial(2, x))

x = 4

# Πρόβλεψη για την πέμπτη ημέρα μετά τα γενέθλια
# Πολύωνυμο 2ου βαθμού
print("\n")
print("DATE: 04 / 11")
print("SECOND DEGREE POLYNOMIAL (a + b * x + c * x^2 = y): ")

print("First company: ")
print(SD.Second_Degree_Polynomial(1, x))

print("Second company: ")
print(SD.Second_Degree_Polynomial(2, x))

# Πολυώνυμο 3ου βαθμού
print("\n")
print("THIRD DEGREE POLYNOMIAL (a + b * x + c * x^2 + d * x^3 = y): ")

print("First company: ")
print(TD.Third_Degree_Polynomial(1, x))

print("Second company: ")
print(TD.Third_Degree_Polynomial(2, x))

# Πολυώνυμο 4ου βαθμού
print("\n")
print("FOURTH DEGREE POLYNOMIAL (a + b * x + c * x^2 + d * x^3 + e * x^4 = y): ")

print("First company: ")
print(FD.Fourth_Degree_Polynomial(1, x))

print("Second company: ")
print(FD.Fourth_Degree_Polynomial(2, x))

# ΣΥΓΡΙΣΗ ΤΙΜΩΝ
print("\n")
# Για τις διαθέσιμες τιμές
# 1ης εταιρίας
print("FIRST COMPANY: ")
fx = SD.selection(1)
for i in range(0, 10):
    print("DATE: ", X[i], " / 10")
    print("SECOND DEGREE (error): ")
    print(abs(SD.Second_Degree_Polynomial(1, X[i]) - fx[i]))
    print("THIRD DEGREE (error): ")
    print(abs(TD.Third_Degree_Polynomial(1, X[i]) - fx[i]))
    print("FOURTH DEGREE (error): ")
    print(abs(FD.Fourth_Degree_Polynomial(1, X[i]) - fx[i]))
    print("\n")

# 2ης εταιρίας
print("SECOND COMPANY: ")
fx = SD.selection(2)
for i in range(0, 10):
    print("DATE: ", X[i], " / 10")
    print("SECOND DEGREE (error): ")
    print(abs(SD.Second_Degree_Polynomial(2, X[i]) - fx[i]))
    print("THIRD DEGREE (error): ")
    print(abs(TD.Third_Degree_Polynomial(2, X[i]) - fx[i]))
    print("FOURTH DEGREE (error): ")
    print(abs(FD.Fourth_Degree_Polynomial(2, X[i]) - fx[i]))
    print("\n")

# Για τις ημέρες πρόβλεψης
# 1ης εταιρίας
# Μία ημέρα μετά τα γενέθλια
x = 31
fx = 19.00
print("FIRST COMPANY: ")
print("DATE: ", x, " / 10")
print("SECOND DEGREE (error): ")
print(abs(SD.Second_Degree_Polynomial(1, x) - fx))
print("THIRD DEGREE (error): ")
print(abs(TD.Third_Degree_Polynomial(1, x) - fx))
print("FOURTH DEGREE (error): ")
print(abs(FD.Fourth_Degree_Polynomial(1, x) - fx))
print("\n")
# Πέντε ημέρες μετά τα γενέθλια
x = 4
fx = 18.78
print("FIRST COMPANY: ")
print("DATE: ", x, " / 11")
print("SECOND DEGREE (error): ")
print(abs(SD.Second_Degree_Polynomial(1, x) - fx))
print("THIRD DEGREE (error): ")
print(abs(TD.Third_Degree_Polynomial(1, x) - fx))
print("FOURTH DEGREE (error): ")
print(abs(FD.Fourth_Degree_Polynomial(1, x) - fx))
print("\n")

# 2ης εταιρίας
# Μία ημέρα μετά τα γενέθλια
x = 31
fx = 0.6750
print("SECOND COMPANY: ")
print("DATE: ", x, " / 11")
print("SECOND DEGREE (error): ")
print(abs(SD.Second_Degree_Polynomial(2, x) - fx))
print("THIRD DEGREE (error): ")
print(abs(TD.Third_Degree_Polynomial(2, x) - fx))
print("FOURTH DEGREE (error): ")
print(abs(FD.Fourth_Degree_Polynomial(2, x) - fx))
print("\n")
# Πέντε ημέρες μετά τα γενέθλια
x = 4
fx = 0.7290
print("SECOND COMPANY: ")
print("DATE: ", x, " / 11")
print("SECOND DEGREE (error): ")
print(abs(SD.Second_Degree_Polynomial(2, x) - fx))
print("THIRD DEGREE (error): ")
print(abs(TD.Third_Degree_Polynomial(2, x) - fx))
print("FOURTH DEGREE (error): ")
print(abs(FD.Fourth_Degree_Polynomial(2, x) - fx))
print("\n")
