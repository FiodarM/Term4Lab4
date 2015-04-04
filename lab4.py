__author__ = 'fiodar'

from ode import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

f = lambda y, x: x**2 - y
x = np.linspace(0, 5.)
y_adm = odesolve_adams(f, 2., x)
y_rk = odesolve(f, 2., x)

fig = plt.figure(tight_layout=True)
ax = fig.add_subplot(111)
ax.plot(x, y_adm, label='Adams method')
ax.plot(x, y_rk, label='Runge - Kutta method')
ax.legend(loc='best')
plt.show()