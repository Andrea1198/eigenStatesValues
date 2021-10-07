from src.functions import *
import numpy as np
from numpy.linalg import eig

A       = np.loadtxt("matrix.txt", delimiter=" ")
# A       = generateRandomMatrix(1000)
print("# Initial matrix is: ")
print(A)
print("# Triangolizing matrix..")
diagA   = triangolize(A)
print("# Trianogolized matrix is: ")
print(diagA)
eigenValues = [A[i,i] for i in range(len(A))]
# eigenValues.sort()
eigenValues = np.array(eigenValues)
w,v=eig(A)
print(v)
print(eigenValues)
# print("# The eigenvalues are: ", eigenValues)
