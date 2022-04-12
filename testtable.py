from quantum.qobj import Qobj
from quantum.table import differenceInVelocity

qobj = Qobj()

#print(differenceInEigenvalues())


def test():
    N_G = qobj.getN_G()
    N_k = qobj.getN_K()
    N_b = qobj.getN_B()
    potential = qobj.getPotential()
    OBck = qobj.getOBck()
    k1 = qobj.getk1()
    res = differenceInVelocity(N_G, N_k, N_b, potential, OBck, k1)
    return res
print(test())    

