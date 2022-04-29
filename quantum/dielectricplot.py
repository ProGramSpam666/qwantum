import numpy as np
from quantum.dielectric import dielectricFunc
import matplotlib.pyplot as plt



"""Function to obtain the relevant plot of the Imaginary part of the Dielectric Function
vs Energy"""
def dielectricPlotImaginary(N_b, ek, damp, energyRange, velocity, numberOccupied):
    wlist  = [] 
    for w in energyRange:
        res = dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied)
        wlist.append(res.imag)  
    plt.xlabel("Energy")
    plt.ylabel("Imaginary part of Dielectric Function")
    plt.plot(energyRange, wlist, 'b')
    plt.show()    
    return 

def dielectricPlotImaginaryArray(N_b, ek, damp, energyRange, velocity, numberOccupied):
    wlist  = [] 
    for w in energyRange:
        res = dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied)
        wlist.append(res.imag)   
    result = np.array(energyRange, wlist)
    plotting = np.asarray(result)
    return plotting    









"""Function to obtain the relevant plot of the Real part of the Dielectric Function
vs Energy"""
def dielectricPlotReal(N_b, ek, damp, energyRange, velocity, numberOccupied):
    wlist  = [] 
    for w in energyRange:
        res = dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied)
        wlist.append(res.real)  
    plt.xlabel("Energy")
    plt.ylabel("Real part of Dielectric Function")
    plt.plot(energyRange, wlist, 'r')
    plt.show()    
    return 

def dielectricPlotRealArray(N_b, ek, damp, energyRange, velocity, numberOccupied):
    wlist  = [] 
    for w in energyRange:
        res = dielectricFunc(N_b, ek, damp, w, velocity, numberOccupied)
        wlist.append(res.real)  
    result = np.array(energyRange, wlist)
    plotting = np.asarray(result)
    return plotting        














