import numpy as np
from quantum.optimalbasis import OptimalBasis, optimalProductBasis
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad
import potential as pt
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasisWithoutInspection
from quantum.utils import kinetic

 #eq 16, obtain ek, compare with solveschrodinger

def interpolateHamiltonian(sb, OB_bi, kpoints, N_G, N_k, N_b, ck, ik, potential):
    bi_out = optimalBasisWithoutInspection(sb ,N_k, N_b, ck)
    Nbasis = bi_out
    k0 = np.zeros(np.shape(OB_bi)[0], np.shape(OB_bi)[1])
    k1 = np.zeros(np.shape(OB_bi)[0], np.shape(OB_bi)[1])
    vloc = np.zeros(np.shape(OB_bi)[0], np.shape(OB_bi)[1])
    for i in(Nbasis):
        for j in(Nbasis):
            k0[i, j] = 2*(OB_bi[i, j]*N_G*OB_bi[i, j])
            k1[i, j] = OB_bi[i, j]*(N_G**2)*OB_bi[i, j]
            termToIntegrate = OB_bi[i, j]*()*OB_bi[i, j]
            vloc[i, j] = integrate.quad(termToIntegrate,-N_G, N_G+1)

    a = potential.parms["lattice"]
    M = np.zeros((2*N_G+1, 2*N_G+1), dtype=np.complex_)        
    for N_k in kpoints:
        for ig1 in range(-N_G, N_G+1):
            for ig2 in range(-N_G, N_G+1):
                if (ig1 == ig2):
                    M[ig1+N_G, ig2+N_G] = kinetic(ik, ig1, a, N_k)
                else:
                    M[ig1+N_G, ig2+N_G] = potential.ft(ig2-ig1)
    return M
        
#hamiltonianFilledWithEk = 0.5*((kpoints**2)*np.kron(i, j) + (N_k*k1[i, j]) + k0[i, j])

def getTest():
    N_G = 11
    N_b = 5
    N_k = 100
    sb = 0.1
    kpoints = 60
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 1, "width" :1 }
    ptl = pf.createPotential("sech", ptparms )
    ek, ck = solveSchrodinger(N_G,N_k,N_b,ptl)
    OB_bi = optimalBasisWithoutInspection(sb, N_k, N_b, ck)
    for ik in range(N_k):
        newEk = interpolateHamiltonian(sb, OB_bi, kpoints, N_G, N_k, N_b, ck, ik, ptl ) 
    return newEk

print(getTest())        







