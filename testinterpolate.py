from quantum.interpolate import interpolateHamiltonian, calculatek0,calculatek1,calculateVLoc
from quantum import potential as pt
from quantum.qobj import Qobj

qobj = Qobj()
#qobj = quantum.qobj.Qobj()


def testCalculateK0():
    potential = qobj.getPotential()
    a = potential.parms["lattice"]
    OB_bi = qobj.getOptimalBasis()
    result = calculatek0(OB_bi, a)
    return result


def testCalculateK1():
    potential = qobj.getPotential()
    a = potential.parms["lattice"]
    OB_bi = qobj.getOptimalBasis()
    result = calculatek1(OB_bi, a)
    return result


def testCalculateVLoc():
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    result = calculateVLoc(OB_bi, potential)
    return result 


def testInterpolateHamiltonian():
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    kList = [1,2,3,4,5]
    result = interpolateHamiltonian(OB_bi, potential, kList)
    return result


print("------------K0-------------")
print(testCalculateK0())

print("------------K1-------------")
print(testCalculateK1())

print("------------VLoc-----------")
print(testCalculateVLoc())

print("------------Hamiltonian-------")
print(testInterpolateHamiltonian())






#------------------TEST Diagonalise Hamiltonain-----------------------



