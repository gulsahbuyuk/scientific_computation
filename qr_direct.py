"""
Author : Gülşah Büyük
Date : 17.04.2021
"""

import numpy as np
import scipy.linalg   # SciPy Linear Algebra Library

A = np.array([[22, -41, 2], [61, 17, -18], [-9, 74, -13]])
Q, R = scipy.linalg.qr(A)
print("A:")
print(A)
print("Q:")
print(Q)
print("R:")
print(R)



