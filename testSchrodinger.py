from quantum.schrodinger import solveSchrodingerForEk
from quantum.potential import PotentialFactory



def testeigen():
    pf = PotentialFactory()
    ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
    ptl = pf.createPotential("sech", ptparms)
    N_G = 3
    N_k = 70
    N_b = 5
    result = solveSchrodingerForEk(N_G, N_k, N_b, ptl)
    return result 

print(testeigen())





