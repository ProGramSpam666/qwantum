from quantum import optimalbasis
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis
from quantum import potential as pt
from testbasis import investigateOptimalBasis, newoptimalbasistest, loopSbOptimalBasis
from quantum.matrix import fillmatrix

pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms = { "lattice" : 2, "depth" : 1, "width" :1 }
ptl = pf.createPotential("sech", ptparms)
ek, ck = solveSchrodinger(8,100,5,ptl)

print(investigateOptimalBasis(0.1, 8 ,100, 5, ptl))

#print(newoptimalbasistest())

#print(loopSbOptimalBasis())





