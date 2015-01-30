import re
from logclass import *
import json


import sys
info = sys.argv[1]
f = open(info, 'r')
data = f.readlines()
f.close()
jsonD = {}
i = 1
for dataline in data:
	jsonD[i] = dataline
	i+=1


result = json.dumps(jsonD, indent = 4, separators=('\n', ': '))
try:
    outputfile = open("output.txt", "w")
    try:
        outputfile.write(result)
    finally:
        outputfile.close()
except IOError:
    pass
