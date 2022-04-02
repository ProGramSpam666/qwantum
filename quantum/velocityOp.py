import numpy as np


""" def kDepVelOperator():
    vk = np.zeros((), dtype=np.complex_)
    return """


#k-dependent velocity operator in terms of the optimal Basis
def kDepVelOperatorOB(N_b, k1, OB_bi, kList, ck):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    vknew = np.zeros((Nbasis, Nbasis), dtype = np.complex_)
    ik = 0
    for k in(kList):
        for i in range(N_b):
            for j in range(N_b):
                if (i==j):
                    vknew[i, j] += k*np.dot(ck[k, i], ck[k, j])
                vknew[i, j] += np.conjugate(OB_bi[k, i])*(OB_bi[k, j]*k1[i,j])
    ik +=1
    return 0.5*vknew


