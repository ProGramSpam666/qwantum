<<<<<<< Updated upstream
=======
from quantum.plot import plotFun
from quantum.potential import PotentialFactory
from quantum.schrodinger import solveSchrodinger
from quantum import potential as pt


pf = PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
ptl = pf.createPotential("sech", ptparms)
[ek,ck] = solveSchrodinger(5,100,4,ptl)
print(plotFun(10,ek,ck,3,10,ptl,'r', 2))


<<<<<<< Updated upstream
#ik,ek,ck,Ncell,Npoints,potential,symbol,shift
>>>>>>> Stashed changes
=======
#ik,ek,ck,Ncell,Npoints,potential,symbol,shift
>>>>>>> Stashed changes
