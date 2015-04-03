__author__ = 'fiodar'

import numpy as np


def odesolve_adams(f, y0, sequence, tol):
    y = np.array([y0], dtype=float)
    h = sequence[1] - sequence[0]
    predict_y = lambda x: y + h / 24. * (55 * f(x) - 59 * f(x - h) + 37 * f(x - 2 * h) + 9 * f(x - 3 * h))
    correct_y = lambda x: y + h / 24. * (9 * f(x + h) - 19 * f(x) - 5 * f(x - h) + f(x - 2 * h))

    for x in sequence[3:]:
        y = np.column_stack((y, predict_y(x)))
        while np.abs(correct_y(x) - y[-1]).any() > tol:
            y[-1] = correct_y(x)

    return y