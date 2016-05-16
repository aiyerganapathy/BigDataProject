#!/usr/bin/env python
import sys

previousKey = None
totalRevenue = 0

for line in sys.stdin:
	line = line.strip()
	#print line
	key, values = line.split("\t")

	if previousKey and previousKey == key:
		totalRevenue += float(values)
	elif previousKey and previousKey != key:
		month,day,hour = previousKey.split(",")
		print "{0},{1},{2}".format(day+"-"+month+"-2015",hour,totalRevenue)
		previousKey = key
		totalRevenue = float(values)
	else:
		previousKey = key
		totalRevenue = float(values)
month,day,hour = previousKey.split(",")
print "{0},{1},{2}".format(day+"-"+month+"-2015",hour,totalRevenue)