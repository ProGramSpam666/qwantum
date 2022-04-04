from tkinter import N
from quantum.interpolate import interpolateHamiltonian
from quantum.qobj import Qobj

import time

from quantum.schrodinger import solveSchrodinger

qobj = Qobj()
N_G = qobj.get__defaultN_G()
N_k = qobj.get__defaultN_K()
N_b = qobj.get__defaultN_B()
potential = qobj.getPotential()
OB_bi = qobj.optimalBasis()
kList = qobj.getKList()
k0 = qobj.getk0()
k1 = qobj.getk1()
VLoc = qobj.getVLoc()
N = qobj.getN_B()

starttime = time.time()
solveSchrodinger(N_G, N_k, N_b, potential)
ssTime = time.time() - starttime
print("solveSchrodinger: " + str(ssTime))

ihStartTime = time.time()
interpolateHamiltonian(OB_bi, kList, k0, k1, VLoc, N)
ihTime = time.time() - ihStartTime
print("interpolateHamiltonian: " + str(ihTime))
