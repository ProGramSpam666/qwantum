import unittest
import quantum.interpolate 
import quantum.qobj 

class InterpolateTester(unittest.TestCase):

    qobj = quantum.qobj.Qobj()

    def test_00_calculateVLoc(self):
        print("Start calculateVLoc test \n")
        qobj = quantum.qobj.Qobj()
        result = quantum.interpolate.calculateVLoc(
            OB_bi=qobj.getOptimalBasis(),
            N_G=qobj.getN_G(),
            N_GPrime= 11,
            N_GPrimePrime=23,
            potential=qobj.getPotential(),
            Ncell=25,
            Npoints=1000,
        )
        print(result)