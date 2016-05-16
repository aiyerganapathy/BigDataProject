#!/usr/bin/env python
from datetime import datetime
import sys

previousTag = None
previousDate = None
taxiData = []

weather_tag = {'wind':"",'temp':"",'visibility':""}

for line in sys.stdin:
    try:
        line = line.strip()
        key, value = line.split("\t")
        values = value.split(",")
        date = key.split(",")

        # print "value 0 : "+values[0]+" value 1 :"+values[1]+" key : "+key
        if previousDate and previousDate == key:
            if values[0] == 'taxi':
                taxiData.append(values[1])
            elif values[0] != 'taxi':
                weather_tag[values[0]] = values[1]

        elif previousDate and previousDate != key:
            for val in taxiData:
                print "{0},{1},{2}".format(date[1] + "-" + date[0] + "-2015", weather_tag['wind']+","+weather_tag['temp']+","+weather_tag['visibility'], val)
            previousDate = None
            weather_tag['wind'] = ""
            weather_tag['temp'] = ""
            weather_tag['visibility'] = ""

        else:
            previousDate = key
            previousTag = values[0]
            taxiData = []
            weather_tag = {'wind': "", 'temp': "", 'visibility': ""}
            if values[0] == 'taxi':
                taxiData.append(values[1])
            else:
                weather_tag[values[0]] = values[1]
    except Exception as e:
        print e.message
