import numpy as np
import scipy as sp

def trapezregel(f, a, b, n):
    """
        Berechnung des Integrals mit der Trapezregel
    """
    h = (b - a) / n
    x = np.linspace(a, b, n)
    y = np.sum(f(x))
    return y

def f(x):
    """
        Funktion f(x) = 1/x^2
    """
    return 1/np.square(x)

def main():
    print("Aufgabe 4:")
    print("-----------------------------------------------")
    print("Funktion f(x) = 1/x^2")
    a = 1 / 10
    b = 10
    actual = sp.integrate.quad(f, a, b)[0]

    print("n = 100")
    res = trapezregel(f, a, b, 100)
    print("actual: " + str(actual))
    print("res: " + str(res))
    print("Abweichung: " + str(np.abs(actual - res)))
    print("\n")

    print("n = 1000")
    res = trapezregel(f, a, b, 1000)
    print("actual: " + str(actual))
    print("res: " + str(res))
    print("Abweichung: " + str(np.abs(actual - res)))
    print("\n")

    print("-----------------------------------------------")
    print("Funktion f(x) = ln(x)")
    a = 1
    b = 2
    actual = sp.integrate.quad(np.log, a, b)[0]

    print("n = 100")
    res = trapezregel(np.log, a, b, 100)
    print("actual: " + str(actual))
    print("res: " + str(res))
    print("Abweichung: " + str(np.abs(actual - res)))
    print("\n")

    print("n = 1000")
    res = trapezregel(np.log, a, b, 1000)
    print("actual: " + str(actual))
    print("res: " + str(res))
    print("Abweichung: " + str(np.abs(actual - res)))
    print("\n")

if __name__ == "__main__":
    main()
