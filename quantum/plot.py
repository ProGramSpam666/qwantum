import numpy as np 
import matplotlib.pyplot as plt
from quantum import qobj
from quantum.qobj import Qobj
from quantum.utils import kvec, Gvec
from testbasis import effectVaryingSbOnOptimalBasis

def plotBand(ek,potential,symbol):
    a = potential.parms["lattice"]
    [Nk,Nb] = np.shape(ek)
    k = np.zeros(Nk)
    
    for ik in range(Nk):
        k[ik]=kvec(ik,a,Nk)
        
    for ib in range(Nb):
        plt.plot(k,ek[:,ib],symbol)
        
    #plt.show()
    #return 

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

def plotSbEffect1():
    sbList = []
    for sb in range(1,1000,10):
        sbvalues = 1/sb
        sbList.append(sbvalues)
        #print(sbList)
        sbArray = np.array(sbList)
        #print(sbArray)
    #return list of sb values, to plot x coord

    #now getting corresponding y values
    sizeArray = effectVaryingSbOnOptimalBasis() 
    #print(sizeArray)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Sb value")
    plt.plot(sizeArray, sbArray, 'r')
    plt.show()    


def plotToFindOptimalSb(qobj, symbol):
    #qobj = Qobj()
    myListOb = []
    myListSb = []
    sbValues = np.linspace(0,1,250)
    for s_b in sbValues:
        qobj.setSb(s_b)
        getOptimalBasis = qobj.optimalBasis()
        sizeOb = getOptimalBasis.size
        myListOb.append(sizeOb)
        myListSb.append(s_b)

    myresultOb = np.array(myListOb)
    myresultSb = np.array(myListSb)
    plt.xlabel("Size of Optimal Basis")
    plt.ylabel("Sb value")
    plt.plot(myresultOb, myresultSb, symbol)
    #plt.show()



#def plot
