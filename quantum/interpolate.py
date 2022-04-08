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


def calculatek0(OB_bi, potential):
    a = potential.parms["lattice"]
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    k0 = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis): 
            for m in range(0, Ng):
                k0[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m- int((Ng-1)/2), a)**2
    return k0


def calculatek1(OB_bi, potential):
    a = potential.parms["lattice"]
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    k1 = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis): 
            for m in range(0, Ng):
                k1[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m- int((Ng-1)/2), a)  
    return 2*k1  
   

def calculateVLoc(OB_bi, potential):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    vloc = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis):    
            for m in range(0, Ng): #m for G
                for n in range(0, Ng): #n for G'
                    vloc[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[n, j]*potential.ft(m-n)
    return vloc


#Interpolating and diagonalising
def interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N):
    Nbasis = OB_bi.shape[1]
    E = np.zeros((len(kList), N))
    ik = 0
    for k in(kList):
        Hk = np.zeros((Nbasis, Nbasis), dtype = np.complex_)
        for i in range(Nbasis):
            for j in range(Nbasis):
                Hk[i,j] = 0.5*k0[i,j] + VLoc[i,j]
                if (i == j):
                    Hk[i ,j] += 0.5*(k**2)
                Hk[i,j] += 0.5*(k*k1[i,j])
        ek2 = np.linalg.eigvalsh(Hk)    
        E[ik,0:N] = ek2[0:N]
        ik +=1
    return E #allowed Eigenenergies

