from quantum.QobjManager import QobjManager
from quantum.qobj import Qobj

manager = QobjManager()
qobj1 = Qobj()
qobj2 = Qobj()

qobj1.setParms(N_K=50)
qobj2.setParms(N_K=200)
print(qobj1.getParms())
print(qobj2.getParms())
manager.addQobj(qobj1)
manager.addQobj(qobj2)

manager.plotBands()