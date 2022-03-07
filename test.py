from quantum.schrodinger import solveSchrodinger
from quantum.schrodinger import solveSchroedinger1
<<<<<<< HEAD
from quantum import potential as pt
from testbasis import testckfunc, testckfunc2, testcktilda1, testcktildafinal, combineckfunc

=======
from testbasis import testckfunc, testckfunc2
import quantum.potential as pt
>>>>>>> 0b7872c534e1f4aa1d1e8305399d081772e297df

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




<<<<<<< HEAD


=======
#Take note how band structure and eigenenergies at the gamma point change when you fix the number of k-points (N_k)
#and change the number of plane-waves (N_G dependent) in the basis set expansion ()
>>>>>>> 0b7872c534e1f4aa1d1e8305399d081772e297df


<<<<<<< HEAD
=======
#Investigate how specific number of plane waves (REMEMBER: up to cutoff N_G) used can 

from quantum.matrix import fillmatrix

matrix = fillmatrix(2,2,2,ptl)
print(matrix)
>>>>>>> 0b7872c534e1f4aa1d1e8305399d081772e297df
