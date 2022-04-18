import numpy as np
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.utils import kvec
from quantum.velocityOp import standardVelocity, interpolatedVelocity




"""Function that obtains the relevant maximum differnence in Eigenvalues with respect 
to the standard Basis implementation (i.e relevant solveSchrodinger() function) and the 
Optimal Basis implementation (i.e relevant interpolateHamiltonian() functionn).  The
maximum difference is output as this indicates the greatest possible margin of error when
comparing Eigenvalues.  Such a function gives an indication of the accuracy of the 
approximation of the Optimal Basis approach with respect to the Standard Basis approach"""
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
    maxValue = np.amax(difference)
    return maxValue
 



""""""
def differenceInVelocity(ck, potential, OBck, k1):
    stanVel = standardVelocity(potential, ck)
    maxStanVel = np.amax(stanVel)
    interVel = interpolatedVelocity(potential, OBck, k1)
    maxInterVel = np.amax(interVel)
    difference = maxStanVel - maxInterVel #- stanVel[0, 0, 0] + interVel[0, 0, 0]
    return difference



