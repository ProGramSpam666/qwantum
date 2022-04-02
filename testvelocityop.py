import numpy as np
from quantum.qobj import Qobj
from quantum.velocityOp import kDepVelOperatorOB
from quantum.interpolate import calculatek1
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum import potential as pt
from quantum.utils import kvec


qobj = Qobj()

#-------------------QUANTUM OBJECT METHOD OF TESTING K-VELOCITY OPERATOR---------
def testVelocityOperator():
    potential = qobj.getPotential()
    a = potential.parms["lattice"]
    N_b = qobj.getN_B()
    OB_bi = qobj.getOptimalBasis()
    kList = qobj.getKList()
    ck = qobj.getCk()
    k1 = calculatek1(OB_bi, a)
    result = kDepVelOperatorOB(N_b, k1, OB_bi, kList, ck)
    return result 
print("---------Quantum Object Method determining Velocity Operator--------")
print(testVelocityOperator())

#TEST COMPARISON


