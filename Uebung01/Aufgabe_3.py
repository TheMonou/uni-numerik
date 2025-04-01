import numpy as np
import scipy as sp


def linkseitige_rechteckregel(f, a, b, n):
    """
        Berechnung des Integrals mit der linkseitigen Rechteckregel
    """

    result = 0
    h = (b-a)/n
    for i in range(n-1):
        result += f(a+i*h)

    result *= h
    return result


def rechtsseitige_rechteckregel(f, a, b, n):
    """
        Berechnung des Integrals mit der rechtsseitigen Rechteckregel
    """
    result = 0
    h = (b - a) / n
    for i in range(1, n):
        result += f(a + i * h)

    result *= h
    return result


def trapezregel(f, a, b, n):
    """
        Berechnung des Integrals mit der Trapezregel
    """
    result = 0
    h = (b - a) / n
    for i in range(1, n):
        result += f(a + i * h) + f(b)

    result *= 2
    result += f(a)
    result *= h / 2
    return result

def f(x):
    """
        Funktion f(x) = 1/x^2
    """
    return 1/np.square(x)



def durchlauf(f, a, b, n):
    print("Integrationsgrenzen:")
    print("a = " + str(a))
    print("b = " + str(b))

    actual = sp.integrate.quad(f, a, b)[0]
    print("\n")

    print("linkseitige Rechteckregel:")
    res = linkseitige_rechteckregel(f, a, b, n)
    print("actual: " + str(actual))
    print("res: " + str(res))
    print("Abweichung: " + str(np.abs(actual - res)))
    print("\n")

    print("rechtsseitige Rechteckregel:")
    res = rechtsseitige_rechteckregel(f, a, b, n)
    print("actual: " + str(actual))
    print("res: " + str(res))
    print("Abweichung: " + str(np.abs(actual - res)))
    print("\n")

    print("Trapezregel:")
    res = trapezregel(f, a, b, n)
    print("actual: " + str(actual))
    print("res: " + str(res))
    print("Abweichung: " + str(np.abs(actual - res)))



def main():
    print("Aufgabe 3:")
    print("-----------------------------------------------")
    print("Funktion f(x) = 1/x^2")
    print("n = 100")
    print("\n")
    durchlauf(f, 1 / 10, 10, 100)
    print("\n")
    print("n = 1000")
    print("\n")
    durchlauf(f, 1 / 10, 10, 1000)
    print("\n")
    print("-----------------------------------------------")
    print("Funktion f(x) = ln(x)")
    print("n = 100")
    print("\n")
    durchlauf(np.log, 1 , 2, 100)
    print("\n")
    print("n = 1000")
    print("\n")
    durchlauf(np.log, 1, 2, 1000)
    print("\n")

    print()
if __name__ == "__main__":
    main()




