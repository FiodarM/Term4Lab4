__author__ = 'fiodar'

from ode import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

f = lambda y, x: x**2 - y
x = np.linspace(0, 5.)
y = odeint(f, 2., x)

fig = plt.figure(tight_layout=True)
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.show()