import numpy as np
from quantum.dielectric import dielectricFunc
import matplotlib.pyplot as plt


def standardDielectricPlotImaginary(N_b, ek, damp, energyRange, stanVel, numberOccupied):
    wlist  = [] 
    for w in energyRange:
        res = dielectricFunc(N_b, ek, damp, w, stanVel, numberOccupied)
        wlist.append(res.imag)  
    plt.xlabel("Energy")
    plt.ylabel("Imaginary part of Dielectric Function")
    plt.plot(energyRange, wlist, 'b')
    plt.show()    
    return 



def standardDielectricPlotReal():
    return 



def optimalDielectricPlotImaginary():
    return 



def optimalDielectricPlotReal():
    return 




