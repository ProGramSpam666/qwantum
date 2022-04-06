from quantum.gettime import differenceInTimeVaryingSb
from quantum.qobj import Qobj

qobj = Qobj()



#Testing Time to get Eigenvalues using SS
def testTimeEkSS():
    res = qobj.getEkTimeSolveSchrodinger()
    print("----Time Elapsed using solveSchrodinger()----")
    print("solveSchrodinger: " + str(res))
    return
print(testTimeEkSS())    



#Testing Time to get Eigenvalues using IH
def testTimeEkIH():
    res = qobj.getEkTimeInterpolateHamiltonian()
    print("----Time Elapsed using interpolateHamiltonian()----")
    print("interpolateHamiltonian: " + str(res))
    return
print(testTimeEkIH())



#Testing difference in time to obtain Eigenvalues between SS and IH
def testDifferenceInTimeEk():
    res = qobj.getDifferenceTimeForEk()
    print("----Time difference in obtaining EigenValues----")
    print("Difference: " + str(res))
    return 
print(testDifferenceInTimeEk())



#Testing difference in Time as sb varies 
def testDifferenceInTimeVaryingSb():
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    ck = qobj.getCk()
    potential = qobj.getPotential()
    kList = qobj.getKList()
    res = differenceInTimeVaryingSb(N_b, N_k, ck, potential, kList)
    return res
#print(testDifferenceInTimeVaryingSb())



