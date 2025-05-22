import numpy as np

def tausche(A, z1, z2, b):
    print(f"Tausche Zeile {z1} mit Zeile {z2}")
    temp_row = A[z1, :].copy()
    A[z1, :] = A[z2, :]
    A[z2, :] = temp_row.copy()

    temp = b[z1]
    b[z1] = b[z2]
    b[z2] = temp

def gauss(A, b):
    A = A.astype(float)  # Ensure A is of type float
    b = b.astype(float)  # Ensure b is of type float


    for k in range(A.shape[0]-1):
        pivot = A[k,k]
        # Prüfen ob das Pivot-Element 0 ist und ggfs. Zeilen tauschen
        if pivot == 0:
            for i in range(k+1, A.shape[0]):
                if (A[i ,k] != 0):
                    tausche(A, k, i, b)
                    break
            else:
                raise ValueError(f"No non-zero pivot found in column {k}.")

        # Eliminationsschritt
        faktoren = A[k + 1:, k] / pivot
        A[k+1:, :] -= faktoren[:, np.newaxis] * A[k, :]
        b[k+1:] -= faktoren * b[k]


    # Rücksubstitution
    b[-1] = b[-1] / A[-1,-1]
    for i in range(2, A.shape[0]+1):
        b[-i] = (b[-i] - np.dot(A[-i, -i + 1:], b[-i + 1:])) / A[-i, -i]


    return b


def main():
    A = np.array([
        [1, 3, 1, 1],
        [0, 1, 0, 2],
        [2, 1, 0, 0],
        [0, 4, 4, 0]
    ])

    b1 = np.array([6, 2, 4, 12])

    print(gauss(A, b1))

    b2 = np.array([8, 7, 1, 12])

    print(gauss(A, b2))


if __name__ == "__main__":
    main()
