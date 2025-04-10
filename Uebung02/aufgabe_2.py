import numpy as np


def gauss(A, b):
    A = A.astype(float)  # ensure float division
    b = b.astype(float)

    n = A.shape[0]  # number of rows
    for k in range(n - 2):
        faktor = A[k + 1, k] / A[k, k]
        A[k + 1, :] -= faktor * A[k, :]
        b[k+1] -= faktor * b[k]

    result = np.zeros_like(b)
    result[-1] = b[-1]/A[-1,-1]
    for i in range(n - 2):
        result[-i] = (b-sum(result[-i+1:-1]))/A[-1,-1]
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
