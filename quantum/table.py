import numpy as np
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.utils import kvec

#obtaining array giving difference in Eigenvalues from both respective methods
def differenceInEigenvalues(sb, N_G, N_k, N_b, potential, N):
    a = potential.parms["lattice"]
    ek, ck = solveSchrodinger(N_G,N_k,N_b,potential)
    OB_bi = optimalBasis(sb, N_b, N_k, ck)
    k0 = calculatek0(OB_bi, potential)
    k1 = calculatek1(OB_bi, potential)
    VLoc = calculateVLoc(OB_bi, potential)
    kList = []
    for i in range(N_k):
        kList.append(kvec(i,a,N_k))   
    eigenEnergies = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N)
    difference = ek - eigenEnergies - ek[0,0] + eigenEnergies[0,0]
    return difference
 

def differenceInVelocity():
    return 

