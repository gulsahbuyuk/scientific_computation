"""
Author : Gülşah Büyük
Date : 17.04.2021
"""
import numpy as np
A = np.array([[22, -41, 2], [61, 17, -18], [-9, 74, -13]])
# For a square matrix A the QR Decomposition converts  into the product of an orthogonal matrix Q
#  (Q.T)Q= I and an upper triangular matrix R.
def householder_reflection(A):
    # A Householder Reflection is a linear transformation that enables a
    # vector to be reflected through a plane or hyperplane.
    size = len(A)
    # Set R equal to A, and create Q as a identity matrix of the same size
    Q = np.identity(size)
    R = np.copy(A)
    for i in range(size - 1):
        # Create the vectors x, e
        # x is the ith column of the matrix A
        x = R[i:, i]
        # e is eigenvector
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        # Using anonymous functions, we create u and v
        # u = x + (sigma)*e
        # sigma= -sgn(x[k])(||x||)
        u = x - e
        # v = u /||u||
        v = u / np.linalg.norm(u)
        Q_count = np.identity(size)
        # Q = I-2*v(v.T)
        Q_count[i:, i:] -= 2.0 * np.outer(v, v)
        # Q is now mxm householder matrix
        R = np.dot(Q_count, R)  # R=H(n-1)*...*H(2)*H(1)*A
        Q = np.dot(Q, Q_count)  # Q=H(n-1)*...*H(2)*H(1) H is the self-inverse matrix
    return (Q, R)

(Q, R) = householder_reflection(A)
print("A:")
print(A)

print("Q:")
print(Q)

print("R:")
print(R)

print("A = QR control:")
print(np.dot(Q,R))