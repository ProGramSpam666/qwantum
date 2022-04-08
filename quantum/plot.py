#File given from model to obtain plots for the band structure of the material
#with the eigenvalues determined from each approach (SS and IH).  Also to plot the
#corresponding wave functions (eigenvectors).



import numpy as np 
import matplotlib.pyplot as plt
from quantum.potential import Potential
from quantum.utils import kvec, Gvec


#Band Structure Array
def bandStructure(ek:np.ndarray,potential:Potential)->np.ndarray:
    a = potential.parms["lattice"]
    [Nk,Nb] = np.shape(ek)
    k = np.zeros(Nk)
    for ik in range(Nk):
        k[ik]=kvec(ik,a,Nk)  
    bands = []
    for ib in range(Nb):
        temp = np.array([k,ek[:,ib]])
        bands.append(temp)
    bands = np.asarray(bands)
    return bands


def plotBand(ek:np.ndarray, potential: Potential, symbol: str):
    a = potential.parms["lattice"]
    [Nk,Nb] = np.shape(ek)
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


