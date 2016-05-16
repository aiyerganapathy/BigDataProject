#!/usr/bin/env python

import sys

for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    splits=value.split("|")
    latlng = splits[9].split(",")
    try:
	if int(key) >=0 and splits[0]!="" and int(splits[0]) > 0 and int(splits[0]) > 0 and splits[1]!="" and splits[2]!="" and splits[3]!="" and int(splits[3]) >= 0 and splits[4] != "" and splits[5] != "" and int(splits[5]) > 0  and splits[6]!=""  and splits[7]!="" and splits[8]!="" and int(splits[8]) >=0  and latlng[0]!="" and latlng[1]!="" and latlng[2]!="" and latlng[3]!="" :
        	print "%s,%s" %(key,value)
    except:
    	pass