#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
	line = line.strip()
	data = line.split("\t")
	key, values = data
	values = values.split(",")
	result = re.match('[*+]',values[1])
	if result is None:
		resultToPrint = [values[0],values[1]]
		print ",".join(resultToPrint)
		
