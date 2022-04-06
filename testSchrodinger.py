from quantum.qobj import Qobj

qobj = Qobj()

def testeigen():
    ek= qobj.getEk()
    return ek

print(testeigen())



