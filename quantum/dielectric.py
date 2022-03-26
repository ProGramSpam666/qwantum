import numpy as np
import math



def dielectricFunc(N_k, N_b, bi_out, ek, q, w):
    constant = 1 - 4/np.pi
    func = np.zeros()


    for k in range(N_k):
        for n in range(N_b):
            for nprime in range(N_b):
                func = func[n,k]*func[nprime,k]
                numerator = bi_out
                denominator = w - (ek[nprime, k + q] - ek[n, k]) + 1j
                Energy = func + numerator/denominator


    return Energy



