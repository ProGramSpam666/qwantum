import numpy as np
from quantum import potential as pt
from quantum.optimalbasis import optimalBasisWithoutInspection
from quantum.schrodinger import solveSchrodinger
from quantum.plot import plotBand
import matplotlib.pyplot as plt


pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
latticeptparms1 = { "lattice" : 1, "depth" : 1, "width" :0.1 }
latticeptparms2 = {"lattice" : 2, "depth" : 1, "width" : 0.1}
latticeptparms3 = {"lattice" : 3, "depth" : 1, "width" : 0.1}
latticeptparms4 = {"lattice" : 4, "depth" : 1, "width" : 0.1}
latticeptl1 = pf.createPotential("sech", latticeptparms1)
latticeptl2 = pf.createPotential("sech",latticeptparms2 )
latticeptl3 = pf.createPotential("sech", latticeptparms3)
latticeptl4 = pf.createPotential("sech", latticeptparms4)

#TEST1 - increasing lattice constant

#band structure (1)
ek1, ck1 = solveSchrodinger(2,100,5,latticeptl1) #N_G,N_k,N_b,potential
plot1 = plotBand(ek1,latticeptl1,'r-')

#band structure (2)
ek2, ck2 = solveSchrodinger(2, 100, 5, latticeptl2)
plot2 = plotBand(ek2, latticeptl2, 'b-')

#band structure (3)
ek3, ck3 = solveSchrodinger(2, 100, 5, latticeptl2)
plot3 = plotBand(ek3,latticeptl3,'y-')

#band structure (4)
ek4, ck4 = solveSchrodinger(2, 100, 5, latticeptl2)
plot4 = plotBand(ek4,latticeptl4,'g-')




""" pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
depthptparms1 = { "lattice" : 1, "depth" : 1, "width" :1 }
depthptparms2 = {"lattice" : 1, "depth" : 30, "width" : 1}
depthptparms3 = {"lattice" : 1, "depth" : 50, "width" : 1}
depthptparms4 = {"lattice" : 1, "depth" : 70, "width" : 1}
depthptl1 = pf.createPotential("sech", depthptparms1)
depthptl2 = pf.createPotential("sech",depthptparms2 )
depthptl3 = pf.createPotential("sech", depthptparms3)
depthptl4 = pf.createPotential("sech", depthptparms4)

#TEST2 - increasing depth

#band structure (1)
ek1, ck1 = solveSchrodinger(2,100,5,depthptl1) #N_G,N_k,N_b,potential
plot1 = plotBand(ek1,depthptl1,'r-')

#band structure (2)
ek2, ck2 = solveSchrodinger(2, 100, 5, depthptl2)
plot2 = plotBand(ek2, depthptl2, 'b-')

#band structure (3)
ek3, ck3 = solveSchrodinger(2, 100, 5, depthptl2)
plot3 = plotBand(ek3,depthptl3,'y-')

#band structure (4)
ek4, ck4 = solveSchrodinger(2, 100, 5, depthptl2)
plot4 = plotBand(ek4,depthptl4,'g-')

plt.show()



pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
widthptparms1 = { "lattice" : 1, "depth" : 1, "width" :0.05}
widthptparms2 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
widthptparms3 = {"lattice" : 1, "depth" : 1, "width" : 0.15}
widthptparms4 = {"lattice" : 1, "depth" : 1, "width" : 0.8}
widthptl1 = pf.createPotential("sech", widthptparms1)
widthptl2 = pf.createPotential("sech",widthptparms2 )
widthptl3 = pf.createPotential("sech", widthptparms3)
widthptl4 = pf.createPotential("sech", widthptparms4)

#TEST2 - increasing width

#band structure (1)
ek1, ck1 = solveSchrodinger(2,100,5,widthptl1) #N_G,N_k,N_b,potential
plot1 = plotBand(ek1,widthptl1,'r-')

#band structure (2)
ek2, ck2 = solveSchrodinger(2, 100, 5, widthptl2)
plot2 = plotBand(ek2, widthptl2, 'b-')

#band structure (3)
ek3, ck3 = solveSchrodinger(2, 100, 5, widthptl2)
plot3 = plotBand(ek3,widthptl3,'y-')

#band structure (4)
ek4, ck4 = solveSchrodinger(2, 100, 5, widthptl2)
plot4 = plotBand(ek4,widthptl4,'g-')

plt.show()

 """


""" pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
latticeptparms1 = { "lattice" : 1, "depth" : 1, "width" :0.1 }
latticeptparms2 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
latticeptparms3 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
latticeptparms4 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
latticeptl1 = pf.createPotential("sech", latticeptparms1)
latticeptl2 = pf.createPotential("sech",latticeptparms2 )
latticeptl3 = pf.createPotential("sech", latticeptparms3)
latticeptl4 = pf.createPotential("sech", latticeptparms4)

#TEST4 - increasing k-points

#band structure (1)
ek1, ck1 = solveSchrodinger(2,20,5,latticeptl1) #N_G,N_k,N_b,potential
plot1 = plotBand(ek1,latticeptl1,'r-')

#band structure (2)
ek2, ck2 = solveSchrodinger(2, 40, 5, latticeptl2)
plot2 = plotBand(ek2, latticeptl2, 'b-')

#band structure (3)
ek3, ck3 = solveSchrodinger(2, 60, 5, latticeptl2)
plot3 = plotBand(ek3,latticeptl3,'y-')

#band structure (4)
ek4, ck4 = solveSchrodinger(2, 80, 5, latticeptl2)
plot4 = plotBand(ek4,latticeptl4,'g-')

plt.show()
 """


""" 
pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
latticeptparms1 = { "lattice" : 1, "depth" : 1, "width" :0.1 }
latticeptparms2 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
latticeptparms3 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
latticeptparms4 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
latticeptl1 = pf.createPotential("sech", latticeptparms1)
latticeptl2 = pf.createPotential("sech",latticeptparms2 )
latticeptl3 = pf.createPotential("sech", latticeptparms3)
latticeptl4 = pf.createPotential("sech", latticeptparms4)

#TEST5 - increasing N_G

#band structure (1)
ek1, ck1 = solveSchrodinger(2,100,5,latticeptl1) #N_G,N_k,N_b,potential
plot1 = plotBand(ek1,latticeptl1,'r-')

#band structure (2)
ek2, ck2 = solveSchrodinger(4, 100, 5, latticeptl2)
plot2 = plotBand(ek2, latticeptl2, 'b-')

#band structure (3)
ek3, ck3 = solveSchrodinger(6, 100, 5, latticeptl2)
plot3 = plotBand(ek3,latticeptl3,'y-')

#band structure (4)
ek4, ck4 = solveSchrodinger(8, 100, 5, latticeptl2)
plot4 = plotBand(ek4,latticeptl4,'g-')

plt.show() """




""" pf = pt.PotentialFactory()
pf.addType("sech", pt.sechpotGenerator, pt.sechFTGenerator)
latticeptparms1 = { "lattice" : 1, "depth" : 1, "width" :0.1 }
latticeptparms2 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
latticeptparms3 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
latticeptparms4 = {"lattice" : 1, "depth" : 1, "width" : 0.1}
latticeptl1 = pf.createPotential("sech", latticeptparms1)
latticeptl2 = pf.createPotential("sech",latticeptparms2 )
latticeptl3 = pf.createPotential("sech", latticeptparms3)
latticeptl4 = pf.createPotential("sech", latticeptparms4)

#TEST6 - increasing N_b

#band structure (1)
ek1, ck1 = solveSchrodinger(5,100,2,latticeptl1) #N_G,N_k,N_b,potential
plot1 = plotBand(ek1,latticeptl1,'r-')

#band structure (2)
ek2, ck2 = solveSchrodinger(5, 100, 4, latticeptl2)
plot2 = plotBand(ek2, latticeptl2, 'b-')

#band structure (3)
ek3, ck3 = solveSchrodinger(5, 100, 6, latticeptl2)
plot3 = plotBand(ek3,latticeptl3,'y-')

#band structure (4)
ek4, ck4 = solveSchrodinger(5, 100, 8, latticeptl2)
plot4 = plotBand(ek4,latticeptl4,'g-')

plt.show()
 """





