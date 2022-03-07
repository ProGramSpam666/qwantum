import numpy as np
from math import sqrt
from quantum.schrodinger import solveSchrodinger
from quantum.schrodinger import solveSchroedinger1

def OptimalBasis(sb, N_b, N_k, ck): 
    
    OB_bi = np.zeros((np.shape(ck)[0], np.shape(ck)[1] * np.shape(ck)[2]), dtype= np.complex_)
    ckTilda = np.zeros(np.shape(ck), dtype= np.complex_)
    
    N = N_b 
    for i in range(N_b): 
        OB_bi[:, i] = ck[:, 0, i] 
     
    for l in range(1, N_k):
        for i in range(N_b):
            ckTilda[:, l, i] = ck[:, l , i]
            for j in range(N):
                ckTilda[:, l , i] -= OB_bi[:,j]*(np.dot(OB_bi[:,j], ck[:, l , i]))        
        Np = N
        for i in range(N_b):
            for j in range(Np, N):
                ckTilda[:, l, i] -= OB_bi[i, j]*(np.dot(OB_bi[:,j], ck[:, l , i]))
                alpha = np.dot(ckTilda[:, l, i], ckTilda[:, l ,i])
                if alpha >= sb:
                    N += 1
                    OB_bi[:,N] = ckTilda[:,l,i] / sqrt(alpha)
    
    print(N_b*N_k, N)
    bi_out = np.zeros((np.shape(ck)[0], N))
    bi_out[:, :] = OB_bi[:, 0:N]
    return bi_out

def OptimalBasisNEW(sb, N_b, N_k, OBck, N_G, potential): 

    OBck = solveSchroedinger1(N_G,N_k,N_b,potential)
    OB_bi = np.zeros((np.shape(OBck)[0], np.shape(OBck)[1] * np.shape(OBck)[2]), dtype= np.complex_)
    ckTilda = np.zeros(np.shape(OBck), dtype= np.complex_)
    
    N = N_b 
    for i in range(N_b): 
        OBck[:, 0, i]  = OB_bi[:, i]
        #OB_bi[:, i] = OBck[:, 0, i] 
    
    for l in range(1, N_k):
        for i in range(N_b):
            ckTilda[:, l, i] = OBck[:, l , i]
            for j in range(N):
                ckTilda[:, l , i] -= OB_bi[:,j]*(np.dot(OB_bi[:,j], OBck[:, l , i]))        
        Np = N
        for i in range(N_b):
            for j in range(Np, N):
                ckTilda[:, l, i] -= OB_bi[i, j]*(np.dot(OB_bi[:,j], OBck[:, l , i]))
                alpha = np.dot(ckTilda[:, l, i], ckTilda[:, l ,i])
                if alpha >= sb:
                    N += 1
                    OB_bi[:,N] = ckTilda[:,l,i] / sqrt(alpha)
    
    #print(N_b*N_k, N)
    bi_out = np.zeros((np.shape(OBck)[0], N))
    bi_out[:, :] = OB_bi[:, 0:N]
    return bi_out



