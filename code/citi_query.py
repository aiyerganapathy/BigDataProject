#!/usr/bin/env python


from pyspark.sql import SQLContext, Row
from pyspark import SparkContext


sc = SparkContext("local", "Simple App")

sqlContext = SQLContext(sc)
parquetFile = sqlContext.read.parquet("citi.parquet")

parquetFile.registerTempTable("citi")

citiData  = sqlContext.sql("select count( distinct bikeid) as bikecount from citi where usertype='Subscriber' ").collect()

#bikeIds = citiData.map(lambda p:" bikeid :"+p.bikeid) 

#print citiData[0].bikecount

for data in citiData.collect():
    print data;


