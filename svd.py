"""
Author : Gülşah Büyük
Date : 22.03.2021
"""
import numpy as np
import scipy.linalg as la
from numpy.linalg import svd


def SVD(A):
    m = A.shape[0]
    n = A.shape[1]
    S = np.zeros(n)

    #Find eigenvectors of biggest values A * A^-1

    helper = np.matmul(A, np.transpose(A))
    eigenvalues, eigenvectors = la.eigh(helper)

    index = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[index]
    eigenvectors = eigenvectors[:, index]
    U = eigenvectors

    # S is a diagonal matrix that keeps square root of eigenvalues
    j = 0
    for i in eigenvalues:
        if j == S.size:
            break
        elif i >= 0:
            S[j] = np.sqrt(i)
            j += 1
    #
    helper = np.matmul(np.transpose(A), A)
    eigenvalues, eigenvectors = la.eigh(helper)
    #
    index = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[index]
    eigenvectors = eigenvectors[:, index]
    V = np.transpose(eigenvectors)

    # S is a diagonal matrix that keeps square root of eigenvalues
    for i in eigenvalues:
        if j == S.size:
            break
        elif i >= 0:
            S[j] = np.sqrt(i)
            j += 1

    # sorting S in descending order
    S[::-1].sort()
    # # print_to_file(S)

    return U, S, V

a = [[32,22,64],[41,17,3],[25,63,19]]

U, sigma, VT = svd(a)
# U, sigma, VT = SVD(np.array(a))
print(U)
print(sigma)
print(VT)
#
#
# U, sigma, VT = SVD(np.array(a))

#
# print(U)
# print()
# print(sigma)
# print()
# print(VT)