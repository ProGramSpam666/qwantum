import numpy as np
from quantum.utils import Gvec, Kronecker

#eq 16, obtain ek, compare with solveschrodinger


def calculateVLoc(OB_bi, N_G, N_GPrime, N_GPrimePrime, potential, Ncell, Npoints):
    a = potential.parms["lattice"]
    x= potential.v(Ncell, Npoints)
    for item in range(0,N_G):
        for i in range(0, N_GPrime):
            for j in range(0, N_GPrimePrime):
                summation = np.conjugate(OB_bi[item, i])*potential.ft(i-j)*OB_bi[item,j]
                integralTerm = (np.exp(1j*Gvec(i,a))*x)*(np.exp(1j*Gvec(item, a))*x)*(np.exp(1j*Gvec(j, a))*x)
                vloc = vloc + summation*integralTerm 
    return vloc 

""" def interpolateHamiltonian(OB_bi, Nbasis, a, kList, potential, N_G):
    vLoc1 = calculateVLoc() ##### no sense if line 31
    a = potential.parms["lattice"] #doesnt make sense, a is a parameter
    kList = 100 # kList is a parameter no need to define
    k0 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    k1 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    vLoc2 = np.zeros(np.shape(OB_bi), dtype = np.complex_) #wHY WHat point, maybe var name mix up
    for i in Nbasis:
        for j in Nbasis:
            for m in range(0, Gvec): #doesnt make sense why u would do this, just keeps repeating calc for new m, doesnt change anything
                k0[i, j] += 2*(np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m, a))
                k1[i, j] += np.conjugate(OB_bi[m, i])*OB_bi[m, j]*(Gvec(m, a)**2)

            vLoc2[i, j] = vLoc1[i,j] #be careful;
            M = np.zeros((2*N_G+1, 2*N_G+1), dtype=np.complex_)
            for k in(kList):
                M[i+N_G, j+N_G] = 0.5*(k**2*Kronecker + kList*k1 + k0 ) + vLoc1
    return M """












