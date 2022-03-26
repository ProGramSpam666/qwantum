import matplotlib.pyplot as plt
from quantum import optimalbasis
from quantum.schrodinger import solveSchrodinger, diagonaliseHamiltonian
from quantum.optimalbasis import optimalBasisGetOBBI
from quantum import potential as pt
from testbasis import effectVaryingSbOnOptimalBasisExp
import numpy as np
from quantum.qobj import Qobj
from quantum.interpolate import calculateVLoc
from quantum.potential import PotentialFactory as pf
from quantum.optimalbasis import optimalBasis


def varyingNbOBPlot():
    i = 0
    symbolList = ["r-", "b-", "g-", "k-", "y-", "p-", "c-"]
    qobj = Qobj()
    for N_B in range(3, 7):
        qobj.setN_B(N_B)
        sbEffectOnSize(qobj, symbolList[i])
        i += 1
    plt.show()


def gettingOptimalSb():
    qobj = Qobj()
    myListOb = []
    myListSb = []
    sb = np.linspace(0,1,100)
    for s_b in sb:
        qobj.setSb(s_b)
        getOptimalBasis = qobj.optimalBasis()
        sizeOb = getOptimalBasis.size
        myListOb.append(sizeOb)
        myListSb.append(s_b)
    newlistOB = []
    newlistSB = []
    for item in(myListOb) < 3:
        newlistOB.append(item)
        obtain = qobj.getSb()
        newlistSB.append(obtain)
    return newlistOB, newlistSB



def getOB_bi():
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 0.2, "width" : 0.2 }
    ptl = pf.createPotential("sech", ptparms)
    [ek,ck] = solveSchrodinger(3,100,5,ptl)
    del ek
    obbi = optimalBasisGetOBBI(0.001, 5, 100, ck)
    sizevalue = obbi.size
    return sizevalue


def sbEffectOnSize(symbol):
    qobj = Qobj()
    myListOb = []
    myListSb = []
    sbValues = np.linspace(0,1,250)
    N_b = qobj.getN_B
    N_k = qobj.getN_K
    ck = qobj.getCk
    for s_b in sbValues:
        
        getOptimalBasis = optimalBasis(s_b, N_b, N_k, ck) 
        sizeOb = getOptimalBasis.size
        myListOb.append(sizeOb)
        myListSb.append(s_b)

    myresultOb = np.array(myListOb)
    myresultSb = np.array(myListSb)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Sb value")
    plt.plot(myresultOb, myresultSb, symbol)
    plt.show()


def sbEffectOnNb():
    return 




#print(plotToFindOptimalSb('r'))




""" sb, N_b, N_k, ck, symbol
def testobplot():
    result1 = plotToFindOptimalSb(0.1)
    result2 = plotToFindOptimalSb()
 """




#print(getOB_bi())
#print(testingVLoc())


#print(calculateVLoc(3,5,7,ptl,3,10))
#OB_bi, N_G, N_GPrime, N_GPrimePrime, potential, Ncell, Npoints








def testingDiagonaliseHamil():
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 0.2, "width" : 0.2 }
    ptl = pf.createPotential("sech", ptparms)
    ek, ck = solveSchrodinger(11,70,4,ptl)
    del ek
    obbi = optimalBasis(0.1,4,70,ck)
    N_k = 70
    result = diagonaliseHamiltonian(obbi,N_k,4,11,ptl)
    print("----------Optimal Solve Schrodinger Result--------")
    return result


print(testingDiagonaliseHamil())

