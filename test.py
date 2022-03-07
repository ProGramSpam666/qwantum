from quantum.schrodinger import solveSchrodinger
from quantum import potential as pt
import quantum.potential as pt

pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
ptl = pf.createPotential("sech", ptparms)

ek,ck = solveSchrodinger(10,100,5,ptl)
print("-----------EK-----------")
print(ek.size)
print("-----------CK-----------")
print(ck.size)


#Take note how band structure and eigenenergies at the gamma point change when you fix the number of k-points (N_k)
#and change the number of plane-waves (N_G dependent) in the basis set expansion ()

#Fix plane-waves (N_G dependent) and vary the number of k-point (N_k) and check change of band structure (depending on ek) 
# AND the eigenenergies (ek) at the gamma point

#Investigate how specific number of plane waves (REMEMBER: up to cutoff N_G) used can 
 
from quantum.matrix import fillmatrix

matrix = fillmatrix(2,2,2,ptl)
print(matrix)
