import numpy as np



"""Function to obtain the Dielectric Function with respect to the Standard Basis
Implementation approach"""
def standardDielectricFunc(N_k, N_b, bi_out, ek, q, w):
    constant = 1 - 4/np.pi
    for k in range(N_k):
        for n in range(N_b):
            for nprime in range(N_b):
                frac1 = bi_out / (ek[n, k] - ek[nprime, k])**2
    return frac1



"""Function to obtain the Dielectric Function with respect to the Optimal Basis
Implementation approach"""
def optimalDielectricFunc(N_k, OB_bi):
    Nbasis = OB_bi.shape[1]
    constant = 1 - 4/np.pi
    for k in range(N_k):
        for n in range(Nbasis):
            for nprime in range(Nbasis):
                yip = 2
    return yip





