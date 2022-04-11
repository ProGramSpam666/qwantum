from quantum.QobjManager import QobjManager
from quantum.qobj import Qobj
import numpy as np

manager = QobjManager()

i = 0

while (i < 1):
    i+=0.001
    print(i)
    """ newQobj = Qobj()
    newQobj.setParms(sb=i)
    manager.addQobj(newQobj) """

#manager.plotSbAgainstOptimalBasisSize()

