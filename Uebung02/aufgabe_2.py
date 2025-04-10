import numpy as np

def tausche(A, z1, z2, b):
    temp_row = A[z1, :].copy()
    A[z1, :] = A[z2, :]
    A[z2, :] = temp_row.copy()

    temp = b[z1]
    b[z1] = b[z2]
    b[z2] = temp

def gauss(A, b):
    for k in range(A.shape[0]-2):
        pivot = A[k,k]
        # Prüfen ob das Pivot-Element 0 ist und ggfs. Zeilen tauschen
        if pivot == 0:
            for i in range(k+1, A.shape[0]-1):
                if (A[i ,k] != 0):
                    tausche(A, k, i, b)
                    break
            else:
                raise ValueError(f"No non-zero pivot found in column {k}.")

        # Eliminationsschritt
        A[k+1, :] -= A[k+1,k]/pivot * A[k, :]
        b[k+1] -= A[k+1,k]/pivot * b[k]





    return result


def main():
    A = np.array([
        [1, 3, 1, 1],
        [0, 1, 0, 2],
        [2, 1, 0, 0],
        [0, 4, 4, 0]
    ])

    b = np.array([8, 7, 1, 12])

    print(gauss(A, b))


if __name__ == "__main__":
    main()
