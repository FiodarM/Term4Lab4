__author__ = 'fiodar'

import numpy as np


def odesolve_adams(f, y0, sequence, tol=1e-3):
    y = odesolve(f, y0, sequence[:4], tol)
    h = sequence[1] - sequence[0]
    predict_y = lambda y, x: y + h / 24. * \
                                 (55 * f(y, x) - 59 * f(y, x - h) + 37 * f(y, x - 2 * h) + 9 * f(y, x - 3 * h))
    correct_y = lambda y, x: y + h / 24. * (9 * f(y, x) - 19 * f(y, x - h) - 5 * f(y, x - 2 * h) + f(y, x - 3 * h))

    for x in sequence[4:]:
        y = np.append(y, predict_y(y[-1], x))
        y[-1] = correct_y(y[-1], x)

    return y


def odesolve(f, y0, sequence, tolerance=1e-2):
    sequence = np.append([], sequence)
    t = t0 = sequence[0]
    y = np.array(y0)
    ytable = np.array([y0])
    dt = (sequence[-1] - t0) * tolerance
    steps = 0

    k1 = lambda: f(y, t)
    k2 = lambda dt: f(y + k1() * dt / 3., t + dt / 3.)
    k3 = lambda dt: f(y + (-k1() / 3. + k2(dt)) * dt, t + dt * 2 / 3.)
    k4 = lambda dt: f(y + (k1() - k2(dt) + k3(dt)) * dt, t + dt)
    next_y = lambda dt: y + dt / 8. * (k1() + 3 * k2(dt) + 3 * k3(dt) + k4(dt))
    rest = lambda dt: np.abs(np.array(next_y(dt) - next_y(dt / 2.))) / 15.

    for end in sequence[1:]:

        while abs(t - t0) < abs(end - t0):

            if np.equal(rest(dt), rest(dt / 2.)).all():
                dt = end - t

            elif np.greater_equal(rest(dt), tolerance * np.abs(next_y(dt / 2.))).any():
                while np.greater_equal(rest(dt), tolerance * np.abs(next_y(dt / 2.))).any() \
                        and abs(dt) > 1e-6:
                    dt *= 0.5

            else:
                while np.less(rest(dt), tolerance * np.abs(next_y(dt / 2.))).all():
                    dt *= 1.2
                    if abs(t + dt - t0) > abs(end - t0):
                        dt = end - t
                        break

            y = next_y(dt)
            t += dt
            steps += 1

        t0 = t

        ytable = np.append(ytable, [y], axis=0)

    return ytable