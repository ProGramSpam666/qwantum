import numpy as np
from quantum.qobj import Qobj
from quantum.velocityOp import kDepVelOperatorOB, standardVelocity
from quantum.interpolate import calculatek1
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum import potential as pt
from quantum.utils import kvec


qobj = Qobj()

#TEST COMPARISON

#-------------------QUANTUM OBJECT METHOD OF TESTING K-VELOCITY OPERATOR---------
def testVelocityOperator():
    potential = qobj.getPotential()
    a = potential.parms["lattice"]
    N_b = qobj.getN_B()
    OB_bi = qobj.getOptimalBasis()
    kList = qobj.getKList()
    ck = qobj.getCk()
    k1 = qobj.getk1()
    result = kDepVelOperatorOB(N_b, k1, OB_bi, kList, ck)
    return result, k1
#print("---------Quantum Object Method determining Velocity Operator--------")
#print(testVelocityOperator())



def testStandardVelocity():
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    potential = qobj.getPotential()
    ck = qobj.getCk()
    result = standardVelocity(N_k, N_b, potential, ck)
    return result
print("---------Standard Velocity------")
print(testStandardVelocity())







