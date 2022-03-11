import unittest
from quantum.potential import generateSechPotential
from quantum.qobj import Qobj
import quantum.schrodinger as schrodinger
import quantum.optimalbasis as optimalbasis

class QobjTester(unittest.TestCase):
    qobj = Qobj()
    
    def test_00_get_defaultPtParms(self):
        print("Start get_defaultPtParms test \n")
        self.assertEqual({ "lattice" : 2, "depth" : 1, "width" :0.1 }, self.qobj.get__defaultPtParms())

    def test_01_get_ptParms(self):
        print("Start get_ptParms test \n")
        self.assertEqual(self.qobj.get__defaultPtParms(), self.qobj.getPtParms()) #checks ptParms equal to default value

    def test_02_set_ptParms(self):
        print("Start set_ptParms test \n")
        newPtParms = { "lattice" : 3, "depth" : 2, "width" :2 }
        self.qobj.setPtParms(newPtParms)
        self.assertEqual(newPtParms, self.qobj.getPtParms()) # check ptParms is equal to newPtParms
    
    def test_03_get_potential(self):
        print("Start set_potential test \n")
        ptParms = self.qobj.getPtParms()
        expected = generateSechPotential(ptParms)
        result = self.qobj.getPotential()
        self.assertEqual(expected.name, result.name)
        self.assertEqual(expected.parms, result.parms)

    def test_04_getN_G(self):
        print("Start getN_G test  \n")
        self.assertEqual(8, self.qobj.getN_G())
    
    def test_05_getN_K(self):
        print("Start getN_K test \n")
        self.assertEqual(100, self.qobj.getN_K())

    def test_06_getN_B(self):
        print("Start getN_B test \n")
        self.assertEqual(5, self.qobj.getN_B())

    def test_07_setN_G(self):
        print("Start setN_G test \n")
        newN_G = self.qobj.getN_G() + 1
        self.qobj.setN_G(newN_G)
        self.assertEqual(newN_G, self.qobj.getN_G())

    def test_08_setN_K(self):
        print("Start setN_K test \n")
        newN_K = self.qobj.getN_K() + 1
        self.qobj.setN_K(newN_K)
        self.assertEqual(newN_K, self.qobj.getN_K())

    def test_09_setN_B(self):
        print("Start setN_B test \n")
        newN_B = self.qobj.getN_B() + 1
        self.qobj.setN_B(newN_B)
        self.assertEqual(newN_B, self.qobj.getN_B())

    def test_10_returnCk(self):
        print("Start returnCk test \n")
        ck = self.qobj.returnCk()
        ek, expected = schrodinger.solveSchrodinger(
            N_G=self.qobj.getN_G(),
            N_k=self.qobj.getN_K(),
            N_b=self.qobj.getN_B(),
            potential=self.qobj.getPotential()
        )
        del ek
        self.assertEqual(ck.all(), expected.all())

    def test_11_getSb(self):
        print("Start getSb test \n")
        sb = self.qobj.getSb()
        expected = self.qobj.get__defaultSb()
        self.assertEqual(sb, expected)

    def test_11_setSb(self):
        print("Start setSb test \n")
        newSb = 0.01
        self.qobj.setSb(newSb)
        self.assertEqual(newSb, self.qobj.getSb())

    def test_12_restoreDefaults(self):
        print("Start restoreDefaults test \n")
        self.qobj.restoreDefaults()
        self.assertEqual(self.qobj.getPtParms(), self.qobj.get__defaultPtParms())
        self.assertEqual(self.qobj.getN_G(), self.qobj.get__defaultN_G())
        self.assertEqual(self.qobj.getN_K(), self.qobj.get__defaultN_K())
        self.assertEqual(self.qobj.getN_B(), self.qobj.get__defaultN_B())
        self.assertEqual(self.qobj.getSb(), self.qobj.get__defaultSb()) 

    def test_13_solveSchrodinger(self):
        print("Start solveSchrodinger test \n")
        ek, ck =  self.qobj.solveSchrodinger()
        ekExp, ckExp = schrodinger.solveSchrodinger(
            N_G=self.qobj.getN_G(),
            N_k=self.qobj.getN_K(),
            N_b=self.qobj.getN_B(),
            potential=self.qobj.getPotential()
        )
        self.assertEqual(ek.all(), ekExp.all())
        self.assertEqual(ck.all(), ckExp.all())

    def test_14_optimalBasis(self):
        print("Start optimalBasis test \n")
        ob = self.qobj.optimalBasis()
        obExp = optimalbasis.optimalBasis(
            sb=self.qobj.getSb(),
            N_b=self.qobj.getN_B(),
            N_k=self.qobj.getN_K(),
            ck=self.qobj.getCk()
        )
        self.assertEqual(ob.all(), obExp.all())


