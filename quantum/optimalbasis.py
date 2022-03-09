import numpy as np
from math import sqrt
from quantum.schrodinger import solveSchrodinger
from quantum.schrodinger import solveSchroedinger1

#function to perform gram schmidt orthonormalization algorithm
def optimalBasis(sb, N_b, N_k, ck): 
    
    OB_bi = np.zeros((np.shape(ck)[0], np.shape(ck)[1] * np.shape(ck)[2]), dtype=np.complex_)
    ckTilda = np.zeros(np.shape(ck), dtype= np.complex_)
    ckTildaPrime = np.zeros(np.shape(ck), dtype= np.complex_)

    N = N_b #set N = number of bands (N_b) to be considered
    for i in range(N_b): #running over bands
        OB_bi[:, i] = ck[:, 0, i] #First N basis vectors = basis vectors at given k point
    for l in range(1, N_k): #running over all k points
        for i in range(N_b): #while running over bands
            ckTilda[:, l, i] = ck[:, l , i] #set ckTilda to vectors = 
            for j in range(N):
                ckTilda[:, l , i] -= OB_bi[:,j]*(np.dot(OB_bi[:,j], ck[:, l , i])) #subtract from the orignal vectors the projection onto the N_b basis vectors built from all k-point 

        Np = N-1
        for i in range(N_b):
            for j in range(Np, N):
                ckTildaPrime[:, l, i] -= OB_bi[:, j]*(np.dot(OB_bi[:,j], ck[:, l , i]))
                alpha = np.dot(ckTildaPrime[:, l, i], ckTildaPrime[:, l ,i])
                if alpha >= sb:
                    N += 1
                    print(N)
                    OB_bi[:,N] = ckTildaPrime[:,l,i] / sqrt(alpha)

    print(sb,N_b*N_k, N)
    bi_out = np.zeros((np.shape(ck)[0], N))
    bi_out[:, :] = OB_bi[:, 0:N]
    return bi_out

def optimalBasisWithoutInspection(sb ,N_k, N_b, ck):
    OB_bi = np.zeros((np.shape(ck)[0], np.shape(ck)[1] * np.shape(ck)[2]), dtype=np.complex_)
    N = N_b
    for i in range(N_b):
        OB_bi[:, i] = ck[:, 0, i]
    ckTilda = np.zeros(np.shape(ck), dtype= np.complex_)
    for l in range(1, N_k): 
        for i in range(N_b): 
            ckTilda[:, l, i] = ck[:, l , i]       
            for j in range(N):
                ckTilda[:, l , i] -= OB_bi[:,j]*(np.dot(OB_bi[:,j], ck[:, l , i]))
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

    bi_out = np.zeros((np.shape(ck)[0], N))
    bi_out[:, :] = OB_bi[:, 0:N]
    print(bi_out.size)
    return bi_out



def optimalProductBasis(sp, N_b, N_k, bi_out):
    
    BjTilda = np.zeros(np.shape(bi_out)[0], np.shape(bi_out)[1] * np.shape(bi_out)[2], dtype = np.complex_)
    BjTildaPrime = np.zeros(np.shape(bi_out), dtype=np.complex_)
    BjTildaPrimePrime = np.zeros(np.shape(bi_out)[0], np.shape(bi_out)[1] * np.shape(bi_out)[2], dtype = np.complex_)
    
    Np = 0
    for i in range(1, N_b):
        for j in range(1, N_b):
            bi_out_product = bi_out[:, i]*bi_out[:, j]
            BjTilda[:, i, j] = bi_out_product
            
        for j in range(1, N_b):
            for alpha in range(Np):
                BjTildaPrime[:, i, j] -= BjTilda[:,alpha]*(np.dot(BjTilda[:, alpha], bi_out_product[:, j]))
                   
        NpPrime = 0
        for j in range(1, N_b):
            for alpha in range(Np + 1, Np + NpPrime):
                BjTildaPrimePrime[:, j, alpha] -= BjTilda[:, alpha]*(np.dot(BjTilda[:, alpha], BjTildaPrime[:, j]))
                                                                                                      
            beta = np.dot(BjTildaPrimePrime[:, i, j], BjTildaPrimePrime[:, i, j])                                              
            if beta >= sp:
                NpPrime = NpPrime + 1
                BNpPrime = BjTildaPrimePrime / sqrt(beta)
          
        Np = Np + NpPrime 
    bi_final = np.zeros((np.shape(bi_out_product)[0], Np))
    bi_final[:, :] = BNpPrime[:, 0:Np]
    return bi_final









