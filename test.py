from quantum.schrodinger import solveSchrodinger
from quantum.schrodinger import solveSchroedinger1
from quantum import potential as pt
from testbasis import testckfunc, testckfunc2, testcktilda1, testcktildafinal, combineckfunc


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

print("--------TESTckcombine-------")
print(combineckfunc(3, 50, 4, ptl))


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








