from quantum.big0 import getOrderPlot
from quantum.qobj import Qobj

qobj = Qobj()

#N_b, N_k, ck, potential, kList
def testGetOrderPlot():
    sb = qobj.getSb()
    N_b = qobj.getN_B()
    N_k = qobj.getN_K()
    ck = qobj.getCk()
    potential = qobj.getPotential()
    kList = qobj.getKList()
    result = getOrderPlot(N_b, N_k, ck, potential, kList)
    return result
print(testGetOrderPlot())


