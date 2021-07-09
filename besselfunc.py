"""
Author : Gülşah Büyük
Date : 24.06.2021
"""

# 090160132 Gülşah Büyük

import numpy as np
from matplotlib import pyplot as plt
from scipy.special import gamma
from scipy.special import jv


class BesselJ:
    # Need for defining Bessel Function Jn(x)
    def __init__(self, n, x):
        self.n = n
        self.x = x
        # This rat variable is to reform bessel equation, i.e. factorize it by 1 or -1
        self.rat = 1
        self.reformBesel()

    # this method written for connection formula i cannot replace inside of that method
    def reformBesel(self):
        if self.n < 0:
            self.n = self.n * -1
            self.rat = (-1) ** self.n

    def aroundzeroGB(self):
        #  The value of the bessel function x-->0
        Jn = ((self.x / 2) ** self.n) / gamma(self.n + 1)
        return Jn

    def aroundinfinitiyGB(self):
        # The value of the Bessel Function x-->inf
        Jn = np.sqrt(2 / (np.pi * self.x)) * np.cos(self.x - (self.n * np.pi / 2) - (np.pi / 4))
        return Jn

    def seriessolutionGB(self):
        # the machine epsilon value is analitically 0 but numerically machine
        # will compute different than 0.
        machineepsilonGB = abs(7 / 3 - 4 / 3 - 1)

        # initialize variable for summation
        Jn = 0
        k = 0

        # written from given formula
        while True:

            # calculate tk
            Tk = ((-1) ** k) * (self.x / 2) ** (2 * k + self.n) / (gamma(k + 1) * gamma(self.n + k + 1))
            # If k>0, calculate tk-1 it will be divide by 0 otherwise
            if k > 0:
                Tk_1 = ((-1) ** (k - 1)) * (self.x / 2) ** (2 * (k - 1) + self.n) / (
                            gamma((k - 1) + 1) * gamma(self.n + (k - 1) + 1))

            # If k>0 and abs value of difference smaller than machinepsilon break
            if k > 0 and abs(Tk - Tk_1) < machineepsilonGB:
                break
            # Add current val to jn
            Jn += ((-1) ** k) * (self.x / 2) ** (2 * k + self.n) / (gamma(k + 1) * gamma(self.n + k + 1))

            k += 1
        return Jn

    def besselcalculate(self):

        # If <0.7 calculate around zero and factor it by self.rat
        if abs(self.x) < 0.7:
            return self.rat * self.aroundzeroGB()

        # If greater than 100 calculate aroundinfinity and factor it by self.rat
        elif abs(self.x) > 100:
            return self.rat * self.aroundinfinitiyGB()
        # else calculate seriessolution and factor it by 1
        else:
            return self.rat * self.seriessolutionGB()


if __name__ == "__main__":

    # token from the given graph
    xvalues = [-10, 0.1, 10, 20, 30, 101, 150]
    nvalues = [0, 1, -1]

    # empty array is created for graph for every n value
    classresults0 = []
    classresults1 = []
    classresults_1 = []
    scipyresults0 = []
    scipyresults1 = []
    scipyresults_1 = []

    # calculation with scipy for every n values
    for i in xvalues:
        res = jv(0, i)
        scipyresults0.append(res)

    for i in xvalues:
        res = jv(1, i)
        scipyresults1.append(res)
    for i in xvalues:
        res = jv(-1, i)
        scipyresults_1.append(res)

    for i in xvalues:
        besselfunc0 = BesselJ(0, i)
        classresults0.append(besselfunc0.besselcalculate())
    for i in xvalues:
        besselfunc1 = BesselJ(1, i)
        classresults1.append(besselfunc1.besselcalculate())
    for i in xvalues:
        besselfunc_1 = BesselJ(-1, i)
        classresults_1.append(besselfunc_1.besselcalculate())

    print(classresults0, classresults_1)

    # use subplot to print all 3 table at once
    figure, axs = plt.subplots(3)
    figure.suptitle("The Bessel Results of Gülşah Büyük")

    # Plotting first axis
    # Scatter for scattering, plot for lines
    # Legend will be only on axs[0] only
    axs[0].scatter(xvalues, scipyresults0, color='r', marker='o', label="SciPy Results")
    axs[0].plot(xvalues, classresults0, color="b", label="Class Results")
    axs[0].legend(loc=1, frameon="False")
    axs[0].set_ylabel("$J_{0}(x)$")

    # Same for ax1, no legend
    axs[1].scatter(xvalues, scipyresults1, color='r', marker='o', label="SciPy Results")
    axs[1].plot(xvalues, classresults1, color="b", label="Class Results")
    axs[1].set_ylabel("$J_{1}(x)$")

    # Same for ax2, no legend
    axs[2].scatter(xvalues, scipyresults_1, color='r', marker='o', label="SciPy Results")
    axs[2].plot(xvalues, classresults_1, color="b", label="Class Results")
    axs[2].set_ylabel("$J_{-1}(x)$")

    # Rotate yticks by 45 for every axis, and remove xtickcs from the first 2 graph
    for ax in range(len(axs)):
        plt.sca(axs[ax])
        plt.yticks(rotation=45)
        if ax == 2:
            # If x == 2 rotate labels by 90
            plt.xticks(rotation=90)
        else:
            plt.xticks([])
    plt.show()