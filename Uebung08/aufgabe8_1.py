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

    return indices

def quadratsumme_nebendiagonal_elemente(A):
    m = A.copy()
    np.fill_diagonal(m, 0)
    print(m**2)
    print(np.sum(m ** 2))
    return np.sum(m ** 2)


def jacobi_eigenvalues(A):
    N = quadratsumme_nebendiagonal_elemente(A)
    while N > 1e-3:
        indices = max_nebendiagonal_element(A)
        a = A[indices]
        alpha = (A[indices[1], indices[1]] - A[indices[0], indices[0]]) / 2 * a
        c = np.sqrt(1/2 + (1/2) * np.sqrt((alpha**2 / 1 + alpha**2)))
        s = signum(a) / (2 * c * np.sqrt(1 + alpha**2))
        # QA
        A[indices[0], :] *= c
        A[indices[0], :] += s * A[indices[1], :]
        A[indices[1], :] *= c
        A[indices[1], :] += s * A[indices[0], :]

        #(QA)Q^T
        A[:, indices[0]] *= c
        A[:, indices[0]] += s * A[:, indices[1]]
        A[:, indices[1]] *= c
        A[:, indices[1]] += s * A[:, indices[0]]
        N = quadratsumme_nebendiagonal_elemente(A)

    return np.diag(A)

def main():
    A = np.array(
        [[2, -1, 0, 0, 0],
         [-1, 2, -1, 0, 0],
         [0, -1, 2, -1, 0],
         [0, 0, -1, 2, -1],
         [0, 0, 0, -1, 2]]
    , dtype=float)

    print(f"Jacobi Eigenwerte: {jacobi_eigenvalues(A)}")
    print(f"Numpy Eigenwerte: {np.linalg.eigvals(A)}")


if __name__ == '__main__':
    main()