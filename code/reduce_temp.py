#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
	line = line.strip()
	data = line.split("\t")
	key, values = data
	values = values.split(",")
	result = re.match('[*+]',values[3])
	if result is None:
		resultToPrint = [values[0],values[3],values[4],values[5]]
		print ",".join(resultToPrint)
		
		
	
