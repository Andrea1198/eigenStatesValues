def triangolize(A):
    rows    = len(A)
    cols    = len(A[0])
    for j in range(cols-1):
        for i in range(j+1, rows):
            A[i,:] -= A[j,:] * A[i,j] / A[j, j]
    return A

def generateRandomMatrix(n):
    from numpy.random import random
    A = random((n, n))
    return A
