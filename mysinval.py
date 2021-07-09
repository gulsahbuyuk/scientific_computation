"""
Author : Gülşah Büyük
Date : 1.04.2021
"""
import math
import numpy as np
import matplotlib.pyplot as plt
print("Please enter x and N values")
x,N=[int(x) for x in input().split()]
k=int()
p =[1,2,3,4,5,6,7]

def myownsin():
    myval=0
    for i in range(0,N):
        myval=((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1)
        myval +=myval
    return myval

