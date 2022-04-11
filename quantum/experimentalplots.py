#File designated for experimental plots to obtain.


import numpy as np
from quantum.optimalbasis import optimalBasis
import matplotlib.pyplot as plt
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.schrodinger import solveSchrodinger
from quantum.gettime import differenceInTimeForObtainingEk
import time
from quantum.table import differenceInEigenvalues


def sbEffectOnSize(N_b, N_k, ck):
    myListOb = []
    myListSb = []
    sbValues = np.linspace(0,1,250)
    for s_b in (sbValues):
        getOptimalBasis = optimalBasis(s_b, N_b, N_k, ck) 
        sizeOb = getOptimalBasis.size
        myListOb.append(sizeOb)
        myListSb.append(s_b)
    #print(myListOb)    
    myresultOb = np.array(myListOb)
    myresultSb = np.array(myListSb)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Sb value")
    plt.plot(myresultOb, myresultSb, 'g')
    plt.show()


def varyingNbOBPlot(N_k, ck):
    i = 0
    symbolList = ["r-", "b-", "g-", "k-", "y-", "p-", "c-"]
    for N_B in range(3, 7):
        sbEffectOnSize(N_B, N_k, ck)
        symbolList[i]
        i += 1
    return 


def optimalBasisVsCk(N_b, N_k, ck):
    myListOb = []
    myListCk = []
    sbValues = np.linspace(0,1,250)
    for s_b in sbValues:
        OB_bi = optimalBasis(s_b, N_b, N_k, ck)
        sizeOB_bi = OB_bi.size
        myListOb.append(sizeOB_bi)
        sizeCk = ck.size
        myListCk.append(sizeCk)
    myresultOb = np.array(myListOb)
    myresultCk = np.array(myListCk)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Size of Ck")
    plt.plot(myresultOb, myresultCk, 'r')
    plt.show()


def ekVsE(OB_bi, kList, k0, k1, VLoc, N_b, N_G, N_k, potential):
    E = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N_b)
    ek, ck = solveSchrodinger(N_G, N_k, N_b, potential )
    del ck
    plt.xlabel("ek")
    plt.ylabel("E")
    plt.plot(ek, E , 'b')
    plt.show()    


def EnergyVsN_G(N_k, N_b, potential):
    N_GValues = np.linspace(0,100,1)
    for Ng in(N_GValues):
        ek, ck = solveSchrodinger(Ng, N_k, N_b, potential)
    del ck
    plt.plot(ek, Ng)
    plt.show()    
    return 


def sbEffectOnEigenvalues(N_b, N_k, ck, OB_bi, kList, k0, k1, VLoc, N):
    myListSb = []
    sbValues = np.linspace(0,1,250)
    for s_b in sbValues:
        OB_bi = optimalBasis(s_b, N_b, N_k, ck) 
        myListSb.append(s_b)
    E = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N )
    myresultSb = np.array(myListSb)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Sb value")
    plt.plot(E, myresultSb, 'g')
    plt.show()
    
    
def differenceInEigenvaluesVsSb():
    return 


def timePlotVaryingSb(N_b, N_k, ck, potential, kList):
    N = N_b
    sbValues = np.linspace(0.5,0,100)
    sbList = []
    timeList = []
    for sb in sbValues:
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
    print(arrayTime)
    plt.xlabel("InterpolateHamiltonian() Computation Time")
    plt.ylabel("sb Value")
    plt.plot(arrayTime, arraySb, 'b')
    plt.show()


def sbEffectOnPrecision(N_G, N_k, N_b, potential, N):
    sbList = []
    maxEigList = []
    sbValues = np.linspace(0, 0.9, 20)
    for sb in sbValues:
        difference = differenceInEigenvalues(sb, N_G, N_k, N_b, potential, N)
        sbList.append(sb)
        maxEigList.append(difference)
    sbArray = np.array(sbList)
    eigArray = np.array(maxEigList)
    plt.xlabel("Maximum difference between eigenvalues obtained comparing SS & IH")
    plt.ylabel("sb Value")
    plt.plot(eigArray, sbArray, 'b')
    plt.show()
    

