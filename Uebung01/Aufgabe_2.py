import numpy as np
import math

def algorithm_1(n, x):
    """
        Algorithmus 1
    """
    result = 0
    for k in range(n):
        result += np.power(x, k)/math.factorial(k)

    return result

def algorithm_2(n, x):
    """
        Algorithmus 2
    """
    result = 1
    for k in range(n):
        result += np.power(x,n-k)/math.factorial(n-k)

    return result

def compare_algorithms(n, x):
    print("n = " + str(n) + ", x = " + str(x))
    print("algorithm_1: ", algorithm_1(n, x))
    print("algorithm_2: ", algorithm_2(n, x))
    print("actual: ", np.exp(x))

def main():
    print("Aufgabe 2:")
    print("\n")
    compare_algorithms(10, 1)
    print("\n")
    compare_algorithms(10, 10)
    print("\n")
    compare_algorithms(10, 3)
    print("\n")
    compare_algorithms(100, 1)
    print("\n")
    compare_algorithms(100, 10)
    print("\n")
    compare_algorithms(100, 3)


if __name__ == "__main__":
    main()
