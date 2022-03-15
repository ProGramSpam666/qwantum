import numpy as np
from quantum.optimalbasis import optimalBasis, optimalProductBasis
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad
from quantum import potential as pt
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasisWithoutInspection
from quantum.utils import kinetic, Gvec

#eq 16, obtain ek, compare with solveschrodinger

def interpolateHamiltonian(sb, OB_bi, kpoints, N_G, N_k, N_b, ck, ik, potential):
    bi_out = optimalBasisWithoutInspection(sb ,N_k, N_b, ck)
    Nbasis = bi_out
    k0 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    k1 = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    vloc = np.zeros(np.shape(OB_bi), dtype = np.complex_)
    a = potential.parms["lattice"]
    M = np.zeros((2*N_G+1, 2*N_G+1), dtype=np.complex_) 
    N = N_b
    for i in(Nbasis):
        for j in(Nbasis):
            for m in(Gvec(m, a)):
                k1[i, j] = 2*(OB_bi[m, i]*OB_bi[m,j])*Gvec(m, a)
                k0[i, j] = OB_bi[m, i]**OB_bi[m, j]*(Gvec(m, a)**2)
                termToIntegrate = OB_bi[i, j]*(potential.ft(i-j))*OB_bi[i, j]
                vloc[i, j] = integrate.quad(termToIntegrate,-N_G, N_G+1)

    for N_k in kpoints:
        for ig1 in range(-N_G, N_G+1):
            for ig2 in range(-N_G, N_G+1):
                if (ig1 == ig2):
                    M[ig1+N_G, ig2+N_G] = kinetic(ik, ig1, a, N_k)
                else:
                    M[ig1+N_G, ig2+N_G] = potential.ft(ig2-ig1)
    return M


    
 

