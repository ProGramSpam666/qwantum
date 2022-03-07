import numpy as np
from quantum.schrodinger import solveSchrodinger
from quantum.schrodinger import solveSchroedinger1
from quantum.optimalbasis import OptimalBasis

#checking form 
def testckfunc(N_G, N_k, N_b, potential):
    N = N_b
    ck = solveSchroedinger1(N_G,N_k,N_b,potential)
    for i in range(N):
        new = ck[:, 0, i]
        return new   

def testckfunc2(N_G, N_k, N_b, potential):
    N = N_b
    ck = solveSchroedinger1(N_G,N_k,N_b,potential)
    for i in range(N):
        new = ck[:, i]
        return new

#testing applicability of first for loop
def testingOB_bi(N_G, N_k, N_b, potential):
    N = N_b
    ck = solveSchroedinger1(N_G,N_k,N_b,potential)
    OB_bi = np.zeros((np.shape(ck)[0], np.shape(ck)[1] * np.shape(ck)[2]), dtype= np.complex_)
    for i in range(N):
        print("-----------GOAT-----------")
        print(ck[:, i].shape)
        print("---------------")
        print(ck[:,0, i].shape)
        print("--------------")
        OB_bi[:, i] = ck[:, 0, i] 
        print(OB_bi.size)
        return OB_bi

def testingckTilda(N_b, N_k, ck, N_G, potential): 
    ck = solveSchroedinger1(N_G,N_k,N_b,potential)
    OB_bi = np.zeros((np.shape(ck)[0], np.shape(ck)[1] * np.shape(ck)[2]), dtype= np.complex_)
    ckTilda = np.zeros(np.shape(ck), dtype= np.complex_)
    N = N_b 
    for i in range(N_b): 
        ck[:, 0, i] = OB_bi[:, i]
        #OB_bi[:, i] = ck[:, 0, i] 
    for l in range(1, N_k):
        for i in range(N_b):
            ckTilda[:, l, i] = ck[:, l , i]
            for j in range(N):
                ckTilda[:, l , i] -= OB_bi[:,j]*(np.dot(OB_bi[:,j], ck[:, l , i]))
                return ckTilda


#checking cktilda
def testcktilda1(N_G, N_k, N_b, potential):
    ck = solveSchroedinger1(N_G,N_k,N_b,potential)
    ckTilda = np.zeros(np.shape(ck), dtype= np.complex_)
    for l in range(1, N_k):
        for i in range(N_b):
            ckTilda[:, l, i] = ck[:, l , i]
    return ckTilda


#testing ckTildaFinal
def testcktildafinal(N_G, N_k, N_b, potential):
    N = N_b
    ck = solveSchroedinger1(N_G,N_k,N_b,potential)
    OB_bi = np.zeros((np.shape(ck)[0], np.shape(ck)[1] * np.shape(ck)[2]), dtype= np.complex_)
    ckTilda = np.zeros(np.shape(ck), dtype= np.complex_)
    for l in range(1, N_k):
        for i in range(N_b):
            ckTilda[:, l, i] = ck[:, l , i]
            for j in range(N):
                ckTilda[:, l , i] -= OB_bi[:,j]*(np.dot(OB_bi[:,j], ck[:, l , i]))
    return ckTilda

