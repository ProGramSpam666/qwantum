from quantum.qobj import Qobj
from quantum.utils import timerFloat



class QobjManager:

    # CONSTRUCTOR
    def __init__(self):
        self.data = list() # stores Qobj objects

    # GETTERS
    """returns Qobj at data[index] if valid"""
    def getQobj(self, index:int)->Qobj:
        if 0<=index and index<len(self.data):
            return self.data[index]

    """returns number of objects in data (length of qobj list)"""
    def getLen(self)->int:
        return len(self.data)

    # METHODS
    """adds Qobj to data"""
    def addQobj(self, qobj: Qobj)->None:
        if (type(qobj) is Qobj and qobj!=None):
            self.data.append(qobj)

    """returns float containing function execution time"""
    @staticmethod
    @timerFloat #decorator wraps function in timer returns float time to execute function
    def timeSolveSchrodinger(qobj: Qobj)->float:
        qobj.solveSchrodinger()

    """Returns float containing function execution time"""
    @staticmethod
    @timerFloat
    def timeInterpolateHamiltonian(qobj: Qobj)->float:
        qobj.interpolateHamiltonian()

    """Returns float containing SS execution time - IH execution time"""
    @staticmethod
    def timeDiffSolveSchrodingerInterpolateHamiltonian(qobj: Qobj)->float:
        t1 = QobjManager.timeSolveSchrodinger(qobj)
        print(t1)
        t2 = QobjManager.timeInterpolateHamiltonian(qobj)
        print(t2)
        return t1 - t2

    

        