import numpy as np
from quantum.qobj import Qobj
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.utils import kvec

qobj = Qobj()

def differenceInEigenvalues():
    potential = qobj.getPotential()
    ek = qobj.getEk()
    a = potential.parms["lattice"]
    N_G = qobj.getN_G()
    N_k = qobj.getN_K()
    N_b = qobj.getN_B()
    sb = qobj.getSb()
    ek1, ck1 = solveSchrodinger(N_G,N_k,N_b,potential)
    del ek1
    OB_bi = optimalBasis(sb, N_b, N_k, ck1)
    k0 = calculatek0(OB_bi, potential)
    k1 = calculatek1(OB_bi, potential)
    VLoc = calculateVLoc(OB_bi, potential)
    kList = []
    for i in range(N_k):
        kList.append(kvec(i,a,N_k))
    print(kList)    
    eigenEnergies = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N_b)
    differenceArray = ek - eigenEnergies
    return differenceArray


#CHECK AS RESULTS DIFFER TO DIFFERENCE OBTAINED ABOVE !!!
def quantumObjDifferenceInEk():
    oldEk = qobj.getEk()
    newEk = qobj.getInterpolateHamiltonian()
    difference = oldEk - newEk
    return difference


def differenceInVelocity():
    return 

