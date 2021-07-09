"""
Author : Gülşah Büyük
Date : 1.05.2021
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp

F = lambda t, s:np.dot(np.array([[0,1],[0,-9.8/s[1]]]),s)
y0 = 0
time = np.linspace(0, 4, 120)

def optimum(v0):
  solution = solve_ivp(F, [0, 4], [y0, v0], t_eval=time)
  y = solution.y[0]
  return (y[-1] - 70)
v0 = fsolve(func=optimum, x0=100)
print(v0)

solution = solve_ivp(F, [0, 4],[y0, v0], t_eval = time)
plt.plot(solution.t, solution.y[0])
plt.plot(4 , 70, 'ro')
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.title(f'calculated initial v={v0} m/s')
plt.show()