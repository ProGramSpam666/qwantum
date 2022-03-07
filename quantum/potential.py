

class Potential:
    def __init__(self, name, parms, v, ft):
        self.name = name
        self.parms = parms
        self.v = v
        self.ft = ft

    def __str__(self):
        return self.name


class PotentialFactory:
        def __init__(self):
                self.potentialList = {}

        def addType(self, name, v, ft):
                potential = { "V" : v, "FourierTransform" : ft }
                self.potentialList[name] = potential
       
        def createPotential(self, name, parms):
                return Potential(name, parms,self.potentialList[name]["V"](parms),
                                 self.potentialList[name]["FourierTransform"](parms) )



#
# SECH = 1/COSH
#
def sechpotGenerator(parms):
        a = parms["lattice"]
        a0 = parms["width"]
        v0 = parms["depth"] 
        def pot(N, m):
                x = np.linspace(-N*a,N*a,N*m) #m defining our descritization
                U = np.zeros(len(x))
                #define grid
                for n in range(-N,N+1):
                        U = U - 1/np.cosh((x-n*a)/a0) #potential v(x)
                return x,v0*U
        return pot 


def sechFTGenerator(parms):
        a = parms["lattice"]
        a0 = parms["width"]
        v0 = parms["depth"] 
        def ft(m):
                Ug=-1/np.cosh(pi**2*a0*m/a)
                return Ug*v0*pi*a0/a
        return ft #returns Fourier Transform

# instantiate factory
pf = PotentialFactory()
pf.addType("sech", sechpotGenerator, sechFTGenerator) #performing transform

