import numpy as np
from quantum.optimalbasis import optimalBasis, optimalProductBasis
import scipy.integrate as integrate
from scipy.integrate import quad
from quantum import potential as pt
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasisWithoutInspection
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
                vloc = summation*integralTerm
    return vloc


def interpolateHamiltonian(OB_bi, Nbasis, a, kList, potential, N_G):
    vLoc = calculateVLoc()
    a = potential.parms["lattice"]
    kList = 100
    k0 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    k1 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    vLoc = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    for i in(Nbasis):
        for j in(Nbasis):
            for m in range(0, Gvec):
                k0[i, j] = 2*(np.conjugate(OB_bi[m, i])*OB_bi[m, j]*Gvec(m, a))
                k1[i, j] = np.conjugate(OB_bi[m, i])*OB_bi[m, j]*(Gvec(m, a)**2)

            vLoc[i, j] = vLoc[i,j] #be careful
            M = np.zeros((2*N_G+1, 2*N_G+1), dtype=np.complex_)
            for k in(kList):
                M[i+N_G, j+N_G] = 0.5*(k**2*Kronecker + kList*k1 + k0 ) + vLoc
    return M












