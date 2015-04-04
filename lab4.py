__author__ = 'fiodar'

from ode import *
import matplotlib.pyplot as plt

f = lambda y, x: x**2 - y
x = np.linspace(0, 5.)
y_adm = odesolve_adams(f, 2., x)
y_rk = odesolve(f, 2., x)
y_analytic = lambda x: x ** 2 - 2 * x + 2

fig = plt.figure(tight_layout=True)
ax = fig.add_subplot(111)
ax.plot(x, y_adm, label='Adams method')
ax.plot(x, y_analytic(x), label='analytic solution')
ax.fill_between(x, y_analytic(x), y_adm, alpha='0.2')
ax.legend(loc='best')
plt.show()