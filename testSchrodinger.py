from quantum.schrodinger import solveSchrodinger
from quantum.potential import PotentialFactory
from quantum import potential as pt 
from quantum.optimalbasis import optimalBasis
from quantum.qobj import Qobj

qobj = Qobj()



def testeigen():
    ek= qobj.getEk()
    return ek

print(testeigen())



