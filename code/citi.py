#!/usr/bin/env python
from datetime import datetime
import sys

for line in sys.stdin:
	line = line.strip()

	bikeid,tripduration,starttime,stoptime,start_station_id,start_station_name,end_station_id,end_station_name,usertype,gender,start_station_latitude,start_station_longitude,end_station_latitude,end_station_longitude = line.split(",")
	#print "{0}\t{1},{2},{3},{4},{5},{6},{7},{8}".format(bikeid,tripduration,datetime.strptime(starttime, "%m/%d/%Y %H:%M"),datetime.strptime(stoptime, "%m/%d/%Y %H:%M"),start_station_id,start_station_name,end_station_id,end_station_name,usertype,gender,start_station_latitude,start_station_longitude,end_station_latitude,end_station_longitude)
	startdate  = starttime.split(" ")
	try:
		dtDate = None
		dtHour = None
		if startdate[0] != "" and len(startdate[1]) >0:
			dtDate  = datetime.strptime(startdate[0], "%m/%d/%Y")
			if len(startdate[1]) == 8:
				dtHour = datetime.strptime(startdate[1],"%H:%M:%S")
			elif len(startdate[1]) == 5:
				dtHour = datetime.strptime(startdate[1],"%H:%M")
			elif len(startdate[1]) == 2:
				dtHour = datetime.strptime(startdate[1],"%H")
		if dtDate and dtHour:
			print "{0},{1},{2}\t{3}".format(dtDate.strftime('%b'),dtDate.strftime('%d'),dtHour.strftime('%H'),1)
			#print "{0},{1}\t{2}".format(dtDate.strftime('%b'),dtDate.strftime('%d'),1)
	except:
		pass
