import numpy as np
from math import sqrt 
from quantum.schrodinger import solveSchrodinger
from quantum.schrodinger import solveSchroedinger1
from quantum.optimalbasis import OptimalBasis
from quantum.potential import PotentialFactory as pf
from quantum import potential as pt

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

def testingOB_bi(N_G, N_k, N_b, potential):
    N = N_b
    ck = solveSchroedinger1(N_G,N_k,N_b,potential)
    OB_bi = np.zeros((np.shape(ck)[0], np.shape(ck)[1] * np.shape(ck)[2]), dtype= np.complex_)
    for i in range(N):
        print("-----------NEW-----------")
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
    print(ckTilda.size)    
    print(ckTilda.shape)        
    return ckTilda



def investigateOptimalBasis(sb, N_G ,N_k, N_b, potential):
    ek, ck = solveSchrodinger(N_G,N_k,N_b,potential)
    print("--------------------size ek--------------")
    print(ek.size)
    print("----------------------size ck---------------")
    print(ck.size)
    print("-----------------------ckshape------------------------")
    ckshape = np.shape(ck)
    print(ckshape)
    print("--------------------ck[0]shape---------------")
    print(np.shape(ck)[0])
    print("--------------------ck[0]----------------")
    print(ck[0])
    print("----------------------OBbishape-----------------------")
    OB_bi = np.zeros((np.shape(ck)[0], np.shape(ck)[1] * np.shape(ck)[2]), dtype=np.complex_)
    OB_bishape = np.shape(OB_bi)
    print(OB_bishape)
    print("-----------------OB_bi[0]---------------------------")
    OB_bizero = OB_bi[0]
    print(OB_bizero)
    print("-------------------OB_bi[1]------------------------")
    OB_bione = OB_bi[1]
    print(OB_bione)
    N = N_b
    print("------------------First section------------------------")
    for i in range(N_b):
        OB_bi[:, i] = ck[:, 0, i]
    print("---------------------- shape OB_bi[:, i]--------------")
    OB_biinsideforloopshape = np.shape(OB_bi[:,i])
    print(OB_biinsideforloopshape) 
    print("----------------------- shape ck[:, 0, i]-------------------")
    ckinsideforloopshape = np.shape(ck[:, 0, i])
    print(ckinsideforloopshape)
    print("--------------------------OB_bi[:]--------------")
    OB_bicolon = OB_bi[:]
    print(OB_bicolon)
    print("-------------------------ck[:]----------------------")
    ckcolon = ck[:]
    print(ckcolon)
    print("--------------------------OB_bi[:, i]------------------")
    OB_bicoloni = OB_bi[:, i]
    print(OB_bicoloni)
    print("-----------------------ck[:, 0]-----------------")
    ck_colon_zero = ck[:, 0]
    print(ck_colon_zero)
    print("---------------------ck[:, 0, i]------------------")
    ckcolonzeroi = ck[:, 0, i]
    print(ckcolonzeroi)
    print("------------------Second section--------------------")
    ckTilda = np.zeros(np.shape(ck), dtype= np.complex_)
    for l in range(1, N_k): 
        for i in range(N_b): 
            ckTilda[:, l, i] = ck[:, l , i]       
            for j in range(N):
                ckTilda[:, l , i] -= OB_bi[:,j]*(np.dot(OB_bi[:,j], ck[:, l , i]))
        print("-------------------ck[:, l, i]------------------")
        ckcolonli = ck[:, l, i]
        print(ckcolonli)
        print("-----------------------shape ck[:, l, i]------------")
        print(np.shape(ckcolonli))
        print("-------------------------ckTilda[:, l, i]------------------")
        cktildacolonli = ckTilda[:, l, i]
        print(cktildacolonli)
        print("-----------------------shape ckTilda[:, l, i]----------------")
        print(np.shape(cktildacolonli))
        print("-----------------------OB_bi[:, j]----------------")
        OB_bicolonj = OB_bi[:, j]
        print(OB_bicolonj)
        print("------------------------shape OB_bi[:, j]---------------")
        print(np.shape(OB_bicolonj))
        print("--------------------- OB_bi[:,j]*(np.dot(OB_bi[:,j], ck[:, l , i]))--------------------")
        projection1 = OB_bi[:,j]*(np.dot(OB_bi[:,j], ck[:, l , i]))
        print(projection1)
        print("------------------- shape projection1----------------")
        print(np.shape(projection1))
        print("--------------------Third section---------------------")
        Np = N-1
        ckTildaPrime = np.zeros(np.shape(ck), dtype= np.complex_)
        for i in range(N_b):
            for j in range(Np, N):
                ckTildaPrime[:, l, i] -= OB_bi[:, j]*(np.dot(OB_bi[:,j], ck[:, l , i]))
                alpha = np.dot(ckTildaPrime[:, l, i], ckTildaPrime[:, l ,i])
                if alpha >= sb:
                    N += 1
                    print(N)
                    OB_bi[:,N] = ckTildaPrime[:,l,i] / sqrt(alpha)
        print("---------------------shape ckTildaPrime----------------------")
        print(np.shape(ckTildaPrime))
        print("-------------------ckTildaPrime[:, l, i]---------------------")
        ckTildaPrimecolonli = ckTildaPrime[:, l, i]
        print(ckTildaPrimecolonli)
        print("------------------- shape ckTildaPrime[:, l, i]---------------------")
        print(np.shape(ckTildaPrimecolonli))
        print("--------------------- new OB_bi[:, j]--------------------")
        newOB_bicolonj = OB_bi[:, j]
        print(newOB_bicolonj)
        print("--------------------- shape new OB_bi[:, j]----------------------")
        print(np.shape(newOB_bicolonj))
        print("--------------------- new OB_bi[i, j]---------------------")
        newOB_biij = OB_bi[i, j]
        print(newOB_biij)
        print("-------------------projection 2----------------------------")
        projection2 = OB_bi[:, j]*(np.dot(OB_bi[:,j], ck[:, l , i]))
        print(projection2)
        print("-------------------- shape projection 2---------------")
        print(np.shape(projection2))
        print("-------------------------shape alpha-------------------")
        print(np.shape(alpha))
        print("----------------------- alpha-----------------")
        print(alpha)
        print("--------------------------OB_bi[:, N]----------------")
        OB_bicolonN = OB_bi[:, N]
        print(OB_bicolonN)
        print("------------------------- shape OB_bi[:, N]---------------")
        print(np.shape(OB_bicolonN))
    print("------------------sb, N_b*N_k, N------------------")    
    print(sb,N_b*N_k, N)
    print("--------------------bi_out-------------------")
    bi_out = np.zeros((np.shape(ck)[0], N))
    print(bi_out)
    print("-------------------shape bi_out-------------------")
    print(np.shape(bi_out))
    bi_out[:, :] = OB_bi[:, 0:N]
    print("-------------------OB_bi[:, 0:N]------------------")
    OB_bicolonzerocolonN = OB_bi[:, 0:N]
    print(OB_bicolonzerocolonN)
    print("-------------------- shape OB_bi[:, 0:N]--------------- ")
    print(np.shape(OB_bicolonzerocolonN))   
    print("----------------------bi_out[:,:]-----------------")
    bi_outcoloncolon = bi_out[:, :]
    print(bi_outcoloncolon)
    print("---------------------- shape bi_out[:, :]---------------------")
    print(np.shape(bi_outcoloncolon))
    print("------------------------bi_out------------------------")
    print(bi_out)
    print("-------------compare bi_out size to N_b*N_k-----------------")
    print("------------------------ size bi_out----------------")
    print(bi_out.size)
    print("------------------------size N_b*N_k------------------")
    print(N_b*N_k)
    #return bi_out


