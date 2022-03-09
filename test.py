from quantum import optimalbasis
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import OptimalBasis
from quantum import potential as pt
from testbasis import investigateOptimalBasis, test1, test2, optimalbasistest, optimalbasiswithoutinspection, newoptimalbasistest
from quantum.matrix import fillmatrix

pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms = { "lattice" : 2, "depth" : 1, "width" :1 }
ptl = pf.createPotential("sech", ptparms)

#print(investigateOptimalBasis(0.001, 8, 10, 6, ptl))

#print("---------------------test1----------------------")
#print(test1())

#print("------------------test2-------------------")
#print(test2())

#ek,ck = solveSchrodinger(8,100,5,ptl)
#print("-----------------ck size---------------------")
#print(ck.size)

#print(optimalbasiswithoutinspection(0.1, 8, 100, 6, ptl))

#print(optimalbasistest())


#ek, ck = solveSchrodinger(8,100,5,ptl)
#print("-----------------ck size---------------------")
#print(ck.size)


print(newoptimalbasistest())

