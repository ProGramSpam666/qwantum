import quantum.potential as pt
import quantum.schrodinger as schrodinger
import quantum.optimalbasis as optimalbasis

class Qobj:
    # PRIVATE ATRRIBUTES
    __defaultPtParms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
    __defaultN_G = 8
    __defaultN_K = 100
    __defaultN_B = 5
    __defaultSb = 0.1
    

    # CONSTRUCTOR
    def __init__(self):
        self.setPtParms(self.get__defaultPtParms())
        self.setN_G(self.get__defaultN_G())
        self.setN_K(self.get__defaultN_K())
        self.setN_B(self.get__defaultN_B())
        self.setSb(self.get__defaultSb())
        self.setCk()
        

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
    def getPtParms(self):
        return self.ptParms
    def getN_G(self):
        return self.N_G
    def getN_K(self):
        return self.N_K
    def getN_B(self):
        return self.N_B
    def getPotential(self):
        return self.potential
    def getCk(self):
        return self.ck
    def getSb(self):
        return self.sb
    """ def getOptimalBasis(self):
        return self.optimalBasis """ 
        
    # PRIVATE SETTERS
    def setPtParms(self, ptParms):
        self.ptParms = ptParms 
        self.setPotential()
    def setN_G(self, N_G):
        self.N_G = N_G
    def setN_K(self, N_K):
        self.N_K = N_K
    def setN_B(self, N_B):
        self.N_B = N_B
    def setPotential(self):
        self.potential = self.generateSechPotential()
    def setCk(self):
        self.ck = self.returnCk()
    def setSb(self, sb):
        self.sb = sb
    def setOb(self):
        self.ob = self.optimalBasis()

    # METHODS
    def restoreDefaults(self):
        self.__init__()

    def generateSechPotential(self):
        return pt.generateSechPotential(self.getPtParms())

    def solveSchrodinger(self):
        return schrodinger.solveSchrodinger(
            N_G=self.getN_G(),
            N_k=self.getN_K(),
            N_b=self.getN_B(),
            potential=self.getPotential()
            )

    def returnCk(self):
        ek, ck = self.solveSchrodinger()
        del ek
        return ck

    def optimalBasis(self):
        ob = optimalbasis.optimalBasis(
            sb=self.getSb(),
            N_b=self.getN_B(),
            N_k=self.getN_K(),
            ck=self.getCk()
        )
        return ob
    

        

    
    

    
