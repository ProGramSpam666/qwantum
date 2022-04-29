import numpy as np
import matplotlib.pyplot as plt
from quantum.interpolate import calculatek0, calculatek1,calculateVLoc, interpolateHamiltonian
from quantum.optimalbasis import optimalBasis
import time
import matplotlib.pyplot as plt

def getOrder(sb, N_b, N_k, ck, potential, kList):
    listCompTime = []
    listN = []
    N = N_b
    OB_bi = optimalBasis(sb, N_b, N_k, ck)
    lengthOB = len(OB_bi)
    k0 = calculatek0(OB_bi, potential)
    k1 = calculatek1(OB_bi, potential)
    VLoc = calculateVLoc(OB_bi, potential)
    startTime = time.time()
    interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N)
    endTime = time.time()
    timeElapsed = endTime - startTime
    listCompTime.append(timeElapsed)
    listN.append(lengthOB)
    timeArray = np.array(listCompTime)
    nArray = np.array(listN)
    return nArray, timeArray
    
    
def getOrderPlot(N_b, N_k, ck, potential, kList):
    sbValues = np.linspace(0, 0.3, 20)
    for sb in sbValues:
        nArray, timeArray = getOrder(sb, N_b, N_k, ck, potential, kList)
    plt.xlabel("n")
    plt.ylabel("Computation time for Diagonalising matrix for given sb")
    plt.plot(nArray, timeArray , 'b')
    plt.show()    


    




