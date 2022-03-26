import numpy as np


#k-dependent velocity operator in terms of the optimal Basis
def kDepVelOperator(N_b, k1, k, OB_bi, kList, ck):
    Nbasis = OB_bi.shape[1]
    k1 = np.zeros((Nbasis, Nbasis), dtype=np.complex_)

    for k in range(kList):
        for n in range(N_b):
            for nprime in range(N_b):
                vk = np.zeros((Nbasis, Nbasis), dtype = np.complex_)
                vk[:,:] = k*np.dot(ck[n,k]*ck[nprime, k])
                for i in range(N_b):
                    for j in range(N_b):
                        vk[i,j] += 0.5*np.conjugate(OB_bi[:,n,i])*(OB_bi[:,nprime,j]*k1[i,j])

    return vk







