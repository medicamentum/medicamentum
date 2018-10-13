#!/usr/bin/env python
import glob
import sys
import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="drugs",
  passwd="Drug$Drug$2020",
  database="DRUGS"
)

path = sys.argv[1] + "/*.txt"

mycursor = mydb.cursor()

for file in glob.glob(path):
    content = open(file,"r").read()
    directory, filename = os.path.split(file)
    filename = filename.replace(".txt", "")
    sql = "INSERT INTO DRUG_LEAFTLET (leaflet, content) VALUES (%s, %s)"
    val = (filename, content)
    print(filename, " processing ...")
    mycursor.execute(sql, val)
    mydb.commit()

print("Done")