from quantum.gettime import differenceInTimeVaryingSb
from quantum.gettime import standardTimeForEk, optimisedTimeForEk, differenceInTimeForObtainingEkSPECIFIC, differenceInTimeForObtainingEk
from quantum.qobj import Qobj
import numpy as np

qobj = Qobj()


N_G = qobj.getN_G()
N_k = qobj.getN_K()
N_b = qobj.getN_B()
potential = qobj.getPotential()
OB_bi = qobj.getOptimalBasis()
kList = qobj.getKList()
k0 = qobj.getk0()
k1 = qobj.getk1()
VLoc = qobj.getVLoc()
N = qobj.getN_B()
ck = qobj.getCk()



def testTimesForEigenvaluesSPECIFIC():
    resultDifference = differenceInTimeForObtainingEkSPECIFIC(N_G, N_k, N_b, potential, OB_bi, kList, k0, k1, VLoc, N)
    return resultDifference
print(testTimesForEigenvaluesSPECIFIC())    



def varyingSbEk():
    differenceList = []
    sbValues = np.linspace(0,1,100)
    for sb in (sbValues):
        qobj.setSb(sb)
        resultDifference = differenceInTimeForObtainingEk(N_G, N_k, N_b, potential, OB_bi, kList, k0, k1, VLoc, N)
        differenceList.append(resultDifference)
    differenceArray = np.array(differenceList)    
    return differenceArray
#print(varyingSbEk())









#QUANTUM OBJECT IMPLEMENTATION TESTING

#Testing Time to get Eigenvalues using SS
def testTimeEkSS():
    res = qobj.getEkTimeSolveSchrodinger()
    print("----Time Elapsed using solveSchrodinger()----")
    print("solveSchrodinger: " + str(res))
    return
#print(testTimeEkSS())    


#Testing Time to get Eigenvalues using IH
def testTimeEkIH():
    res = qobj.getEkTimeInterpolateHamiltonian()
    print("----Time Elapsed using interpolateHamiltonian()----")
    print("interpolateHamiltonian: " + str(res))
    return
#print(testTimeEkIH())


#Testing difference in time to obtain Eigenvalues between SS and IH
def testDifferenceInTimeEk():
    res = qobj.getDifferenceTimeForEk()
    print("----Time difference in obtaining EigenValues----")
    print("Difference: " + str(res))
    return 
#print(testDifferenceInTimeEk())



#Testing difference in Time as sb varies 
def testDifferenceInTimeVaryingSb():
    res = differenceInTimeVaryingSb(N_b, N_k, ck, potential, kList)
    return res
#print(testDifferenceInTimeVaryingSb())



