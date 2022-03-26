from math import pi
import numpy as np

def Gvec(m,a):
        return 2*pi*m/a


#m from -N_G to N_G+1       

def kgrid(a,N,Nk): #check Nk definition
    k = np.zeros(N)
    for ik in range(N):
        k[ik]=kvec(ik,a,Nk)
    return k


def kvec(i,a,N):
        return -pi/a + i*2*pi/a/(N-1)



def kinetic(i,m,a,N):
        return 0.5*(kvec(i,a,N) - Gvec(m,a))**2 




