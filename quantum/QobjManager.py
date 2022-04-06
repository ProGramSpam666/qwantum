from quantum.qobj import Qobj

class QobjManager:
    data = list[Qobj] # stores Qobj objects

    # CONSTRUCTOR
    def __init__(self):
        pass

    # GETTERS
    """returns Qobj at data[index] if valid"""
    def getQobj(self, index:int)->Qobj:
        if 0<=index and index<len(self.data):
            return self.data[index]


    """adds Qobj to data"""
    def addQobj(self, qobj: Qobj)->None:
        if (qobj!=None):
            self.data.append(qobj)

    

        