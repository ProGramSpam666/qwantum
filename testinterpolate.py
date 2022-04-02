from quantum.interpolate import interpolateHamiltonian, calculatek0,calculatek1,calculateVLoc
from quantum.qobj import Qobj
from quantum.utils import kvec



qobj = Qobj()
#qobj = quantum.qobj.Qobj()

#COMPLETE
def testCalculateK0():
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    result = calculatek0(OB_bi, potential)
    return result
#print("------------K0-------------")
#print(testCalculateK0())    


def testQuantumCalculatek0():
    result = qobj.getk0()
    return result
#print(testQuantumCalculatek0())


#COMPLETE
def testCalculateK1():
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    result = calculatek1(OB_bi, potential)
    return result
#print("------------K1-------------")
#print(testCalculateK1())


#COMPLETE
def testCalculateVLoc():
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    result = calculateVLoc(OB_bi, potential)
    return result 
#print("------------VLoc-----------")
#print(testCalculateVLoc())


#----------------------TESTING OPTIMISED EK AND BAND STRUCTURE USING QUANTUM OBJECT-----------
def testInterpolateHamiltonian():
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    kList = [1,2,3,4,5,6,7,8,9,10]
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







=======
    N_k = qobj.getN_K()
    a = potential.parms["lattice"]
    k0 = calculatek0(OB_bi, potential)
    k1 = calculatek1(OB_bi, potential)
    VLoc = calculateVLoc(OB_bi, potential)
    kList = []
    for i in range(N_k):
        kList.append(kvec(i,a,N_k))
    eigenEnergies = interpolateHamiltonian(OB_bi, kList,k0, k1, VLoc, N_b)
    return eigenEnergies
#print("-----Interpolate Hamiltonian--------")    
#print(testInterpolateHamiltonian())    


#-----------OPTIMISED METHOD OF OBTAINING INTERPOLATED HAMILTONIAN------
def testInterpolateHamiltonian():
    eigenEnergies = qobj.getInterpolateHamiltonian()
    return eigenEnergies #obtains arrays of eigenenergies for each k point in N_k 
print("-----Interpolate Hamiltonian--------")    
print(testInterpolateHamiltonian())  



>>>>>>> Stashed changes
=======
    N_k = qobj.getN_K()
    a = potential.parms["lattice"]
    k0 = calculatek0(OB_bi, potential)
    k1 = calculatek1(OB_bi, potential)
    VLoc = calculateVLoc(OB_bi, potential)
    kList = []
    for i in range(N_k):
        kList.append(kvec(i,a,N_k))
    eigenEnergies = interpolateHamiltonian(OB_bi, kList,k0, k1, VLoc, N_b)
    return eigenEnergies
#print("-----Interpolate Hamiltonian--------")    
#print(testInterpolateHamiltonian())    


#-----------OPTIMISED METHOD OF OBTAINING INTERPOLATED HAMILTONIAN------
def testInterpolateHamiltonian():
    eigenEnergies = qobj.getInterpolateHamiltonian()
    return eigenEnergies #obtains arrays of eigenenergies for each k point in N_k 
print("-----Interpolate Hamiltonian--------")    
print(testInterpolateHamiltonian())  



>>>>>>> Stashed changes
=======
    N_k = qobj.getN_K()
    a = potential.parms["lattice"]
    k0 = calculatek0(OB_bi, potential)
    k1 = calculatek1(OB_bi, potential)
    VLoc = calculateVLoc(OB_bi, potential)
    kList = []
    for i in range(N_k):
        kList.append(kvec(i,a,N_k))
    eigenEnergies = interpolateHamiltonian(OB_bi, kList,k0, k1, VLoc, N_b)
    return eigenEnergies
#print("-----Interpolate Hamiltonian--------")    
#print(testInterpolateHamiltonian())    


#-----------OPTIMISED METHOD OF OBTAINING INTERPOLATED HAMILTONIAN------
def testInterpolateHamiltonian():
    eigenEnergies = qobj.getInterpolateHamiltonian()
    return eigenEnergies #obtains arrays of eigenenergies for each k point in N_k 
print("-----Interpolate Hamiltonian--------")    
print(testInterpolateHamiltonian())  



>>>>>>> Stashed changes



