from quantum.qobj import Qobj
import numpy as np

def effectVaryingSbOnOptimalBasis():
    qobj = Qobj()
    myList = []
    for num in range(1,1000, 10):
        sb = 1/num
        qobj.setSb(sb)
        getOptimalBasis = qobj.optimalBasis()
        sizeOb = getOptimalBasis.size
        myList.append(sizeOb)
        myresult = np.array(myList)
    return myresult


print(effectVaryingSbOnOptimalBasis())


