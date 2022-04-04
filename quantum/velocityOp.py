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
def standardVelocity(N_b, kList, potential, ck):
    Nbasis = ck.shape[1]
    Ng = ck.shape[0]
    a = potential.parms["lattice"]
    velocity = np.zeros((Nbasis, Nbasis), dtype = np.complex_)
    ik = 0
    for k in(kList):
        for m in range(N_b):
            for n in range(N_b):
                if (m == n):
                    velocity[m, n] += k
                velocity[m, n] += np.conjugate(velocity[k, m])*velocity[k, n]*Gvec(m- int((Ng-1)/2), a)   
    ik +=1
    return velocity


#velocity optimal basis
def optimalVelocity():
    return 

