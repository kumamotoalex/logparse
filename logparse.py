import re
from logclass import *
import json


#Specifies what type of log to analyze
logtype = QLog

import sys
info = sys.argv[1]
f = open(info, 'r')
data = f.readlines()
f.close()
filename = sys.argv[2]
new = open(filename, "w")

i = 1
for dataline in data:
	jsonD = {}
	log = logtype(dataline)
	for attr in log.attrs:
		result = eval('log.' + attr)
		if result:
			jsonD[attr] = result
	# new.write(str(i) + '. ' + json.dump(jsonD, 'fp') + '\n')
	new.write(str(i) + '. ' + str(jsonD) + '\n' +'\n')
	i+=1

new.close()