#!/usr/bin/env python
from datetime import datetime
import sys

for line in sys.stdin:
	line = line.strip()
	pickup_datetime, dropoff_datetime, passenger_count, trip_distance, pickup_longitude, pickup_latitude, ratecodeid, dropoff_longitude, dropoff_latitude, total_amount, fare_amount, payment_type, tip_amount = line.split(",")
	FMT1 = '%H:%M:%S'
	FMT2 = '%H:%M'
	FMT3 = '%H'
	pickup_date , pickup_time = pickup_datetime.split(" ")
	
	formatToApply = None
	dtDate  = datetime.strptime(pickup_date.strip(), "%d-%b-%Y")
	if len(pickup_time) == 8:
		formatToApply =FMT1
	elif len(pickup_datetime) == 5:
		formatToApply = FMT2
	else:
		formatToApply = FMT3
	dtHour = datetime.strptime(pickup_time.strip(),formatToApply)
	day = dtDate.strftime('%d')
	month = dtDate.strftime('%b')
	hours = dtHour.strftime('%H')
	print "{0},{1},{2}\t{3}".format(month,day,hours,total_amount)