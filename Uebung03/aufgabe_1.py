import numpy as np

def tausche(A, z1, z2, p):
    temp = A[z1, :]
    A[z1, :] = A[z2, :]
    A[z2, :] = temp
    p[z1] = z2
    return p

def zerlegung(A):
    p = np.zeros
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

def permutation(p,x):
    pass

def main():
    pass

if __name__ == '__main__':
    main()

