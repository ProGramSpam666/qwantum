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
    maxDifference = np.amax(difference)
    return maxDifference
 



"""Function to obtain the relevant difference in Velocity with respect to the 
Standard Basis implementation (i.e relevant standardVelocity() function) and the
Optimal Basis implementation (i.e relevant interpolatedVelocity() function)."""
def differenceInVelocity(ck, potential, OBck, k1):
    stanVel = standardVelocity(potential, ck)
    interVel = interpolatedVelocity(potential, OBck, k1)
    difference = stanVel - interVel - stanVel[0, 0, 0] + interVel[0, 0, 0]
    maxDifference = np.abs(difference).max() #Greatest magnitude
    return maxDifference



