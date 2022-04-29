import numpy as np
from quantum.dielectric import dielectricFunc
from quantum.velocityOp import standardVelocity, interpolatedVelocity
from quantum.qobj import Qobj

qobj = Qobj()




def testDielectricFunc():
    numberOccupied = 1
    N_b = qobj.getN_B()
    ek = qobj.getEk()
    damp = 0.001
    w = 10 + 1j*damp
    potential = qobj.getPotential()
    ck = qobj.getCk()
    stanvel = standardVelocity(potential, ck)
    result = dielectricFunc( N_b, ek, damp, w, stanvel, numberOccupied )
    print("-------Standard Dielectric Function----------")
    return result
print(testDielectricFunc())




def testOptimalDielectricFunc():
    numberOccupied = 1
    N_b = qobj.getN_B()
    Eigen, Eigenvec = qobj.interpolateHamiltonianEC()
    w = 10 + 1j*0.001
    potential = qobj.getPotential()
    k1 = qobj.getk1()
    interpolatedVel = interpolatedVelocity(potential, Eigenvec, k1)
    result = dielectricFunc(N_b, Eigen, w, interpolatedVel, numberOccupied )
    print("-------Optimal Dielectric Function------")
    return result
print(testOptimalDielectricFunc())







