from quantum.potential import generateSechPotential
from quantum.schrodinger import solveSchrodinger
from quantum.optimalbasis import optimalBasis

def test():
    ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
    potential = generateSechPotential(ptparms)
    N_G = 8
    N_b = 6
    N_k = 70
    ek, ck = solveSchrodinger(N_G, N_k, N_b, potential)
    del ek
    sb = 1
    ob = optimalBasis(sb, N_b, N_k, ck)
    print(ob)


test()

    
