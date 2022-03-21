import numpy as np
from quantum.utils import Gvec

#eq 16, obtain ek, compare with solveschrodinger

def calculatek0(OB_bi, m, a):
    k0 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    
    for i in range(OB_bi.shape[0]):
        for j in range(OB_bi.shape[1]):
            k0[i, j] = 2*(np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m, a))

    return k0

def calculatek1(OB_bi, m, a):
    k1 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    for i in range(k1.shape[0]):
        for j in range(k1.shape[1]):    
            k1[i, j] = np.conjugate(OB_bi[m, i])*OB_bi[m, j]*(Gvec(m, a)**2)

    return k1


def calculateVLoc(OB_bi, N_G, N_GPrime, N_GPrimePrime, potential, Ncell, Npoints):
    a = potential.parms["lattice"]
    x = np.asarray(potential.v(Ncell, Npoints), dtype=np.complex_)
    vloc = np.zeros(np.shape(x), dtype=np.complex_)
    
    for item in range(0,N_G):
        for i in range(0, N_GPrime):
            for j in range(0, N_GPrimePrime):
                    summation = np.conjugate(OB_bi[item, i])*potential.ft(i-j)*OB_bi[item,j]
                    integralTerm = (np.exp(1j*Gvec(i,a))*x)*(np.exp(1j*Gvec(item, a))*x)*(np.exp(1j*Gvec(j, a))*x)
                    term = summation*integralTerm
                    vloc += term
                    
    return vloc


def interpolateHamiltonian(OB_bi, potential, N_G, N_GPrime, N_GPrimePrime, Ncell, Npoints, m):
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
                    M[i+N_G, j+N_G] = vLoc[i,j]

    return M





