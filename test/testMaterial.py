import sys, os
sys.path.append(os.path.abspath(os.path.join('..','core')))

from material import Material

m = Material()
print(m.dielectric("FusedQuartz"))
print(m.permittivity("FusedQuartz"))
print(m.conductivity("Cu"))
print(m.permittivity("FusedQuartz",False))
print(m.lossTangent("FusedQuartz"))
