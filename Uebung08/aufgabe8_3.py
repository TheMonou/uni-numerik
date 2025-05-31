import numpy as np




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


    A2 = generate_tridiagonal(10)
    print(f" n = 10: \n {A2}")


    A3 = generate_tridiagonal(20)

    print(f" n = 20: \n {A3}")



if __name__ == '__main__':
    main()