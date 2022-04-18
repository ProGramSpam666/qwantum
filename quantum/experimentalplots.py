"""File designated for experimental plots to obtain."""

import numpy as np
from quantum.optimalbasis import optimalBasis
import matplotlib.pyplot as plt
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.schrodinger import solveSchrodinger
from quantum.gettime import differenceInTimeForObtainingEk, standardTimeForEk, optimisedTimeForEk, optimisedTimeForEkEE, optimisedTimeForEkEENEW
import time
from quantum.table import differenceInEigenvalues
from quantum.utils import kvec



"""Function to investigate the size of Optimal Basis as Threshold sb varies"""
def sbEffectOnSize(N_b, N_k, ck):
    myListOb = []
    myListSb = []
    sbValues = np.linspace(0,1,250)
    #sbValues = [0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001 ]
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




"""Plot to show how the Number of Bands is directly dictated by the threshold sb"""
def varyingNbOBPlot(N_k, ck):
    i = 0
    symbolList = ["r-", "b-", "g-", "k-", "y-", "p-", "c-"]
    for N_B in range(3, 7):
        sbEffectOnSize(N_B, N_k, ck)
        symbolList[i]
        i += 1
    return 




"""Function to show size of Optimal basis against Standard Basis"""
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




"""Function to show relationship between eigenvalues obtained from implementing standard
Basis against Eigenvalues obtained from implementing Optimal Basis"""
def ekVsE(OB_bi, kList, k0, k1, VLoc, N_b, N_G, N_k, potential):
    E = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N_b)
    ek, ck = solveSchrodinger(N_G, N_k, N_b, potential )
    del ck
    plt.xlabel("ek")
    plt.ylabel("E")
    plt.plot(ek, E , 'b')
    plt.show()    



"""Function demonstrating the effect of the Eigenenergies obtained agaisnt 
the number of plane-waves included in the approximation of the periodic state"""
def EnergyVsN_G(N_k, N_b, potential):
    N_GValues = np.linspace(0,100,1)
    for Ng in(N_GValues):
        ek, ck = solveSchrodinger(Ng, N_k, N_b, potential)
    del ck
    plt.plot(ek, Ng)
    plt.show()    
    return 



"""Function demonstrating the effect the Threshold sb has on the Eigenvalues obtained"""
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



#IMPROVED BELOW
"""Function demonstrating the relationship between the time taken to obtain 
solutions with respect to the optimal Basis implementation and the Threshold sb"""
def timePlotVaryingSb(N_b, N_k, ck, potential, kList):
    N = N_b
    sbValues = np.linspace(0.5,0,100)
    sbList = []
    timeList = []
    for sb in sbValues:
        OB_bi = optimalBasis(sb, N_b, N_k, ck)
        k0 = calculatek0(OB_bi, potential)
        k1 = calculatek1(OB_bi, potential)
        VLoc = calculateVLoc(OB_bi, potential)
        startTime = time.time()
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




"""Function demonstrating the relationship between the Threshold value sb and the 
difference in Eigenvalues obtained regarding the respective approaches implemented """
def sbEffectOnPrecision(N_G, N_k, N_b, potential, N):
    sbList = []
    maxEigList = []
    sbValues = [0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]
    sb = 0
    for sb in sbValues:
        difference = differenceInEigenvalues(sb, N_G, N_k, N_b, potential, N)
        sbList.append(sb)
        maxEigList.append(difference)
        sb += 1
    sbArray = np.array(sbList)
    eigArray = np.array(maxEigList)
    plt.xlabel("Maximum difference between eigenvalues obtained comparing SS & IH")
    plt.ylabel("sb Value")
    plt.plot(eigArray, sbArray, 'b')
    plt.show()
    



"""Function demonstrating the relationship between the the number of k-points 
being considered and the computational cost of obtaining solutions to the 
Schrodinger Equation with respect to the standard approach, that is, 
with respect to the standard Basis"""
def kpointsVsTimeSS(N_G, N_b, potential):
    NKValues = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    timeList = []
    NKList = []
    for NK in NKValues:
        result = standardTimeForEk(N_G, NK, N_b, potential)
        NKList.append(NK)
        timeList.append(result)
    NKArray = np.array(NKList)
    timeArray = np.array(timeList) 
    plt.xlabel("Computation time to obtain solutions for SS")
    plt.ylabel("Number of k-points (N_k) being considered")   
    plt.plot(timeArray, NKArray, 'r')
    #plt.show()



"""Function that takes the plot demonstrating the relationship between the number of 
k-points being considered and the computational cost of obtaining solutions
with respect to the standard Basis implementation, and repeats this plot 100
times to obtain an average for such a relationship, as the underlying plot
will vary slightly each time it is ran"""
def averagePlotSS(N_G, N_b, potential):
    i = 0
    for i in range(0, 100):
        average = kpointsVsTimeSS(N_G, N_b, potential)
        i += 1
    plt.show()    
    return average



"""Function that demonstrates the relationship between the number of k-points being 
considered and the computational cost of obtaining solutions to the Schrodinger 
Equation with respect to the Optimal Basis implementation"""
def kpointsVsTimeIHEENEW(OB_bi, k0, k1, VLoc, N, potential):
    NKValues = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    timeList = []
    NKList = []
    for NK in NKValues:
        result = optimisedTimeForEkEENEW(OB_bi, k0, k1, VLoc, N, potential, NK)
        NKList.append(NK)
        timeList.append(result)
    NKArray = np.array(NKList)
    timeArray = np.array(timeList) 
    plt.xlabel("Computation time to obtain solutions for IH")
    plt.ylabel("Number of k-points (N_k) being considered")   
    plt.plot(timeArray, NKArray, 'b')
    #plt.show()



"""Function that takes the plot demonstrating the relationship between the number
of k-points being considered and the computational cost of obtaining solutions 
with respect to the Optimal Basis implementation, and repeats the plot 100 times
to achieve an average of such a relationsip, as the underlying plot will vary
each time it is ran"""
def averagePlotIHEE(OB_bi, k0, k1, VLoc, N, potential):
    i = 0
    for i in range(0, 100):
        average = kpointsVsTimeIHEENEW(OB_bi, k0, k1, VLoc, N, potential)
        i += 1
    plt.show()    
    return average



"""Function that performs the same task as the function described above, but also 
plots the line of best fit (average) of all the plots, to give a more accurate 
representation of the relationship between k-points and the computational 
cost of achieving the results"""
def averagePlotIHEELineOfBestFit(OB_bi, k0, k1, VLoc, N, potential):
    i = 0
    for i in range(0, 100):
        NKArray, timeArray = kpointsVsTimeIHEENEW(OB_bi, k0, k1, VLoc, N, potential)
        plt.plot(timeArray, NKArray, 'b')
        if i == 99:
            a, b = np.polyfit(timeArray, NKArray, 1)
            plt.plot(timeArray, a*timeArray+b, 'y')
            i += 1  
    plt.xlabel("Computation time to obtain solutions for IH")
    plt.ylabel("Number of k-points (N_k) being considered")   
    plt.show()    
    return 






