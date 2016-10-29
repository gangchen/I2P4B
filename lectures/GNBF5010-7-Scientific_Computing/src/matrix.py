import random

class DimError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def multiply(X, Y):

    if len(X[0]) != len(Y):
        raise DimError("Dim Error")

    result = [[0.0 for i in  range(len(Y[0]))] for j in range(len(X))]
    # iterate through rows of X
    for i in range(len(Y[0])):
       # iterate through columns of Y
       for j in range(len(X)):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[j][i] += X[j][k] * Y[k][i]

    return(result)

def genMat(N, M):
    return [[random.random() for i in range(N)] for j in range(M)]

import time

X = genMat(20, 60)
Y = genMat(50, 20)
try:
    start = time.time()
    ret = multiply(X, Y)
    end = time.time()
    print("Python:")
    print(end - start)
except DimError:
    print("Dim Error")

import numpy as np

X1 = np.array(X)
Y1 = np.array(Y)
start = time.time()
ret = X1.dot(Y1)
end = time.time()
print("NumPy:")
print(end - start)
