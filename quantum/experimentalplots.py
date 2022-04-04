import numpy as np
from quantum.qobj import Qobj
from quantum.optimalbasis import optimalBasis
import matplotlib.pyplot as plt
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.schrodinger import solveSchrodinger
from quantum.utils import kvec

qobj = Qobj()

def sbEffectOnSize():
    myListOb = []
    myListSb = []
    sbValues = np.linspace(0,1,250)
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    ck = qobj.getCk()
    for s_b in sbValues:
        
        getOptimalBasis = optimalBasis(s_b, N_b, N_k, ck) 
        sizeOb = getOptimalBasis.size
        myListOb.append(sizeOb)
        myListSb.append(s_b)

    myresultOb = np.array(myListOb)
    myresultSb = np.array(myListSb)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Sb value")
    plt.plot(myresultOb, myresultSb, 'g')
    plt.show()



def varyingNbOBPlot():
    i = 0
    symbolList = ["r-", "b-", "g-", "k-", "y-", "p-", "c-"]
    qobj = Qobj()
    for N_B in range(3, 7):
        qobj.setN_B(N_B)
        sbEffectOnSize(qobj, symbolList[i])
        i += 1
    plt.show()


def optimalBasisVsCk():
    myListOb = []
    myListCk = []
    sbValues = np.linspace(0,1,250)
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    ck = qobj.getCk()
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


def ekVsE():
    N_k = qobj.getN_K()
    N_G = qobj.getN_G()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    k0 = qobj.getk0()
    k1 = qobj.getk1()
    VLoc = qobj.getVLoc()
    kList = qobj.getKList()
    E = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N_b)
    ek, ck = solveSchrodinger(N_G, N_k, N_b, potential )
    del ck
    plt.xlabel("ek")
    plt.ylabel("E")
    plt.plot(ek, E , 'b')
    plt.show()    


def EnergyVsN_G():
    N_k = qobj.getN_K()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    N_GValues = np.linspace(0,100,1)
    for N_G in(N_GValues):
        Ng = qobj.setN_G(N_G)
        ek, ck = solveSchrodinger(Ng, N_k, N_b, potential)
    del ck
    plt.plot(ek, Ng)
    plt.show()    
    return 


def sbEffectOnEigenvalues():
    myListSb = []
    sbValues = np.linspace(0,1,250)
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    ck = qobj.getCk()
    kList = qobj.getKList()
    k0 = qobj.getk0()
    k1= qobj.getk1()
    VLoc = qobj.getVLoc()
    for s_b in sbValues:
        OB_bi = optimalBasis(s_b, N_b, N_k, ck) 
        myListSb.append(s_b)
    E = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N_b )
    myresultSb = np.array(myListSb)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Sb value")
    plt.plot(E, myresultSb, 'g')
    plt.show()
    
    
def differenceInEigenvaluesVsSb():
    return 
