import quantum.potential as pt
import quantum.schrodinger as schrodinger
import quantum.optimalbasis as optimalbasis
import quantum.plot as plot

class Qobj:

    # PRIVATE ATRRIBUTES
    __defaultPtParms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
    __defaultN_G = 8
    __defaultN_K = 100
    __defaultN_B = 5
    __defaultSb = 0.1
    __defaultPtType = "sech"
    
    
    # CONSTRUCTOR
    def __init__(self):
        self.parms = {
            "ptParms": self.get__defaultPtParms(),
            "N_G": self.get__defaultN_G(),
            "N_K": self.get__defaultN_K(),
            "N_B": self.get__defaultN_B(),
            "sb": self.get__defaultSb(),
            "ptType": self.get__defaultPtType()
        }
    

    # GETTERS
    def get__defaultPtParms(self):
        return self.__defaultPtParms
    def get__defaultN_G(self):
        return self.__defaultN_G
    def get__defaultN_K(self):
        return self.__defaultN_K
    def get__defaultN_B(self):
        return self.__defaultN_B
    def get__defaultSb(self):
        return self.__defaultSb
    def get__defaultPtType(self):
        return self.__defaultPtType
    def getPtParms(self):
        return self.parms["ptParms"]
    def getN_G(self):
        return self.parms["N_G"]
    def getN_K(self):
        return self.parms["N_K"]
    def getN_B(self):
        return self.parms["N_B"]
    def getSb(self):
        return self.parms["sb"]
    def getPtType(self):
        return self.parms["ptType"]
    def getPotential(self):
        return self.generatePotential(self.getPtType())
    def getEk(self):
        ek, ck = self.solveSchrodinger()
        del ck
        return ek
    def getCk(self):
        ek, ck = self.solveSchrodinger()
        del ek
        return ck
    def getOptimalBasis(self):
        return self.optimalBasis()
    
    
        
    # SETTERS
    def setPtParms(self, ptParms):
        self.parms["ptParms"] = ptParms 
    def setN_G(self, N_G):
        self.parms["N_G"] = N_G
    def setN_K(self, N_K):
        self.parms["N_K"] = N_K
    def setN_B(self, N_B):
        self.parms["N_B"] = N_B
    def setSb(self, sb):
        self.parms["sb"] = sb
    def setPtType(self, type):
        typeList = ["sech"]
        if type not in typeList:
            raise TypeError("type not in typeList")
        else:
            self.parms["ptType"] = type

    # METHODS
    def restoreDefaults(self):
        self.__init__()

    def generatePotential(self, type):
        typeList = ["sech"]
        if type not in typeList:
            raise TypeError("type not in typeList")
        elif type == "sech":
            return pt.generateSechPotential(self.getPtParms())

    def solveSchrodinger(self):
        ss =  schrodinger.solveSchrodinger(
            N_G=self.getN_G(),
            N_k=self.getN_K(),
            N_b=self.getN_B(),
            potential=self.getPotential()
            )
        return ss   

    def optimalBasis(self):
        ob = optimalbasis.optimalBasis(
            sb=self.getSb(),
            N_b=self.getN_B(),
            N_k=self.getN_K(),
            ck=self.getCk()
        )
        return ob
    
    

        

    
    

    
