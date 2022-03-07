from quantum.schrodinger import solveSchrodinger
from quantum import potential as pt
from quantum.plot import plotBand, plotFun

pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
ptl = pf.createPotential("sech", ptparms)
[ek,ck] = solveSchrodinger(10,100,5,ptl)
plotBand(ek,ptl,'r-')
plotFun(2,ek,ck,3,10,ptl,'r-',2)