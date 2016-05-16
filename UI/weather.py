#!/usr/bin/env python
file_citi=open('city_weather.csv','r')
file_citi1=open('weather_freq_city.csv','w')
prev_date=""
wind=""
temp=""
visibility=""
total_count=0
for line in file_citi:
    splits=line.split(",")
    if prev_date=="":
        prev_date=splits[0]
        temp=splits[1]
        visibility=splits[2]
        wind=splits[3]
        total_count=int(splits[4])
    elif prev_date!=splits[0]:
        file_citi1.write(prev_date+","+temp+","+wind+","+visibility+","+str(total_count)+"\n")
        prev_date=splits[0]
        temp=splits[1]
        visibility=splits[2]
        wind=splits[3]
        total_count=int(splits[4])
    else:
        total_count+=int(splits[4])
file_citi1.write(prev_date+","+temp+","+wind+","+visibility+","+str(total_count)+"\n")