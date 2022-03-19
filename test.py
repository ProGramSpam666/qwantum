import matplotlib.pyplot as plt
from quantum import optimalbasis
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasisGetOBBI
from quantum import potential as pt
from testbasis import effectVaryingSbOnOptimalBasisExp
from quantum.plot import plotToFindOptimalSb
import numpy as np
from quantum.qobj import Qobj
from quantum.interpolate import calculateVLoc
from quantum.potential import PotentialFactory as pf

def varyingNbOBPlot():
    i = 0
    symbolList = ["r-", "b-", "g-", "k-", "y-", "p-", "c-"]
    qobj = Qobj()
    for N_B in range(3, 7):
        qobj.setN_B(N_B)
        plotToFindOptimalSb(qobj, symbolList[i])
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



def testingVLoc():
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 0.2, "width" : 0.2 }
    ptl = pf.createPotential("sech", ptparms)
    obbi = getOB_bi()
    result = calculateVLoc(obbi, 3,5,7,ptl,3,10)
    return result


#print(getOB_bi())
print(testingVLoc())


#print(calculateVLoc(3,5,7,ptl,3,10))
#OB_bi, N_G, N_GPrime, N_GPrimePrime, potential, Ncell, Npoints


