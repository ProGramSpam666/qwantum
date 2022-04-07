from numpy import ndarray
import quantum.potential as pt
import quantum.schrodinger as schrodinger
import quantum.optimalbasis as optimalbasis
import quantum.interpolate as interpolateHamiltonian
import quantum.utils as utils 
import quantum.velocityOp as velocityoperator
import quantum.gettime as getTime
import quantum.table as Table
import quantum.plot as plot

class Qobj:

    # PRIVATE ATRRIBUTEs
    __defaultPtParms = { "lattice" : 1, "depth" : 10, "width" :0.1 }
    __defaultN_G = 10
    __defaultN_K = 25
    __defaultN_B = 5
    __defaultSb = 0.3
    __defaultPtType = "sech"
    
    
    # CONSTRUCTOR
    def __init__(self):
        self.parms = {}
        self.setParms(
            ptParms = self.get__defaultPtParms(),
            N_G = self.get__defaultN_G(),
            N_K = self.get__defaultN_K(),
            N_B = self.get__defaultN_B(),
            sb = self.get__defaultSb(),
            ptType = self.get__defaultPtType()
        )
    

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
    def get__defaultLatticeConstant(self):
        return self.__defaultPtParms["lattice"]
    def get__defaultPotentialDepth(self):
        return self.__defaultPtParms["depth"]
    def get__defaultPotentialWidth(self):
        return self.__defaultPtParms["width"]           
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
    def getLatticeConstant(self):
        return self.getPtParms()["lattice"]
    def getPotentialDepth(self):
        return self.getPtParms()["depth"] 
    def getPotentialWidth(self):
        return self.getPtParms()["width"]           
    def getPotential(self):
        return self.__potential
    def getEk(self):
        return self.__ek
    def getCk(self):
        return self.__ck
    def getOptimalBasis(self):
        return self.__OB
    def getk0(self):
        return self.__k0   
    def getk1(self):
        return self.__k1
    def getVLoc(self):
        return self.__vLoc         
    def getKList(self):
        return self.__klist
    def getInterpolateHamiltonian(self):
        return self.interpolateHamiltonian()    
    def getDifferenceInEkTable(self):
        return self.differenceEigenvalues()
    def getEkTimeSolveSchrodinger(self):
        return self.ekTimeSolveSchrodinger()
    def getEkTimeInterpolateHamiltonian(self):
        return self.ekTimeInterpolateHamiltonian() 
    def getDifferenceTimeForEk(self):
        return self.differenceTimeForGettingEk()   
    def getVelocityOperator(self):
        return self.velocityOperator()
    def getBands(self):
        return self.__bands


    # SETTERS
    def __setPtParms(self, ptParms):
        self.parms["ptParms"] = ptParms 
    def __setN_G(self, N_G):
        self.parms["N_G"] = N_G
    def __setN_K(self, N_K):
        self.parms["N_K"] = N_K
    def __setN_B(self, N_B):
        self.parms["N_B"] = N_B
    def __setSb(self, sb):
        self.parms["sb"] = sb
    def __setPtType(self, ptType):
        typeList = ["sech"]
        if ptType not in typeList:
            raise TypeError("type not in typeList")
        else:
            self.parms["ptType"] = ptType
    def __setOptimalBasis(self):
        self.__OB = self.optimalBasis()
    def __setKList(self):
        self.__klist = self.kList()
    def __setPotential(self):
        self.__potential = self.generatePotential(self.getPtType())
    def __setK0(self):
        self.__k0 = self.calculatek0()
    def __setK1(self):
        self.__k1 = self.calculatek1()
    def __setVLoc(self):
        self.__vLoc = self.calculateVLoc()
    def __setEkAndCk(self):
        ek, ck = self.solveSchrodinger()
        self.__ek = ek
        self.__ck = ck
    def __setBands(self):
        self.__bands = self.bandStructure()
    def setParms(self, **kwargs):
        for arg in kwargs:
            if arg == "ptParms":
                ptParms = kwargs.get("ptParms")
                self.__setPtParms(ptParms)
            if arg == "N_G":
                N_G = kwargs.get("N_G")
                self.__setN_G(N_G)
            if arg == "N_K":    
                N_K = kwargs.get("N_K")
                self.__setN_K(N_K)
            if arg == "N_B":
                N_B = kwargs.get("N_B")
                self.__setN_B(N_B)
            if arg == "sb":
                sb = kwargs.get("sb")
                self.__setSb(sb)
            if arg == "ptType":
                ptType = kwargs.get("ptType")
                self.__setPtType(ptType)
        self.__setPotential()
        self.__setEkAndCk()
        self.__setOptimalBasis()
        self.__setKList()
        self.__setK0()
        self.__setK1()
        self.__setVLoc()
        
        

            


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

    def calculatek0(self):
        k0 = interpolateHamiltonian.calculatek0(
            OB_bi = self.getOptimalBasis(),
            potential = self.getPotential()
        )
        return k0    

    def calculatek1(self):
        k1 = interpolateHamiltonian.calculatek1(
            OB_bi = self.getOptimalBasis(),
            potential = self.getPotential()
        )
        return k1  

    def calculateVLoc(self):
        VLoc = interpolateHamiltonian.calculateVLoc(
            OB_bi = self.getOptimalBasis(),
            potential = self.getPotential()
        )
        return VLoc    

    def kList(self):
        klist = utils.kList(
            N_k = self.getN_K(),
            potential = self.getPotential()
        )
        return klist
        
    def interpolateHamiltonian(self):
        interHamil = interpolateHamiltonian.interpolateHamiltonian(
            OB_bi = self.getOptimalBasis(),
            kList = self.getKList(),
            k0 = self.getk0(),
            k1 = self.getk1(),
            VLoc = self.getVLoc(),
            N = self.getN_B()
        )
        return interHamil   

    
    def differenceEigenvalues(self):
        differenceEk = Table.differenceInEigenvalues(
            sb  = self.getSb(),
            N_G = self.getN_G(),
            N_k = self.getN_K(),
            N_b = self.getN_B(),
            potential = self.getPotential(),
            N = self.getN_B()
        )
        return differenceEk

    def ekTimeSolveSchrodinger(self):
        ekTimeSS = getTime.standardTimeForEk(
            N_G= self.getN_G(),
            N_k= self.getN_K(),
            N_b= self.getN_B(),
            potential= self.getPotential()
        )
        return ekTimeSS

    def ekTimeInterpolateHamiltonian(self):
        ekTimeIH = getTime.optimisedTimeForEk(
            OB_bi = self.getOptimalBasis(),
            kList = self.getKList(),
            k0 = self.getk0(),
            k1 = self.getk1(),
            VLoc = self.getVLoc(),
            N_b = self.getN_B()
        )
        return ekTimeIH    

    def differenceTimeForGettingEk(self):
        differenceTime = getTime.differenceInTimeForObtainingEk(
            N_G= self.getN_G(),
            N_k= self.getN_K(),
            N_b= self.getN_B(),
            potential= self.getPotential(),
            OB_bi = self.getOptimalBasis(),
            kList = self.getKList(),
            k0 = self.getk0(),
            k1 = self.getk1(),
            VLoc = self.getVLoc(),
            N = self.getN_B()
        )
        return differenceTime

    def velocityOperator(self):
        kdvo = velocityoperator.kDepVelOperatorOB(
            N_b = self.getN_B(),
            k1 = self.getk1(),
            OB_bi = self.getOptimalBasis(),
            kList = self.getKList(),
            ck = self.getCk()
        )
        return kdvo

    def bandStructure(self)->ndarray:
        bands = plot.bandStructure(
            ek=self.getEk(),
            potential=self.getPotential()
        )
        return bands





     
     