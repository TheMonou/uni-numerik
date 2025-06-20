import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def calc_stuetzstelle(i, m):
    return (2 / (m-1)) * i - 1

def stuetzstellen(m):
    return calc_stuetzstelle(np.arange(0, m), m)


def x(t):
    return t + (np.sin(2 * np.pi * t) / (t ** 2 + 1))

def y(t):
    return np.cos(2 * np.pi * t) / (2 * t ** 2 + 1)

def gamma(t):
    return np.array([x(t), y(t)])

def s_x(t, t_i):
    sx = CubicSpline(t_i, x(t_i), bc_type='natural')
    return sx(t)

def s_y(t, t_i):
    sy = CubicSpline(t_i, y(t_i), bc_type='natural')
    return sy(t)

def gamma_approx(t, t_i):
    return np.array([s_x(t, t_i), s_y(t, t_i)])

def main():
    m_werte = np.array([5, 7, 9, 11, 17])
    for m in m_werte:
        stuetzen = stuetzstellen(m)
        gamma_werte = gamma(np.linspace(-1, 1))
        plt.plot(gamma_werte[0, :],  gamma_werte[1, :])
        plt.show()
        approximated_values = gamma_approx(np.linspace(-1, 1), stuetzen)
        plt.plot(approximated_values[0,:], approximated_values[1, :])
        plt.show()

if __name__ == '__main__':
    main()