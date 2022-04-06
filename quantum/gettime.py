from quantum.schrodinger import solveSchrodinger
from quantum.interpolate import interpolateHamiltonian
from quantum.optimalbasis import optimalBasis
from quantum.interpolate import calculatek0, calculatek1, calculateVLoc
import numpy as np
import time


#obtain time taken to calculate eigenvalues using solveSchrodinger()
def standardTimeForEk(N_G, N_k, N_b, potential):
    startTimeStandard = time.time()
    solveSchrodinger(N_G, N_k, N_b, potential)
    endTimeStandard = time.time()
    timeElapsed = endTimeStandard - startTimeStandard
    return timeElapsed



#obtain time taken to calculate eigenvalues using interpolateHamiltonain()
def optimisedTimeForEk(OB_bi, kList, k0, k1, VLoc, N_b):
    N = N_b
    startTimeOptimised = time.time()
    interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N)
    endTimeOptimised = time.time() 
    timeElapsed = endTimeOptimised - startTimeOptimised
    return timeElapsed
    


#obtaining difference in time taken to calculate eigenvalues from each respective method
def differenceInTimeForObtainingEk(N_G, N_k, N_b, potential, OB_bi, kList, k0, k1, VLoc, N):
    SSTimeForEk = standardTimeForEk(N_G, N_k, N_b, potential)
    IHTimeForEk = optimisedTimeForEk(OB_bi, kList, k0, k1, VLoc, N)
    difference = SSTimeForEk - IHTimeForEk
    return difference



#obtaining difference in time for varying sb
def differenceInTimeVaryingSb(N_b, N_k, ck, potential, kList):
    N = N_b
    sbValues = np.linspace(0.5,0,100)
    sbList = []
    timeList = []
    for sb in (sbValues):
        startTime = time.time()
        OB_bi = optimalBasis(sb, N_b, N_k, ck)
        k0 = calculatek0(OB_bi, potential)
        k1 = calculatek1(OB_bi, potential)
        VLoc = calculateVLoc(OB_bi, potential)
        interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N)
        endTime = time.time()
        elapsedTime = endTime - startTime
        sbList.append(sb)
        timeList.append(elapsedTime)
    sbList = sbList[:-1]
    timeList = timeList[:-1]  
    arraySb = np.array(sbList)
    arrayTime = np.array(timeList) 
    print("---------arraySb values--------")
    print(arraySb)
    print("---------arrayTime values-------")
    print(arrayTime)
    return 





    