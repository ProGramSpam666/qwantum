import matplotlib.pyplot as plt
from quantum import optimalbasis
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum import potential as pt
from testbasis import effectVaryingSbOnOptimalBasisExp
from quantum.plot import plotToFindOptimalSb
import numpy as np
from quantum.qobj import Qobj
from quantum.interpolate import calculateVLoc

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



print(calculateVLoc())


