import numpy as np
from quantum.dielectric import dielectricFunc
from quantum.qobj import Qobj

qobj = Qobj()

#parameters = N_k, N_b, bi_out, ek, q, w
def testDielectricFunc():
    N_k = qobj.getN_K()
    N_b = qobj.getN_B()
    OB_bi = qobj.getOptimalBasis()
    ek = qobj.getEk()
    q = 2
    w = 3
    result = dielectricFunc(N_k, N_b, OB_bi, ek, q, w)
    return result
print("-------Dielectric Function----------")
print(testDielectricFunc())


