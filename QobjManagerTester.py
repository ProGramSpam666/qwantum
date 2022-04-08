from quantum.QobjManager import QobjManager
from quantum.qobj import Qobj

manager = QobjManager()

qobj1 = Qobj()
qobj2 = Qobj()

manager.addQobj(qobj1)
manager.addQobj(qobj2)

qobj1.setParms(N_B = 6)
qobj2.setParms(N_B = 8)


manager.plotBands()


