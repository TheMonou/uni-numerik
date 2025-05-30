import numpy as np

def dividierte_differenzen(punkte):
    x = punkte[:,0]
    y = punkte[:,1]
    dd = np.zeros(len(punkte))
    diagonal_indices = np.diag_indices(len(punkte))
    dd[diagonal_indices] = y
    for i in range(1, len(punkte)-1):
        for j in range(len(punkte)-i):
            pass




def interpolations_polynome(punkte):
    pass
