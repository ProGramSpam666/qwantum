import numpy as np
from quantum.dielectricplot import standardDielectricPlotImaginary
from quantum.velocityOp import standardVelocity
from quantum.dielectric import dielectricFunc
from quantum.qobj import Qobj


qobj = Qobj()

def testStandardDielectricPlotImaginary():
    numberOccupied = 2
    N_b = qobj.getN_B()
    energyRange = np.linspace(0,180,200)
    potential = qobj.getPotential()
    ck = qobj.getCk()
    ek = qobj.getEk()
    damp = 0.1
    stanvel = standardVelocity(potential, ck)
    standardDielectricPlotImaginary( N_b, ek, damp, energyRange, stanvel, numberOccupied)
    return 
print(testStandardDielectricPlotImaginary())






