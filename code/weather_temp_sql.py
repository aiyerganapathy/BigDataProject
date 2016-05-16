#!/usr/bin/env python

from pyspark.sql import SQLContext, Row
from pyspark import SparkContext
from decimal import Decimal


sc = SparkContext("local", "Simple App")

sqlContext = SQLContext(sc)

lines = sc.textFile("citi1.csv")
parts = lines.map(lambda l: l.split(","))
citi = parts.map(lambda p: Row(bikeid = int(p[0]),tripduration = float(p[1]),starttime = (p[2]).encode('utf-8').strip(),stoptime = (p[3]).encode('utf-8').strip(),start_station_id = float(p[4]),start_station_name = (p[5]).encode('utf-8').strip(),end_station_id= float(p[6]),end_station_name = (p[7]).encode('utf-8').strip(),usertype = (p[8]).encode('utf-8').strip(),gender = (p[9]).encode('utf-8').strip(),start_station_latitude = Decimal(p[10]),start_station_longitude = Decimal(p[11]),end_station_latitude = Decimal(p[12]),end_station_longitude= Decimal(p[13])))

#linesFromWind = sc.textFile("/home/rk2795/project/weather_wind_clean.txt")
#partsForWindData = linesFromWind.map(lambda l: l.split(","))
#windByDate = partsForWindData.map(lambda p: Row(date=p[0], wind=int(p[1])))

#linesFromVisibility = sc.textFile("/home/rk2795/project/weather_visibility_clean.txt")
#partsForVisibilityData = linesFromVisibility.map(lambda l: l.split(","))
#visibilityByDate = partsForVisibilityData.map(lambda p: Row(date=p[0], visibility=int(p[1])))


schemaCiti = sqlContext.createDataFrame(citi)
schemaCiti.registerTempTable("citi")
schemaCiti.write.parquet("citi.parquet")

#schemaWind = sqlContext.createDataFrame(windByDate)
#schemaWind.registerTempTable("wind")
#schemaWind.write.parquet("wind.parquet")

#schemaVisibility = sqlContext.createDataFrame(visibilityByDate)
#schemaVisibility.registerTempTable("visibility")
#schemaVisibility.write.parquet("visibilityByDate.parquet")





