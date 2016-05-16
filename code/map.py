#!/usr/bin/env python
import sys
from datetime import datetime
from pytz import timezone

est_tz = timezone('US/Eastern')
gmt_tz = timezone('GMT')

for line in sys.stdin:
	line = line.strip()
	line = ' '.join(line.split())
	data = line.split(" ")

	if(data[0] != 'USAF'):
		station_num, wban_num, date_time, wind_speed,visibility, temp, max_temp, min_temp = data[0],data[1],data[2],data[4], data[11], data[21], data[26], data[27]
		year = date_time[0:4]
		month = date_time[4:6]
		day = date_time[6:8]
		hour = date_time[8:10]
		mins = date_time[10:12]
		date  = datetime(int(year), int(month),int(day), int(hour), int(mins), 0)
		gmtDate = gmt_tz.localize(date,is_dst = True)
		fmt = '%Y-%m-%d %H:%M:%S %Z%z'
		estDate = gmtDate.astimezone(est_tz)
		estDate = estDate.strftime(fmt)
		print "{0},{1}\t{2},{3},{4},{5},{6},{7}".format(station_num, wban_num, estDate, wind_speed,visibility, temp, max_temp, min_temp) 
