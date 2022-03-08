from quantum import optimalbasis
from quantum.schrodinger import solveSchrodinger
from quantum.schrodinger import solveSchroedinger1
from quantum.optimalbasis import OptimalBasis
from quantum import potential as pt
from testbasis import testckfunc, testckfunc2, testcktilda1, testcktildafinal, testingOB_bi
from testbasis import testingckTilda, test
from quantum.matrix import fillmatrix

pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
ptl = pf.createPotential("sech", ptparms)


ek,ck = solveSchrodinger(10,100,5,ptl)
print("-----------EK-----------")
print(ek.size)

print("-----------CK-----------")
print(ck.size)

print("---------------TESTshapeck----------")
print(ck.shape)

print("----------TESTck[:, 0, i]--------")
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
print(ckTildafinal.size)

print("------TEST")
print()

matrix = fillmatrix(2,2,2,ptl)
print(matrix)

print("---------")
print(testingckTilda(3, 50, ck, 4, ptl ))

print("-----------OB-------------")

print(test())




