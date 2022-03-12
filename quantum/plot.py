import numpy as np 
import matplotlib.pyplot as plt
from quantum.qobj import Qobj
from quantum.utils import kvec, Gvec
#from testbasis import effectVaryingSbOnOptimalBasis

def plotBand(ek,potential,symbol):
    a = potential.parms["lattice"]
    [Nk,Nb] = np.shape(ek)
    k = np.zeros(Nk)
    
    for ik in range(Nk):
        k[ik]=kvec(ik,a,Nk)
        
    for ib in range(Nb):
        plt.plot(k,ek[:,ib],symbol)
        
    plt.show()
    return 


def plotOptimalBasisSizeAgainstCkSize(optimalBasisSize, ckSize, symbol):
    plt.plot(optimalBasisSize, ckSize, symbol)
    plt.show()

def plotFun(ik,ek,ck,Ncell,Npoints,potential,symbol,shift):
    a = potential.parms["lattice"]
    [NG,Nk,Nb] = np.shape(ck)
    N = int(NG/2-1) #check dimension ck
    x, U = potential.v(Ncell, Npoints)
    plt.plot(x,U)
    
    for ib in range(Nb):
        phi = np.full(len(x),shift*ek[ik,ib]) #shift - bloch?
        #shift allows to adjust to improve visualisation
        
        for ig in range(NG):
            phi = phi + ck[ig,ik,ib]*np.exp(1j*(kvec(ik,a,Nk)-Gvec(ig-N,a))*x)
        plt.plot(x,phi,symbol)
    plt.show()
    return

def OBplotFun(ik,ek,bi_out,Ncell,Npoints,potential,symbol,shift):
    a = potential.parms["lattice"]
    [NG,Nk,Nb] = np.shape(bi_out)
    N = int(NG/2-1) #check dimension ck
    x, U = potential.v(Ncell, Npoints)
    plt.plot(x,U)
    
    for ib in range(Nb):
        phi = np.full(len(x),shift*ek[ik,ib]) #shift - bloch?
        #shift allows to adjust to improve visualisation
        
        for ig in range(NG):
            phi = phi + bi_out[ig,ik,ib]*np.exp(1j*(kvec(ik,a,Nk)-Gvec(ig-N,a))*x)
        plt.plot(x,phi,symbol)
    plt.show()
    return

""" def plotSbEffect():
    newlist = effectVaryingSbOnOptimalBasis()
    for sb in range(1,1000, 10):
        num = 1/sb
        for item in newlist:
            sizevalue = item 
        plt.plot(num, sizevalue)
    plt.show     """

""" def plotSbEffect1():
    qobj = Qobj()
    ob = qobj.optimalBasis
    np.size(ob)
    newlist = effectVaryingSbOnOptimalBasis
    plt.plot(newlist, ob)
    """

""" def plotSbEffect1():
    listUsed = []
    newlist = effectVaryingSbOnOptimalBasis
    listUsed.append(newlist)
    xSb = np.array(range(listUsed))
    ySize = np.array(listUsed)
    plt.figure(xSb, ySize) """


""" def plotSbEffect1():
    resultListOb = effectVaryingSbOnOptimalBasis()
    for sb in range(1,1000, 10):
        numlist = []
        num = 1/sb
        numlist.append(num)
    xSb = np.array(numlist)
    ySize = resultListOb
    plt.plot(ySize, xSb) """









    
















    
