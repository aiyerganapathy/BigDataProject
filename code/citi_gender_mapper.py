#!/usr/bin/env python
import sys
from datetime import datetime

for line in sys.stdin:
	line = line.strip()
	bikeid,tripduration,starttime,stoptime,start_station_id,start_station_name,end_station_id,end_station_name,usertype,gender,start_station_latitude,start_station_longitude,end_station_latitude,end_station_longitude = line.split(",")
	genderValue = None
	try:
		gender = gender.strip()
		FMT1 = '%H:%M:%S'
		FMT2 = '%H:%M'
		FMT3 = '%H'
		startDate , startTime = starttime.split(" ")
		endDate, endTime = stoptime.split(" ")
		startDate  = datetime.strptime(startDate.strip(), "%m/%d/%Y")
		endDate  = datetime.strptime(endDate.strip(), "%m/%d/%Y")

		if len(startTime) == 8:
			startTime = datetime.strptime(startTime,FMT1)
		elif len(startTime) == 5:
			startTime = datetime.strptime(startTime,FMT2)
		elif len(startTime) == 2:
			startTime = datetime.strptime(startTime,FMT3)
		
		if len(endTime) == 8:
			endTime = datetime.strptime(endTime,FMT1)
		elif len(endTime) == 5:
			endTime = datetime.strptime(endTime,FMT2)
		elif len(startTime) == 2:
			endTime = datetime.strptime(endTime,FMT3)

		startTimeMin = int(startTime.strftime("%M"))
		endTimeMin = int(endTime.strftime("%M"))
		startTimeHr = int(startTime.strftime("%H"))
		endTimeHr = int(endTime.strftime("%H"))
		if endTimeMin < startTimeMin:
			startTimeMin = 60 - int(startTime.strftime("%M"))
			endTimeMin = int(endTime.strftime("%M"))
			duration = endTimeMin+startTimeMin
		else:
			duration = int(endTime.strftime("%M")) - int(startTime.strftime("%M"))
		if endTimeHr - startTimeHr > 1:
			duration = duration + 60 * (endTimeHr - startTimeHr)
		#print "end: "+startTime.strftime(FMT2)+" end: "+endTime.strftime(FMT2)+" duration : "+str(duration)
		if int(gender) == 1:
			genderValue = "male"
		elif int(gender) == 2:
			genderValue = "female"
		else:
			genderValue = "unknown"
		print "{0}\t{1},{2}".format(genderValue,1,duration)
	except:
		pass
	
