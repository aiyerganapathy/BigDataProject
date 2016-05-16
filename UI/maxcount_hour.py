#!/usr/bin/env python
file_citi=open('city_weather.csv','r')
file_citi1=open('final_result_citi_peak.csv','w')
prev_date=""
count=0
max_count=0
max_count_index=0
for line in file_citi:
    splits=line.split(",")
    if prev_date=="":
        prev_date=splits[0]
        max_count=int(splits[4])
        max_count_index=1
        count+=1
    elif prev_date!=splits[0]:
        file_citi1.write(prev_date+","+str(max_count_index)+","+str(max_count)+"\n")
        prev_date=splits[0]
        print(splits)
        max_count=int(splits[4])
        max_count_index=1
        count=1
    else:
        if int(splits[4])>max_count:
            max_count=int(splits[4])
            max_count_index=count
        count+=1
file_citi1.write(prev_date+","+str(max_count_index)+","+str(max_count)+"\n")