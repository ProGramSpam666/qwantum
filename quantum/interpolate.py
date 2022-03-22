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
    k0 = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    #k0 = np.zeros(np.shape(OB_bi)[0], np.shape(OB_bi)[1], dtype = np.complex_)

    for i in range(Nbasis):
        for j in range(Nbasis): 
            for m in range(0, Ng):
                k0[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m- int((Ng-1)/2), a)

    return k0

def calculatek1(OB_bi, a):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    k1 = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    #k1 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis):    
            for m in range(0,Ng):
                k1[i, j] += 2*np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m- int((Ng-1)/2), a)**2

    return k1


def calculateVLoc(OB_bi, potential):
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    #a = potential.parms["lattice"]
    #x = np.asarray(potential.v(Ncell, Npoints), dtype=np.complex_)
    vloc = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis):    
            for m in range(0, Ng): #m for G
                for n in range(0, Ng): #n for G'
                    vloc[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[n, j]*potential.ft(m-n)
    return vloc



def interpolateHamiltonian(OB_bi, potential, kList):
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
    #kList = [], list of k points, the k you want to interpolate
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









""" def interpolateHamiltonian(OB_bi, potential, N_G, N_GPrime, N_GPrimePrime, Ncell, Npoints, m):
    vLoc = calculateVLoc(
        OB_bi=OB_bi,
        N_G=N_G,
        N_GPrime=N_GPrime,
        N_GPrimePrime=N_GPrimePrime,
        potential=potential,
        Ncell=Ncell,
        Npoints=Npoints,
    )
    a = potential.parms["lattice"]
    k0 = calculatek0(
        OB_bi=OB_bi,
        m=m,
        a=a
    )
    k1 = calculatek1(
        OB_bi=OB_bi,
        m=m,
        a=a
    )
    print("----------------k0----------------- \n", k0, "\n")
    print(k0.size)
    print(k0.shape)
    print("----------------k1----------------- \n", k1, "\n")
    print(k1.size)
    print(k1.shape)
    #checking OB_bi[i] 
    for i in range(OB_bi.shape[0]):
        print(OB_bi[i])
    kList = 100
    M = np.zeros((2*N_G+1, 2*N_G+1), dtype=np.complex_)
    for i in range():
        for j in range(-N_G, N_G+1):  
            for k in range(kList):
                if (i == j):
                    M[i+N_G, j+N_G] = 0.5*(k**2 + kList*k1[i,j] + k0[i,j])
                else:
                    M[i+N_G, j+N_G] = vLoc[i,j] # shapes dont make sense what is vloc M; what is even meant to be rturned from this; what is klist

    return M """














