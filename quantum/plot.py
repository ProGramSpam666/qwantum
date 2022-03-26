import numpy as np 
import matplotlib.pyplot as plt
from quantum.optimalbasis import optimalBasis
from quantum.utils import kvec, Gvec

def plotBand(ek,potential,symbol):
    a = potential.parms["lattice"]
    [Nk,Nb] = np.shape(ek)
    print([Nk, Nb])
    print("--------ek-----------")
    print(ek)
    print("-------Nk-----")
    print(Nk)
    k = np.zeros(Nk)
    for ik in range(Nk):
        k[ik]=kvec(ik,a,Nk)
        print(k[ik])
    for ib in range(Nb):
        plt.plot(k,ek[:,ib],symbol)
    plt.show()
    return 


def plotOptimalBasisSizeAgainstCkSize(optimalBasisSize, ckSize, symbol):
    plt.plot(optimalBasisSize, ckSize, symbol)
    plt.show()

""" def plotFun(ik,ek,ck,Ncell,Npoints,potential,symbol,shift):
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
    return """


def plotFun(ik,ek,ck,Ncell,Npoints,potential,symbol,shift):
    a = potential.parms["lattice"]
    [NG,Nk,Nb] = np.shape(ck)
    print("-----------ck------------")
    print(ck)
    print("------shape(ck)--------")
    print(np.shape(ck))
    print("----------[NG, Nk, Nb]---------")
    print([NG, Nk, Nb])
    N = int(NG/2-1) 
    print("-----------N-----------")
    print(N)
    x, U = potential.v(Ncell, Npoints)
    print("-------x--------")
    print(x)
    print("-------U--------")
    print(U)
    plt.plot(x,U)
    for ib in range(Nb):
        phi = np.full(len(x),shift*ek[ik,ib]) 
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



