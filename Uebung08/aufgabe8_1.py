import numpy as np

def signum(t):
    if t >= 0: return 1
    else: return -1


def max_nebendiagonal_element(A):
    m = A.copy()
    np.fill_diagonal(m, 0)
    abs_matrix = np.abs(m)
    flat_index = np.argmax(abs_matrix)
    indices = np.unravel_index(flat_index, m.shape)
    return indices[0], indices[1]


def quadratsumme_nebendiagonal_elemente(A):
    m = A.copy()
    np.fill_diagonal(m, 0)

    return np.sum(m ** 2)


def jacobi_eigenvalues(A):
    N = quadratsumme_nebendiagonal_elemente(A)
    while N > 1e-3:
        i,j = max_nebendiagonal_element(A)
        a_ij = A[i,j]
        alpha = (A[j,j] - A[i,i]) / (2 * a_ij)
        c = np.sqrt(0.5 + 0.5 * np.sqrt(alpha**2 / (1 + alpha ** 2)))
        s = signum(alpha) / (2 * c * np.sqrt(1 + alpha**2))

        # QA

        a_i = A[i, :].copy()
        a_j = A[j, :].copy()

        A[i, :] = c * a_i + s * a_j
        A[j, :] = c * a_j + -s * a_i


        #(QA)Q^T
        a__i = A[:, i].copy()
        a__j = A[:, j].copy()
        A[:, i] = c * a__i + s * a__j
        A[:, j] = c * a__j + -s * a__i
        N = quadratsumme_nebendiagonal_elemente(A)

    return np.diag(A)


def generate_tridiagonal(n):
    A = 2 * np.eye(n, dtype=float)
    for i in range(n - 1):
        A[i, i+1] = A[i+1, i] = -1
    return A



def main():
    A1 = np.array(
        [
         [2, -1, 0, 0, 0],
         [-1, 2, -1, 0, 0],
         [0, -1, 2, -1, 0],
         [0, 0, -1, 2, -1],
         [0, 0, 0, -1, 2]
        ]
    , dtype=float)

    print(f" n = 5: \n {A1}")
    print(f"Jacobi Eigenwerte: {jacobi_eigenvalues(A1)}")
    print(f" Numpy Eigenwerte: {np.linalg.eigvals(A1)}")

    A2 = generate_tridiagonal(10)
    print(f" n = 10: \n {A2}")
    print(f"Jacobi Eigenwerte: {jacobi_eigenvalues(A2)}")
    print(f" Numpy Eigenwerte: {np.linalg.eigvals(A2)}")

    A3 = generate_tridiagonal(20)

    print(f" n = 20: \n {A3}")
    print(f"Jacobi Eigenwerte: {jacobi_eigenvalues(A3)}")
    print(f" Numpy Eigenwerte: {np.linalg.eigvals(A3)}")


if __name__ == '__main__':
    main()