from quantum import potential as pt

pf = pt.PotentialFactory()
pf.addType("well", pt.wellpotGenerator, pt.wellFTGenerator)
print(pf.potentialList)