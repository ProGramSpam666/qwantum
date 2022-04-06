from quantum import potential
from quantum.experimentalplots import EnergyVsN_G, optimalBasisVsCk, sbEffectOnEigenvalues 
from quantum.experimentalplots import sbEffectOnSize, ekVsE, timePlotVaryingSb
from quantum.plot import plotFun, OBPlotFun
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.qobj import Qobj

qobj = Qobj()

def testSbEffectOnSize():
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    ck = qobj.getCk()
    res = sbEffectOnSize(N_b, N_k, ck)
    return res
#print(testSbEffectOnSize())    


#print(optimalBasisVsCk())

#print(ekVsE())

def testOBPlotFun():
    ik = 2
    NCell = 3
    NPoints = 10
    shift = 2
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OB_bi = qobj.getOptimalBasis()
    kList = qobj.getKList()
    k0 = calculatek0(OB_bi, potential)
    k1 = calculatek1(OB_bi, potential)
    VLoc = calculateVLoc(OB_bi, potential)
    E = interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N_b)
    plotfun = OBPlotFun(ik, E, OB_bi, NCell, NPoints, potential, 'b', shift )
    return plotfun
#print(testOBPlotFun())


#print(EnergyVsN_G())

#print(sbEffectOnEigenvalues())



def testTimePlotVaryingSb():
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    ck = qobj.getCk()
    potential = qobj.getPotential()
    kList = qobj.getKList()
    res = timePlotVaryingSb(N_b, N_k, ck, potential, kList)
    return res
print(testTimePlotVaryingSb())    


