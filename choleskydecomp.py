"""
Author : Gülşah Büyük
Date : 1.04.2021
"""
import numpy as np
# The Cholesky decomposition is used in the special case when A is a square,
# conjugate symmetric matrix.
A = np.array([[61, 2, 5, 9], [1, 6, 4, 10], [3, 2, 8, 5], [18, 5, 1, 36]])

def Choleosky_Decomp(A):
    # The Cholesky decomposition maps matrix A into the product of A = L · LH
    # where L is the lower triangular matrix and
    # LH is the transposed, complex conjugate or Hermitian,
    # and therefore of upper triangular form
    n = A.shape[0]
    L = np.zeros((n,n),dtype=float)
    # The solution to find L requires square root
    # and inverse square root operators.

    for j in range(n):
        # We define the decomposed matrix as L.
        # Thus L[k−1] represents the (k−1)×(k−1) upper left corner of L.
        # a[k] and l[k] denote the first k−1 entries in column k of A and L, respectively.
        # a[k,k] and l[k,k] are defined as the entries of A and L.
        sum=0.
        for k in range(j):
            sum+=float(L[j,k]**2)
        L[j,j]=float(np.sqrt(A[j,j]-sum))
        for i in range(j+1,n):
            sum=0.
            for k in range(j):
                sum+=float(L[i,k]*L[j,k])
            L[i,j]=float((A[i,j]-sum)/L[j,j])

    print("Matrix A:")
    print(A)
    print(" ")
    print("Lower Triangular L:")
    print(L)
    print(" ")
    print("Upper Triangular U:")
    print(L.T)
    return L
# Cholesky factor of A and can be interpreted as the
# square root of a positive-definite matrix.
Choleosky_Decomp(A)
