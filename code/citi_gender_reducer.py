#!/usr/bin/env python
import sys
from decimal import *
previousGender = None
count = 0
totalDuration = 0
for line in sys.stdin:
	line = line.strip()
	key,value = line.split("\t")
	value = value.split(",")
	if len(key) > 0:
		if previousGender and previousGender == key:
			count = count +  1
			totalDuration = totalDuration +  int(value[1])
		elif previousGender and previousGender != key:
			avgDuration = Decimal(int(totalDuration)/int(count))
			print "{0},{1},{2}".format(previousGender,count,str(avgDuration))
			previousGender = None
			totalDuration = 0
		else:
			previousGender = key
			count = 1
			totalDuration = int(value[1])
avgDuration = Decimal(int(totalDuration)/int(count))
print "{0},{1},{2}".format(previousGender.strip(),count,str(avgDuration))