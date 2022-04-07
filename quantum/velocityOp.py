import numpy as np
from quantum.utils import Gvec


#k-dependent velocity operator in terms of the optimal Basis
def kDepVelOperatorOB(N_b, k1, OB_bi, kList, ck):
    Nbasis = OB_bi.shape[1]
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


#velcity in standard basis
def standardVelocity(N_k, N_b, potential, ck):
    Ng = ck.shape[0]
    a = potential.parms["lattice"]
    kth = 0
    for k in range(N_k):
        for ik in range(N_b):
            for ib in range(N_b):
                for m in range(0, Ng):
                    if (ik == ib):
                        ck[ ik, ib] += k
                    ck[:, ik, ib] += np.conjugate(ck[:, k, ik])*ck[:, k, ib]*Gvec(m- int((Ng-1)/2), a)   
    kth +=1
    return ck

