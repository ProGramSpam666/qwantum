from quantum import potential
from quantum.experimentalplots import EnergyVsN_G, optimalBasisVsCk, sbEffectOnEigenvalues, sbEffectOnSize, ekVsE
from quantum.plot import plotFun, OBPlotFun
from quantum.interpolate import interpolateHamiltonian, calculatek0, calculatek1, calculateVLoc
from quantum.qobj import Qobj

qobj = Qobj()

print(sbEffectOnSize())

#print(optimalBasisVsCk())

#print(ekVsE()) #SAME PROBLEM AS TEST-INTERPOLATE!!!!!

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
