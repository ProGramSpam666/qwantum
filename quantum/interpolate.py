import numpy as np
from quantum.utils import Gvec, kvec

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

    return k0

def calculatek1(OB_bi, potential):
    a = potential.parms["lattice"]
    Nbasis = OB_bi.shape[1]
    Ng = OB_bi.shape[0]
    k1 = np.zeros((Nbasis, Nbasis), dtype=np.complex_)
    #k1 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    for i in range(Nbasis):
        for j in range(Nbasis): 
            for m in range(0,Ng):
                k1[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m- int((Ng-1)/2), a)  
    return 2*k1  
   

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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
                if (i == j):
                    Hk[i ,j] += 0.5*(k**2)
                Hk[i,j] += 0.5*(k*k1[i,j])
                print(Hk.shape)
        ek2 = np.linalg.eigvalsh(Hk)    
        E[ik,0:N] = ek2[0:N]
        ik +=1
    return E #allowed Eigenenergies







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
    for i in range(-N_G):
        for j in range(OB_bi.shape[1]):
            for k in range(kList):
                if (i == j):
                    M[i+N_G, j+N_G] = 0.5*(k**2 + kList*k1[i,j] + k0[i,j])
                else:
                    M[i+N_G, j+N_G] = vLoc[i,j] # shapes dont make sense what is vloc M; what is even meant to be rturned from this; what is klist

    return M """





=======
                if (i == j):
                    Hk[i ,j] += 0.5*(k**2)
                Hk[i,j] += 0.5*(k*k1[i,j])
                print(Hk.shape)
        ek2 = np.linalg.eigvalsh(Hk)    
        E[ik,0:N] = ek2[0:N]
        ik +=1
    return E #allowed Eigenenergies
>>>>>>> Stashed changes








=======
                if (i == j):
                    Hk[i ,j] += 0.5*(k**2)
                Hk[i,j] += 0.5*(k*k1[i,j])
                print(Hk.shape)
        ek2 = np.linalg.eigvalsh(Hk)    
        E[ik,0:N] = ek2[0:N]
        ik +=1
    return E #allowed Eigenenergies
>>>>>>> Stashed changes

