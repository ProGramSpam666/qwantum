from quantum.qobj import Qobj
from quantum.utils import OB_bix, phi



qobj = Qobj()

#OB_bi, a, potential, Ncell, Npoints
def testOB_bix():
    OB_bi = qobj.getOptimalBasis()
    potential = qobj.getPotential()
    a = potential.parms["lattice"]
    Ncell = 3
    Npoints = 10
    OB_bixresult = OB_bix(OB_bi, a, potential, Ncell, Npoints)
    return OB_bixresult
print(testOB_bix())


def testPhi():
    N_b = qobj.getN_B()
    OB_bi = qobj.getOptimalBasis()
    potential = qobj.getPotential()
    a = potential.parms["lattice"]
    Ncell = 3
    Npoints = 10
    Phi = phi(N_b,OB_bi, a, potential, Ncell, Npoints)
    return Phi
#print(testPhi())




