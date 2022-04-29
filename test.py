import matplotlib.pyplot as plt
from quantum import optimalbasis
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasisGetOBBI
from quantum import potential as pt
import numpy as np
from quantum.qobj import Qobj
from quantum.interpolate import calculateVLoc
from quantum.potential import PotentialFactory as pf


"""File to run quick tests if required"""


qobj = Qobj()

def getOB_bi():
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 0.2, "width" : 0.2 }
    ptl = pf.createPotential("sech", ptparms)
    [ek,ck] = solveSchrodinger(3,100,5,ptl)
    del ek
    obbi = optimalBasisGetOBBI(0.001, 5, 100, ck)
    sizevalue = obbi.size
    return sizevalue














