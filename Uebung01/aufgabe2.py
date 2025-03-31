import numpy as np
import math

def algorithm_1(n, x):
    """
        Algorithmus 1
    """
    result = 0
    for k in range(n):
        result += np.power(x, k)/np.math.factorial(k)

    return result

def algorithm_2(n, x):
    """
        Algorithmus 2
    """
    result = 0
    for k in range(n):
        result += np.power(x,n-k)/np.math.factorial(n-k)

    return result

def main():
    print("Aufgabe 2:")
    print("\n")

    print("n=10")