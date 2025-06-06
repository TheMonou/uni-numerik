import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dividierte_differenzen(punkte):
    n = punkte.shape[1]
    x = punkte[0, :]
    y = punkte[1, :]
    dd = np.zeros((n,n))
    dd[np.diag_indices(n)] = y
    for i in range(1, n):
        for j in range(0, i):
            m = i-(j+1)
            dd[i, m] = (dd[i, m+1] - dd[i-1, m]) / (x[i] - x[m])

    return dd[:, 0]


def horner_auswertung(x, X, d):
    result = d[-1]
    n = len(d)-1
    for i in range(0, n):
        result = result * (x - X[n-i-1]) + d[n-i-1]
    return result


def interpolations_polynome(punkte, x):
    return horner_auswertung(x, punkte[0, :], dividierte_differenzen(punkte))

def f(x):
    return 1/(1+x**2)

def aufgabe_2_b(m):
    x = np.linspace(-5, 5, m)
    y = f(x)
    p = np.array((x, y))
    x_axis = np.linspace(-5, 5)
    y_inter = interpolations_polynome(p, x_axis)
    y_f = f(x_axis)

    df = pd.DataFrame({
        'x' : x_axis,
        'y_interpoliert' : y_inter,
        'y_f' : y_f
    })
    df = df.set_index('x')
    plt.ylabel('y')
    df.plot(title='Aufgabe 2b)')
    plt.show()

def calc_x(i, m):
    return -5 * np.cos(np.pi * (2 * i + 1) / (2 * m))


def aufgabe_2_c(m):
    x = np.arange(0, m-1)
    x = calc_x(x, m)
    y = f(x)
    p = np.array((x, y))
    x_axis = np.linspace(-5, 5)
    y_inter = interpolations_polynome(p, x_axis)
    y_f = f(x_axis)

    df = pd.DataFrame({
        'x' : x_axis,
        'y_interpoliert' : y_inter,
        'y_f' : y_f
    })
    df = df.set_index('x')
    df.plot(title='Aufgabe 2c)')
    plt.ylabel('y')
    plt.show()

def main():
    # Aufgabe 2a)
    print("Aufgabe 2a):")
    points = np.array([
        [0,1,3],
        [3,2,6]
    ])
    x = 2
    print(f" Interpolation von \n {points} \n an der Stelle x = {x}: \n {interpolations_polynome(points, x)}")

    # Aufgabe 2b)
    aufgabe_2_b(3)
    aufgabe_2_b(5)
    aufgabe_2_b(7)
    aufgabe_2_b(9)
    aufgabe_2_b(11)
    aufgabe_2_b(13)

    #Aufgabe 2c)
    aufgabe_2_c(9)
    aufgabe_2_c(11)
    aufgabe_2_c(13)

if __name__ == '__main__':
    main()
