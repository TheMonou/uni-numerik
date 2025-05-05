import numpy as np

def tausche(A, z1, z2, p):
    print(f"Tausche Zeile {z1} mit Zeile {z2}")
    temp = A[z1, :]
    A[z1, :] = A[z2, :]
    A[z2, :] = temp
    p[z1] = z2
    print(f"p: {p}")
    return p

def zerlegung(A):
    p = np.zeros(A.shape[0], dtype=float)
    for i in range(A.shape[0]):
        print(f" i: {i}")
        pivot = A[i, i]
        # Prüfung auf 0-Wert an Pivot-Stelle
        if pivot == 0:
            for j in range(A.shape[0]):
                if A[j, i] != 0:
                    tausche(A, i, j, p)
                    break

        pivot = A[i, i]
        #Zerlegung
        faktoren = A[i + 1:, i] / pivot
        A[i + 1:, :] -= faktoren[:, np.newaxis] * A[i, :]
        A[i + 1:, i] = faktoren

    return p


def rueckwaerts(lu, b):
    # Rücksubstitution
    b[-1] = b[-1] / lu[-1, -1]
    for i in range(2, lu.shape[0] + 1):
        b[-i] = (b[-i] - np.dot(lu[-i, -i + 1:], b[-i + 1:])) / lu[-i, -i]

def vorwaerts(lu, b):
    for i in range(1, lu.shape[0]):
        b[i] = (b[i] - np.dot(lu[i, :i], b[:i])) / lu[i, i]


def permutation(p,x):
    for i in range(len(p)):
        temp = x[i]
        x[i] = x[p[i]]
        x[p[i]] = temp

def lösen(A, b, p):
    permutation(p, b)
    vorwaerts(A, b)
    rueckwaerts(A, b)


def main():
    A = np.array([
        [0, 0, 0, 1],
        [2, 1, 2, 0],
        [4, 4, 0, 0],
        [2, 3, 1, 0]
    ], dtype=float)

    p = zerlegung(A)

    print(f"A: {A}")

    b1 = np.array([3, 5, 4, 5])
    lösen(A, b1, p)
    print(b1)

    b2 = np.array([4, 10, 12, 11])
    lösen(A, b2, p)
    print(b2)

if __name__ == '__main__':
    main()

