import numpy as np



def original_alg(p, q):
    """
        ursprünglicher Algorithmus
    """
    return p*-1+np.sqrt(np.square(p) + q)

def alternative_alg(p, q):
    """
        alternativer Algorithmus
    """
    x1 = -p - np.sqrt(np.square(p) + q)
    return -q/x1


def durchlauf(p, q):
    """
        Durchlauf der Algorithmen
    """


    print("ursprünglicher Algorithmus:")
    x = original_alg(p, q)
    print("x:" + str(x))
    print("Abweichung:")
    print(np.square(x) + 2 * p * x - q)

    print("alternativer Algorithmus:")
    x = alternative_alg(p, q)
    print("x:" + str(x))
    print("Abweichung:")
    print(np.square(x) + 2 * p * x - q)



def main():
    print("Aufgabe 1:")
    print("\n")
    print("10^2")
    durchlauf(1e2, 1)
    print("\n")
    print("10^4")
    durchlauf(1e4, 1)
    print("\n")
    print("10^6")
    durchlauf(1e6, 1)
    print("\n")
    print("10^7")
    durchlauf(1e7, 1)
    print("\n")
    print("10^8")
    durchlauf(1e8, 1)


if __name__ == "__main__":
    main()
