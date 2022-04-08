from quantum.QobjManager import QobjManager
from quantum.qobj import Qobj

manager = QobjManager()
qobj1 = Qobj()
qobj2 = Qobj()


print(QobjManager.timeDiffSolveSchrodingerInterpolateHamiltonian(qobj1))
