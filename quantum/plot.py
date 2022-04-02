import numpy as np 
import matplotlib.pyplot as plt
from quantum.utils import kvec, Gvec



def plotBand(ek,potential,symbol):
    a = potential.parms["lattice"]
    [Nk,Nb] = np.shape(ek)
    #print([Nk, Nb])
    #print("--------ek-----------")
    #print(ek)
    #print("-------Nk-----")
    #print(Nk)
    k = np.zeros(Nk)
    
    for ik in range(Nk):
        k[ik]=kvec(ik,a,Nk)
        
    for ib in range(Nb):
        plt.plot(k,ek[:,ib],symbol)
    plt.ylabel("Energy (ev)")  
    plt.xlabel("wave vector k")  
    plt.show()
    return 


def plotOptimalBasisSizeAgainstCkSize(optimalBasisSize, ckSize, symbol):
    plt.plot(optimalBasisSize, ckSize, symbol)
    plt.show()

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
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


def OBPlotFun(ik, E, OB_bi, Ncell, Npoints, potential, symbol, shift):
    a = potential.parms["lattice"]
    [NG,Nk,Nb] = np.shape(OB_bi)
    N = int(NG/2-1) 
    x, U = potential.v(Ncell, Npoints)
    plt.plot(x,U)
    for ib in range(Nb):
        phi = np.full(len(x),shift*E[ik,ib]) #shift - bloch?
        #shift allows to adjust to improve visualisation
        for ig in range(NG):
            phi = phi + OB_bi[ig,ik,ib]*np.exp(1j*(kvec(ik,a,Nk)-Gvec(ig-N,a))*x)
        plt.plot(x,phi,symbol)
    plt.show()
    return 

