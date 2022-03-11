from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasisWithoutInspection
from quantum.interpolate import interpolateHamiltonian
from quantum import potential as pt


""" def getTest():
    N_G = 11
    N_b = 5
    N_k = 100
    sb = 0.1
    kpoints = 60
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 1, "width" :1 }
    ptl = pf.createPotential("sech", ptparms )
    ek, ck = solveSchrodinger(N_G,N_k,N_b,ptl)
    OB_bi = optimalBasisWithoutInspection(sb, N_k, N_b, ck)
    for ik in range(N_k):
        newEk = interpolateHamiltonian(sb, OB_bi, kpoints, N_G, N_k, N_b, ck, ik, ptl) 
    return newEk

print(getTest())        
 """

#hamiltonianFilledWithEk = 0.5*((kpoints**2)*np.kron(i, j) + (N_k*k1[i, j]) + k0[i, j])
def getTest():
    N_G = 11
    N_b = 5
    N_k = 100
    sb = 0.1
    kpoints = 60
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 1, "width" :1 }
    ptl = pf.createPotential("sech", ptparms )
    ek, ck = solveSchrodinger(N_G,N_k,N_b,ptl)
    OB_bi = optimalBasisWithoutInspection(sb, N_k, N_b, ck)
    for ik in range(N_k):
        newEk = interpolateHamiltonian(sb, OB_bi, kpoints, N_G, N_k, N_b, ck, ik, ptl ) 
    return newEk

print(getTest())        
