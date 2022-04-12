import numpy as np

def dielectricFunc(N_k, N_b, bi_out, ek, q, w):
    constant = 1 - 4/np.pi
    for k in range(N_k):
        for n in range(N_b):
            for nprime in range(N_b):
                numerator = bi_out
                denominator = (ek[nprime, k + q] - ek[n, k])**2
                diel = numerator/denominator
    return diel



