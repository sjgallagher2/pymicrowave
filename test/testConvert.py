import sys, os
sys.path.append(os.path.abspath(os.path.join("..","core")))

import convert

print(convert.dbmToWatt(33))
print(convert.dbmToVolt(33,50))
print(convert.dbmToVolt(33,75+60j))

