from quantum.qobj import Qobj
from quantum.plot import plotBand
import matplotlib.pyplot as plt
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.utils import kvec
import time


qobj = Qobj()

#-------------------COMPARING TO STANDARD EIGENVALUES EK---------------
def testCorrespondingSchrodinger():
    starttime = time.time()
    potential = qobj.getPotential()
    ek = qobj.getEk()
    result = plotBand(ek,potential, 'g' )
    endtime = time.time()
    timeElapsed = endtime - starttime
    print("------Time Elapsed------")
    print(timeElapsed)
    return ek, result
print("------Ek Schrodinger-------")
print(testCorrespondingSchrodinger())


#----------------TESTING OPTIMISED EK AND PLOTTING NEW BAND----------
def NEWtestInterpolateHamiltonian():
    starttime = time.time()
    latticeptl1 = qobj.getPotential()
    a = latticeptl1.parms["lattice"]
    N_k = qobj.getN_K()
    N_b = qobj.getN_B()
    sb = qobj.getSb()
    ck = qobj.getCk()
    OB_bi = optimalBasis(sb, N_b, N_k, ck)
    k0 = calculatek0(OB_bi, latticeptl1)
    k1 = calculatek1(OB_bi, latticeptl1)
    VLoc = calculateVLoc(OB_bi, latticeptl1)
    kList = []
    for i in range(N_k):
        kList.append(kvec(i,a,N_k))    
    eigenEnergies = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N_b)
    result = plotBand(eigenEnergies, latticeptl1, 'b')
    endtime = time.time()
    timeElapsed = endtime - starttime
    print("-----Time Elapsed Optimised-----")
    print(timeElapsed)
    return eigenEnergies, result
print("-----Interpolate Hamiltonian------")  
print(NEWtestInterpolateHamiltonian())    








