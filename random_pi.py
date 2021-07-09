"""
Author : Gülşah Büyük
Date : 9.03.2021
"""

from random import random
import numpy as np
from time import perf_counter
all =eval(input("Point count: "))
starttime=perf_counter()
inside =0

x=np.random.rand(all)
y=np.random.rand(all)

inside=np.where((x**2+y**2)**(0.5)< 1,1,0).sum()

mypi=4.0*(inside/all)

elapsedtime= (perf_counter()-starttime)
print("The value of pi for %d points is %f for %f seconds"%(all,mypi,elapsedtime))