# qwantum

N_G = cuttoff for number of plane waves (Sum from 1 to N_G, think periodicity, think x direction)
N_b = number of bands considering (think y direction)
N_k = number of k points (think discretization x direction)
N = energy levels

ek = eigenenergies (eigenvalues)
ck = eigenfunctions (wavefunctions)


plotBand = plotting the shape of ck
plotFun = plotting wavefunctions, will need both ek and ck


OPTIMAL BASIS
invovlves taking ck vector (matrix) and optimising by performing gram schmidt orthonormalisation algoritm


INVESTIGATE
Take note how band structure and eigenenergies at the gamma point change when you fix the number of k-points (N_k)
and change the number of plane-waves (N_G dependent) in the basis set expansion ()

Fix plane-waves (N_G dependent) and vary the number of k-point (N_k) and check change of band structure (depending on ek) AND the eigenenergies (ek) at the gamma point

Investigate how specific number of plane waves (REMEMBER: up to cutoff N_G) can be utilized for specific results - 
i.e if you want the FIRST 5 eigenvalues correct to 5 significant figures, how many plane waves are required?

Repeat all tests for varying:
-lattice constant
-lattice depth
-lattice width
 


