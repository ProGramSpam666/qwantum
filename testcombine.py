

from quantum.qobj import Qobj
import matplotlib.pyplot as plt


qobj = Qobj()

def varyingLatticeConstantStandardImaginaryDielectricPlot():
    energy = qobj.getEnergyRangeFunc()
    qobj.setParms(lattice = 1)
    res1 = qobj.getStandardImaginaryDielectricPlotArray()
    plt.plot(energy, res1, 'r' )
    qobj.setParms(lattice = 2)
    res2 = qobj.getStandardImaginaryDielectricPlotArray()
    plt.plot(energy, res2, 'b')
    plt.show()
    return 
print(varyingLatticeConstantStandardImaginaryDielectricPlot()) 







