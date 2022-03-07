import numpy as np
from quantum.schrodinger import solveSchrodinger
from quantum.schrodinger import solveSchroedinger1
from quantum.optimalbasis import OptimalBasis


def determineBasis(N_G, N_b, N_k, ck, potential):
    [ek,ck] = solveSchrodinger(N_G,N_k,N_b,potential)
    for i in range(N_b):
        basis = ck
    return basis


def determineOptimalBasis(N_G, N_b, N_k, sb, ck, potential):
    ck = solveSchrodinger(N_G,N_k,N_b,potential)
    ckNEW = OptimalBasis(sb, N_b, N_k, ck)
    for sb in range(N_b):
        optimalBasis = ckNEW
    return optimalBasis

def testckfunc(N_G, N_k, N_b, potential):
    ck = solveSchroedinger1(N_G,N_k,N_b,potential)
    for i in range(N_b):
        new = ck[:, 0, i]
        return new   

def testckfunc2(N_G, N_k, N_b, potential):
    ck = solveSchroedinger1(N_G,N_k,N_b,potential)
    for i in range(N_b):
        new = ck[:, i]
        return new       





















