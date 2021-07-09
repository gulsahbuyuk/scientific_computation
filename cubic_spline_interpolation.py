"""
Author : Gülşah Büyük
Date : 3.04.2021
"""
import numpy as np
import matplotlib.pyplot as plt
def cubic_spline(x_new, x, y):
    # Cubic Spline is a piece-wise cubic polynomial that is twice continuously differentiable.
    # It is considerably ‘stiffer’ than a polynomial in the sense that
    # it has less tendency to oscillate between data points.
    x = np.array(x)
    y = np.array(y)
    # check if sorted because x should be SORTED.
    if np.any(np.diff(x) < 0):
        indexes = np.sort(x)
        x = x[indexes]
        y = y[indexes]
    size = len(x)
    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # creating buffer matrices
    Li = np.empty(size)
    Li_1 = np.empty(size-1)
    z = np.empty(size)

    # fill diagonals Li and Li-1 and solve [L][y] = [B]
    Li[0] = np.sqrt(2*xdiff[0])
    Li_1[0] = 0.0
    # The natural spline is defined as setting the second derivative of the first and
    # the last polynomial equal to zero in the interpolation function’s boundary points
    # Second derivatives at the endpoints are known:
    B0 = 0.0 # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size-1, 1):
        Li_1[i] = xdiff[i-1] / Li[i-1]
        Li[i] = np.sqrt(2*(xdiff[i-1]+xdiff[i]) - Li_1[i-1] * Li_1[i-1])
        Bi = 6*(ydiff[i]/xdiff[i] - ydiff[i-1]/xdiff[i-1])
        z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    i = size - 1
    Li_1[i-1] = xdiff[-1] / Li[i-1]
    Li[i] = np.sqrt(2*xdiff[-1] - Li_1[i-1] * Li_1[i-1])
    Bi = 0.0 # Boundary condition “natural”.
    # Intuitively, the result looks best compared to the other methods.
    z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    # solve [L.T][x] = [y]
    i = size-1
    z[i] = z[i] / Li[i]
    for i in range(size-2, -1, -1):
        z[i] = (z[i] - Li_1[i-1]*z[i+1])/Li[i]

    # find index
    index = x.searchsorted(x_new)
    np.clip(index, 1, size-1, index)

    xi1, xi0 = x[index], x[index-1]
    yi1, yi0 = y[index], y[index-1]
    zi1, zi0 = z[index], z[index-1]
    hi1 = xi1 - xi0

    # calculate cubic
    func = zi0/(6*hi1)*(xi1-x_new)**3 + \
         zi1/(6*hi1)*(x_new-xi0)**3 + \
         (yi1/hi1 - zi1*hi1/6)*(x_new-xi0) + \
         (yi0/hi1 - zi0*hi1/6)*(xi1-x_new)
    return func


if __name__ == '__main__':
    x_new = np.linspace(0, 4, 13)
    x = np.linspace(0, 4, 13)
    y = np.sin(x)
    cubic = cubic_spline(x_new, x, y)
    plt.scatter(x, y)
    plt.title('Cubic Spline Interpolation')
    plt.plot(x_new, cubic_spline(x_new, x, y))
    plt.show()
    print(cubic)