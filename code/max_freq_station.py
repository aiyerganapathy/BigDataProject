#!/usr/bin/env python
from datetime import datetime
import sys

FMT1 = '%H:%M:%S'
FMT2 = '%H:%M'
FMT3 = '%H'

for line in sys.stdin:
	line = line.strip()
	try:
		bikeid,tripduration,starttime,stoptime,start_station_id,start_station_name,end_station_id,end_station_name,usertype,gender,start_station_latitude,start_station_longitude,end_station_latitude,end_station_longitude = line.split(",")
		pickup_date , pickup_time = starttime.split(" ")
		formatToApply = None
		dtDate  = datetime.strptime(pickup_date.strip(), "%m/%d/%Y")
		if len(pickup_time) == 8:
			formatToApply =FMT1
		elif len(pickup_time) == 5:
			formatToApply = FMT2
		else:
			formatToApply = FMT3
		dtHour = datetime.strptime(pickup_time.strip(),formatToApply)
		day = dtDate.strftime('%d')
		month = dtDate.strftime('%b')
		hours = dtHour.strftime('%H')
		print "{0},{1},{2},{3}\t{4},{5}".format(month,day,hours,start_station_id,1,start_station_name)
	except:
		pass