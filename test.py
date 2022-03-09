from quantum import optimalbasis
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import OptimalBasis
from quantum import potential as pt
from testbasis import testingckTilda, investigateOptimalBasis, test1, test2, optimalbasistest
from quantum.matrix import fillmatrix

pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms = { "lattice" : 2, "depth" : 1, "width" :1 }
ptl = pf.createPotential("sech", ptparms)


""" print("----------TESTck[:, 0, i]--------")
print(testckfunc(3, 50, 4, ptl)) #arguments = (N_G, N_k, N_b, potential)

print("---------TESTck[:, i]----------")
print(testckfunc2(3, 50, 4, ptl))

print("--------TESTOB_bi-------") #-------TEST-------- being printed
print(testingOB_bi(3, 50, 4, ptl)) #printing (7,4) => N_G*N_k

print("-------TESTckTilda[:, l, i]---------")
ckTilda1 = testcktilda1(3, 50, 4, ptl)
print(testcktilda1(3, 50, 4, ptl))
print(ckTilda1.size)

print("TESTcktilda[:, l , i]final--------")
ckTildafinal = testcktildafinal(3, 50, 4, ptl)
print(testcktildafinal(3, 50, 4, ptl))
print(ckTildafinal.size) """

print(investigateOptimalBasis(0.001, 8, 10, 6, ptl))

#print("---------------------test1----------------------")
#print(test1())

#print("------------------test2-------------------")
#print(test2())


print(optimalbasistest())

ek,ck = solveSchrodinger(8,100,5,ptl)
print("-----------------ck size---------------------")
print(ck.size)

