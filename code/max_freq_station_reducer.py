#!/usr/bin/env python
import sys

count = 0
previousKey = None

for line in sys.stdin:
	line = line.strip()
	key, values = line.split("\t")
	month,day,hour, station_id = key.split(",")
	values = values.split(",")
	if previousKey and previousKey == key:
		count += 1
	elif previousKey and previousKey != key:
		month,day,hour, station_id = previousKey.split(",")
		print "{0},{1},{2},{3}".format(day+"-"+month+"-2015",hour+":00",values[1],count)
		previousKey = key
		count = 1
	else:
		previousKey = key
		count = 1
month,day,hour, station_id = previousKey.split(",")
print "{0},{1},{2},{3}".format(day+"-"+month+"-2015",hour+":00",values[1],count)
