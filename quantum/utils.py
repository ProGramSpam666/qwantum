from math import pi

def Gvec(m,a):
        return 2*pi*m/a

def kvec(i,a,N):
        return -pi/a + i*2*pi/a/(N-1)

def kinetic(i,m,a,N):
        return 0.5*(kvec(i,a,N) - Gvec(m,a))**2 


                