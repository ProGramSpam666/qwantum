import numpy as np
from quantum.utils import Gvec

#eq 16, obtain ek, compare with solveschrodinger
#should be summing over m
#want NbasisxNbasis array
#OB_bi -> (2N_G+1, NBasis)
#k0 -> (Nbasis, Nbasis)
#Nbasis = OB_bi.shape[1]
#Ng = OB_bi.shape[0]
#k0 = np.zero((Nbasis, Nbasis))
#i contain [0, Nbasis)
#j contain [0, Nbasis)
#m contain [0, Ng)
#k0[i,j] += np.conj(OB_bi[m,i])*OB_bi[m,j]*Gvec(m-Ng, a)
#m -> 0,....,2N_G +1 where this is = -N_G -> N_G



def calculatek0(OB_bi, a):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    k0 = np.zeros((Nbasis, Nbasis), dtype=np.complex)
    for i in range(Nbasis):
        for j in range(Nbasis): 
            for m in range(0, Ng):
                k0[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m- int((Ng-1)/2), a)
    return k0


def calculatek1(OB_bi, a):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    k1 = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis):    
            for m in range(0,Ng):
                k1[i, j] += 2*np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m- int((Ng-1)/2), a)**2
    return k1


def calculateVLoc(OB_bi, potential):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    vloc = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis):    
            for m in range(0, Ng): 
                for n in range(0, Ng): 
                    vloc[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[n, j]*potential.ft(m-n)
    return vloc



def interpolateHamiltonian(OB_bi, potential, kList): #kList = N_k ?
    Nbasis = OB_bi.shape[1]
    vLoc = calculateVLoc(
        OB_bi=OB_bi,
        potential=potential,
    )
    a = potential.parms["lattice"]
    k0 = calculatek0(
        OB_bi=OB_bi,
        a=a
    )
    k1 = calculatek1(
        OB_bi=OB_bi,
        a=a
    )
    for k in(kList):
        Hk = np.zeros((Nbasis, Nbasis), dtype = np.complex_)
        Hk[:,:] = 0.5*(k0[:,:] + vLoc[:,:])
        for i in range(Nbasis):
            for j in range(Nbasis):

                if (i == j):
                    Hk[i,j] += k^2
                else:
                    Hk[i,j] += k*k1[i,j]

    return Hk   



