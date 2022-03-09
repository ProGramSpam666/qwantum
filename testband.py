import numpy as np
from quantum import potential as pt
from quantum.schrodinger import solveSchrodinger
from quantum.plot import plotBand


pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms1 = { "lattice" : 2, "depth" : 1, "width" :1 }
ptparms2 = {}
ptl1 = pf.createPotential("sech", ptparms1)
ptl2 = pf.createPotential("sech",ptparms1 )

ek, ck = solveSchrodinger(8,100,5,ptl1)
print(ek)
print(plotBand(ek,ptl1,'r-'))







