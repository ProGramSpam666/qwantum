from quantum.qobj import Qobj
import numpy as np

qobj = Qobj()

ob1 = qobj.optimalBasis()
print(ob1.size)
print(np.shape(ob1))
qobj.setSb(0.9)
ob2 = qobj.optimalBasis()
print(ob2.size)
print(np.shape(ob2))




