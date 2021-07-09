"""
Author : Gülşah Büyük
Date : 1.04.2021
"""
import numpy as np
import math
import scipy.linalg

A = np.array([[61, 2, 5, 9], [1, 6, 4, 10], [3, 2, 8, 5], [18, 5, 1, 36]])
L = scipy.linalg.cholesky(A, lower=True)
U = scipy.linalg.cholesky(A, lower=False)
print ("Matrix A:")
print(A)

print("Lower Triangular L:")
print(L)

print("Transpose U:")
print(U)

