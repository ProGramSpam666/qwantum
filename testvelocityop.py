import numpy as np
from quantum.qobj import Qobj
from quantum.velocityOp import standardVelocity, interpolatedVelocity
from quantum.interpolate import calculatek1, interpolateHamiltonianEE
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum import potential as pt
from quantum.utils import kvec


qobj = Qobj()

#TEST COMPARISON

def testStandardVelocity():
    potential = qobj.getPotential()
    ck = qobj.getCk()
    result = standardVelocity( potential, ck)
    return result
#print("---------Standard Velocity------")
#print(testStandardVelocity())

def testInterpoaltedVelocity():
    k1 = qobj.getk1()
    OBck = qobj.getOBck()
    potential = qobj.getPotential()
    result = interpolatedVelocity(potential, OBck, k1)
    return result
#print("---------Interpolated Velocity------")
#print(testStandardVelocity())







#TEST COMPARISON QUANTUM OBJECT APPROACH

def testStanVelQ():
    result = qobj.getStandardVelocityOperator()
    return result
print("--STANDARD--")
print(testStanVelQ)

def testInterVelQ():
    result = qobj.getInterpolatedVelocityOperator()
    return result
print("--INTERPOALTED--")
print(testInterVelQ())




