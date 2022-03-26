import numpy as np 
from quantum.matrix import fillmatrix
from quantum.interpolate import interpolateHamiltonian


def solveSchrodinger(N_G,N_k,N_b,potential):#iterates k-point by k-point
    #e and c are NOT dependent on ik, however, we alter to make e,c k-dependent
    ek = np.zeros((N_k,N_b)) #energy band
    ck = np.zeros((2*N_G+1,N_k,N_b),dtype=np.complex_)#eigenstate, is a vector with dimension
    for ik in range(N_k):
        M=fillmatrix(ik,N_G,N_k,potential)
        [e,c]=np.linalg.eigh(M) #because orthogonal basis standard eigenvalue problem
        print([e,c])
        ek[ik,0:N_b] = e[0:N_b]
        ck[:,ik,0:N_b] = c[:,0:N_b]
        
    return ek,ck


def solveSchroedinger1(N_G,N_k,N_b,potential):#iterates k-point by k-point
    #e and c are NOT dependent on ik, however, we alter to make e,c k-dependent
    ek = np.zeros((N_k,N_b)) #energy band
    ck = np.zeros((2*N_G+1,N_k,N_b),dtype=np.complex_)#eigenstate, is a vector with dimension
    for ik in range(N_k): 
        M=fillmatrix(ik,N_G,N_k,potential)
        [e,c]=np.linalg.eigh(M) #because orthogonal basis standard eigenvalue problem
        
        ek[ik,0:N_b] = e[0:N_b]
        ck[:,ik,0:N_b] = c[:,0:N_b]
        return ck



#--------------Diagonalising Hamiltonian--------------------------



def diagonaliseHamiltonian(OB_bi, N_k, N_b, N_G, potential):
    #a = potential.parms["lattice"]
    #Nbasis = OB_bi.shape[1]
    optimalE = np.zeros((N_k, N_b))
    #optimalC = np.zeros((Nbasis, Nbasis), dtype = np.complex_)
    optimalC = np.zeros((2*N_G+1,N_k,N_b), dtype = np.complex_)
    for ik in range(N_k):

        M = interpolateHamiltonian(OB_bi, potential, N_k)
        [ee, cc] = np.linalg.eigh(M)
        optimalE[ik,0:N_b] = ee[0:N_b]
        #optimalC[:,0:N_b] = cc[:,0:N_b] ????
        optimalC[:,ik,0:N_b] = cc[:,0:N_b]

    return ee,cc



    




