import numpy as np
from quantum.dielectricplot import dielectricPlotImaginary
from quantum.dielectricplot import dielectricPlotReal
from quantum.velocityOp import standardVelocity, interpolatedVelocity
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
    dielectricPlotImaginary(N_b, ek, damp, energyRange, stanvel, numberOccupied)
    return 
print(testStandardDielectricPlotImaginary())



def testStandardDielectricPlotReal():
    numberOccupied = 2
    N_b = qobj.getN_B()
    energyRange = np.linspace(0,180,200)
    potential = qobj.getPotential()
    ck = qobj.getCk()
    ek = qobj.getEk()
    damp = 0.1
    stanvel = standardVelocity(potential, ck)
    dielectricPlotReal(N_b, ek, damp, energyRange, stanvel, numberOccupied)
    return
#print(testStandardDielectricPlotReal())




def testOptimalDielectricPlotImaginary():
    numberOccupied = 2
    N_b = qobj.getN_B()
    energyRange = np.linspace(0,180,200)
    potential = qobj.getPotential()
    k1 = qobj.getk1()
    E, OBck = qobj.getInterpolateHamiltonianEE()
    damp = 0.1
    velocity = interpolatedVelocity(potential, OBck, k1)
    dielectricPlotImaginary(N_b, E, damp, energyRange, velocity, numberOccupied)
    return 
#print(testOptimalDielectricPlotImaginary())  





def testOptimalDielectricPlotReal():
    numberOccupied = 2
    N_b = qobj.getN_B()
    energyRange = np.linspace(0,180,200)
    potential = qobj.getPotential()
    k1 = qobj.getk1()
    E, OBck = qobj.getInterpolateHamiltonianEE()
    damp = 0.1
    velocity = interpolatedVelocity(potential, OBck, k1)
    dielectricPlotReal(N_b, E, damp, energyRange, velocity, numberOccupied)
    return 
#print(testOptimalDielectricPlotReal())




