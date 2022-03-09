from quantum.optimalbasis import optimalBasis
from quantum.potential import generateSechPotential
from quantum.schrodinger import solveSchrodinger
import numpy as np

N_G = 8
N_b = 6
N_k = 70
ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
ptl = generateSechPotential(ptparms)
ek, ck = solveSchrodinger(N_G,N_k,N_b,ptl) 
sb = 0.1
ob = optimalBasis(sb, N_b, N_k, ck)
print(ob)