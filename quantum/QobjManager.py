from numpy import ndarray, shape
from quantum.qobj import Qobj
from quantum.utils import timerFloat
import matplotlib.pyplot as plt



class QobjManager:

    # CONSTRUCTOR
    def __init__(self):
        self.__data = list() # stores Qobj objects

    # GETTERS
    """returns Qobj at data[index] if valid"""
    def getQobj(self, index:int)->Qobj:
        if 0<=index and index<len(self.__data):
            return self.__data[index]

    def getQobjList(self)->list[Qobj]:
        return self.__data

    """returns number of objects in data (length of qobj list)"""
    def getLen(self)->int:
        return len(self.__data)

    # METHODS
    """adds Qobj to data"""
    def addQobj(self, qobj: Qobj)->None:
        if (type(qobj) is Qobj and qobj!=None):
            self.__data.append(qobj)

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

    """Returns list containg band structure arrays for each qobj in data - calculated with ek from solve schrodinger"""
    def schrodingerBands(self)->list[ndarray]:
        bands = list()
        qobjList = self.getQobjList()
        for qobj in qobjList:
            bands.append(qobj.schrodingerBandStructure())
        return bands

    """Returns list containing band structure arrays for each qobj in data - calculated with ek from interpolate hamiltonian"""
    def interpolatedBands(self)->list[ndarray]:
        bands = list()
        qobjList = self.getQobjList()
        for qobj in qobjList:
            bands.append(qobj.interpolatedBandStructure())
        return bands

    def plotBands(self):
        schrodingerBandsList: list = self.schrodingerBands()
        interpolatedBandsList: list = self.interpolatedBands()
        for schrodingerBands in schrodingerBandsList:
            for band in schrodingerBands:
                plt.plot(band[0], band[1], "r-")
        for interpolatedBands in interpolatedBandsList:
            for band in interpolatedBands:
                plt.plot(band[0], band[1], "b--")
        plt.show()



    

        