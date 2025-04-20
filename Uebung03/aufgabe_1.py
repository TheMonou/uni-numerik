import numpy as np

def tausche(A, z1, z2, p):
    temp = A[z1, :]
    A[z1, :] = A[z2, :]
    A[z2, :] = temp
    p[z1] = z2
    return p

def zerlegung(A):
    p = np.zeros(A.shape[0], dtype=float)
    for i in range(A.shape[0]):
        pivot = A[i, i]
        # Prüfung auf 0-Wert an Pivot-Stelle
        if pivot == 0:
            for j in range(A.shape[0]):
                if A[j, i] != 0:
                    tausche(A, j, i, p)
                    break

        #Zerlegung




    pass

def rueckwaerts(lu, b):
    # Rücksubstitution
    b[-1] = b[-1] / lu[-1, -1]
    for i in range(2, lu.shape[0] + 1):
        b[-i] = (b[-i] - np.dot(lu[-i, -i + 1:], b[-i + 1:])) / lu[-i, -i]


def permutation(p,x):
    for i in range(len(p)):
        temp = x[i]
        x[i] = x[p[i]]
        x[p[i]] = temp

def main():
    pass

if __name__ == '__main__':
    main()