#investigate optimal basis test 1
def test1():
    N_G = 8
    N_b = 5
    N_k = 100
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
    ptl = pf.createPotential("sech", ptparms ) 
    for sb in (0.1, 0.001, 0.0001, 0.00001, 0.0000001):
        obtain = investigateOptimalBasis(sb, N_G, N_k, N_b, ptl)
        print("-----------------obtain----------------------")
        print(obtain)
        print("---------------obtain size--------------------")
        print(obtain.size)
        print("--------------------shape obtain---------------------")
        print(np.shape(obtain))

#investigate optimal basis test 2
def test2():
    N_G = 8
    N_b = 5
    N_k = 70
    sb = 0.1
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 1, "width" :0.1 }
    ptl = pf.createPotential("sech", ptparms )
    obtain = investigateOptimalBasis(sb, N_G, N_k, N_b, ptl)
    print("-----------------obtain----------------------")
    print(obtain)
    print("---------------obtain size--------------------")
    print(obtain.size)
    print("--------------------shape obtain---------------------")
    print(np.shape(obtain))

#optimal basis test - USED
def optimalbasistest():
    N_G = 8
    N_b = 5
    N_k = 70
    sb = 0.05
    pf = pt.PotentialFactory()
    pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
    ptparms = { "lattice" : 2, "depth" : 1, "width" :1 }
    ptl = pf.createPotential("sech", ptparms )
    obtain = investigateOptimalBasis(sb, N_G, N_k, N_b, ptl)
    print("------------compare obtain to N_b*N_k-------------")
    print(obtain)
    print(N_b*N_k)










   

    